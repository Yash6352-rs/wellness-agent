# 🧠 Wellness Agent – AI-Powered Daily Health Companion

A lightweight, browser-based wellness assistant that provides instant, AI-generated lifestyle feedback based on daily inputs like sleep, hydration, mood, and activity — all without any devices, wearables, or logins.


This project was developed as part of the 15-day internship under GTU in collaboration with IBM SkillBuild and CSRBOX. The program focused on applying AI and emerging technologies to solve real-world problems. "Wellness Agent" is the final submission, showcasing the practical implementation of AI-powered wellness tracking using open-source tools.

> " A free daily health checkup guided by Wellness Agent — built for students, by students.."

---

## Project Overview

In today’s fast-paced world, people often ignore key wellness habits — leading to chronic health issues. Wellness Agent helps users **self-reflect on their daily lifestyle** in under 2 minutes through a smart, accessible interface that gives empathetic feedback powered by **Gemini 1.5 AI**.

---

## Features

-  **No wearables, no login** – Fully browser-based
-  **AI-generated lifestyle insights** – Powered by Gemini 1.5 Flash
-  **Personalized health classification** – Healthy / Risky / Unhealthy
-  **Instant feedback & motivational tips**
-  **Downloadable session summaries**
-  **Mobile-friendly interface**
-  **Free and privacy-respecting** – No data is uploaded or stored externally

---

##  Tech Stack

| Component        | Technology             |
|------------------|-------------------------|
| Frontend         | HTML, CSS               |
| Backend          | Flask (Python)          |
| AI Agent Logic   | LangGraph, LangChain    |
| LLM              | Gemini 1.5 Flash (via Google Generative AI) |
| Storage Format   | JSON (local session logs) |
| Env Management   | `python-dotenv`         |

---

##  Project Structure



---


## Getting Started

### 1. Clone the Repository
- git clone https://github.com/YOUR_USERNAME/wellness-agent.git
- cd wellness-agent

### 2. Set Up Environment
   
Install required packages:
- pip install -r requirements.txt

Create a .env file in the root folder and add your Gemini API key:
- GEMINI_API_KEY=your-gemini-api-key-here

### 3. Run the App
- python app.py
- Then open http://127.0.0.1:5000 in your browser.

---

## How It Works

1. User fills a quick wellness form (sleep, food, water, mood, etc.)
2. LangGraph agents validate and route data through Gemini AI
3. Gemini classifies health status + generates personalized advice
4. Output is shown and logged locally as a .json session
5. User gets a motivational tip and can download the result

---

## Security & Privacy

- No login or account needed
- No personal data stored externally
- All session data saved locally in logs/
- API keys hidden via .env

---

## Use Cases

- Daily health reflection tool for students
- Digital wellness check-ins in schools or NGOs
- Awareness tool for rural or underprivileged communities

---

## Screenshots

### 1. Wellness Input Form 

- This is the initial screen where users enter their daily wellness data — including sleep, water intake, food, activity, and mood. It’s clean, mobile-friendly, and quick to use.
  
<img width="904" height="848" alt="image" src="https://github.com/user-attachments/assets/e21aef55-da68-4291-b5d7-589fe49544d8" />

### 2. Gemini-generated advice 

- Based on the inputs, our agentic AI classifies the user’s health as Healthy, Risky, or Unhealthy, and provides personalized suggestions. This feedback mimics how a digital wellness coach might respond.
- Start Over button: 

<img width="886" height="958" alt="image" src="https://github.com/user-attachments/assets/7a43e580-56b6-4378-a527-07a12f7a6cd1" />

---

## License

- This project is open-source under the MIT License.
- Feel free to fork, use, or build on it for educational or non-commercial purposes.

---

## Acknowledgments

- Built as part of the IBM AI-ML Internship
- Developed by Yash Panchal
- Powered by Google Gemini, LangGraph, and Flask

---

 ## Links
 
- [GitHub Repository](https://github.com/Yash6352-rs/wellness-agent)  
- [Email](mailto:yashpanchal1422004@gmail.com)  
- [LinkedIn Profile](https://www.linkedin.com/in/yash6352-rs/)


Feel free to explore, contribute, or reach out for collaboration opportunities!


