import os
import json
import uuid
from datetime import datetime
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key

from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")


# Initialize Gemini Model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    temperature=0.3
)

# Validate Input

def data_validator(state: dict) -> dict:
    try:
        state["sleep"] = float(state.get("sleep", 0))
        state["water"] = float(state.get("water", 0))
    except ValueError:
        state["sleep"] = 6
        state["water"] = 5
    for key in ["food", "activity", "mood"]:
        if not state.get(key):
            state[key] = "Not mentioned"
    return state

# Classify Status with Gemini

def classify_status(state: dict) -> dict:
    prompt = f"""
You are a friendly health assistant. Analyze the user's wellness data and provide a short summary.

- Sleep: {state['sleep']} hrs
- Water: {state['water']} glasses
- Food: {state['food']}
- Activity: {state['activity']}
- Mood: {state['mood']}

Explain how they're doing and suggest small improvements (2 lines).
"""
    response = llm.invoke(prompt)
    state["status_summary"] = response.content.strip()
    return state


# Router Decide Path

def router(state: dict) -> str:
    prompt = f"""
Classify this user's health based on the following summary into one of these categories:
- Healthy
- Risky
- Unhealthy

Summary:
{state['status_summary']}

Respond with only one word.
"""
    response = llm.invoke(prompt)
    result = response.content.strip().lower()
    return "healthy" if "healthy" in result else "unhealthy" if "unhealthy" in result else "risky"


# Healthy Agent

def healthy_agent(state: dict) -> dict:
    prompt = f"""
User appears healthy:
- Sleep: {state['sleep']} hrs
- Water: {state['water']} glasses
- Food: {state['food']}
- Activity: {state['activity']}
- Mood: {state['mood']}

Give 2 lines of encouragement and 2 tips to maintain it.
"""
    state["response"] = llm.invoke(prompt).content.strip()
    state["category"] = "healthy"
    return state


# Risky Agent

def risky_agent(state: dict) -> dict:
    prompt = f"""
User's wellness shows some risk:
- Sleep: {state['sleep']} hrs
- Water: {state['water']} glasses
- Food: {state['food']}
- Activity: {state['activity']}
- Mood: {state['mood']}

Give a friendly warning and 3 tips to improve.
"""
    state["response"] = llm.invoke(prompt).content.strip()
    state["category"] = "risky"
    return state


# Unhealthy Agent

def unhealthy_agent(state: dict) -> dict:
    prompt = f"""
User's habits suggest serious concern:
- Sleep: {state['sleep']} hrs
- Water: {state['water']} glasses
- Food: {state['food']}
- Activity: {state['activity']}
- Mood: {state['mood']}

Gently alert them. Suggest 2 improvements and recommend consulting a doctor if it persists.
"""
    state["response"] = llm.invoke(prompt).content.strip()
    state["category"] = "unhealthy"
    return state


# Summary Logger 

def summary_logger(state: dict) -> dict:
    log = {
        "id": str(uuid.uuid4()),
        "timestamp": str(datetime.now()),
        "inputs": {
            "sleep": state["sleep"],
            "water": state["water"],
            "food": state["food"],
            "activity": state["activity"],
            "mood": state["mood"]
        },
        "category": state.get("category", ""),
        "response": state.get("response", "")
    }
    os.makedirs("logs", exist_ok=True)
    with open(f"logs/session_{log['id']}.json", "w") as f:
        json.dump(log, f, indent=2)
    return state


# Suggest Final Step

def suggest_next_step(state: dict) -> dict:
    prompt = f"""
Summarize the session in 2 lines and give one motivational or practical next step.
Category: {state.get('category')}
Response: {state.get('response')}
"""
    state["final_tip"] = llm.invoke(prompt).content.strip()
    return state


# Build LangGraph Workflow

def run_agent(user_data: dict) -> dict:
    builder = StateGraph(dict)
    builder.set_entry_point("data_validator")
    builder.add_node("data_validator", data_validator)
    builder.add_node("classify_status", classify_status)
    builder.add_node("router_node", classify_status)  # reuse
    builder.add_node("healthy", healthy_agent)
    builder.add_node("risky", risky_agent)
    builder.add_node("unhealthy", unhealthy_agent)
    builder.add_node("summary_logger", summary_logger)
    builder.add_node("suggest_next_step", suggest_next_step)

    builder.add_edge("data_validator", "classify_status")
    builder.add_edge("classify_status", "router_node")
    builder.add_conditional_edges("router_node", router, {
        "healthy": "healthy",
        "risky": "risky",
        "unhealthy": "unhealthy"
    })
    builder.add_edge("healthy", "summary_logger")
    builder.add_edge("risky", "summary_logger")
    builder.add_edge("unhealthy", "summary_logger")
    builder.add_edge("summary_logger", "suggest_next_step")
    builder.add_edge("suggest_next_step", END)

    graph = builder.compile()
    return graph.invoke(user_data)
