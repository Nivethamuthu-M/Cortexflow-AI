# CortexFlow AI

*Agentic AI Backend – Real-Time Intelligent Assistant System*

CortexFlow AI is a *modular, FastAPI-powered backend* that demonstrates an *agent-based intelligent system*, where multiple independent agents collaborate to handle different tasks such as document understanding, meeting data retrieval, and external information lookup.

This project is built to clearly showcase how *agentic workflows* can be designed in a backend system for *learning, demos, and academic purposes*.

---

##  Project Highlights

- *Agent-based backend architecture*
- *Real-time intelligent request handling*
- *Document question answering with fallback intelligence*
- *SQLite-powered meeting query system*
- *Clean, beginner-friendly FastAPI structure*

---

##  Technologies Used

- *Python*
- *FastAPI*
- *SQLite*
- *DuckDuckGo Search*
- *PyPDF2*
- *Uvicorn*

---

##  Project Overview

CortexFlow AI follows a *multi-agent design, where each agent focuses on a **single responsibility*.

Instead of using one large logic block, the system intelligently routes user queries to the *most suitable agent*, improving scalability and clarity.

---

##  Core Agents

- *Document Intelligence Agent*  
  Answers questions from uploaded PDF or text files

- *Web Search Agent*  
  Fetches answers from the web when documents do not contain the information

- *Database Agent*  
  Retrieves meeting data from an SQLite database

- *Agent Controller*  
  Coordinates all agents to generate structured responses

This architecture ensures *scalability, clarity, and easy extension*.

---

##  Features

- *Modular agent-based backend design*
- *PDF and text-based question answering*
- *Intelligent web search fallback*
- *SQLite-based meeting scheduler queries*
- *Interactive FastAPI Swagger UI*
- *Easy-to-understand project layout*

---

##  Project Structure

```text
cortexflow-ai/
│
├── main.py                   # FastAPI application entry point
├── agents/
│   ├── document_agent.py     # Document Q&A agent
│   ├── db_agent.py           # SQLite database agent
│   ├── weather_agent.py      # Optional external info agent
│   └── _init_.py
│
├── database/
│   └── meetings.db           # SQLite database file
│
├── requirements.txt
├── .gitignore
└── README.md
```
---
## **Installation & Setup**

Step 1: Clone the Repository
git clone https://github.com/<your-username>/cortexflow-ai.git
cd cortexflow-ai
Step 2: Create a Virtual Environment
python -m venv venv
Step 3: Activate the Virtual Environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
You should see:
(venv)
Step 4: Install Dependencies
pip install -r requirements.txt
If requirements.txt is missing:
pip install fastapi uvicorn python-multipart PyPDF2 duckduckgo-search

---
## **Running the Application**
uvicorn main:app --reload
Application will run at:
http://127.0.0.1:8000

---
## **API Usage**
Open Swagger UI:
http://127.0.0.1:8000/docs
You can:
Upload documents
Ask questions from documents
Query meetings (today / tomorrow / all)
Test all endpoints interactively

---
## **Learning Outcomes**
Understanding agentic system architecture
Building REST APIs using FastAPI
Handling file uploads and PDF parsing
Working with SQLite databases
Organizing scalable backend projects
Practical Git & GitHub usage

---
## **Future Enhancements** 
Semantic search using embeddings
Authentication and role-based access
Frontend integration (React / Next.js)
Cloud deployment
Advanced multi-agent coordination

---
## **Author**
 Nivetha,
 Computer Science Engineering Student
Passionate about Frontend & Backend Development, AI-powered systems, and creating practical, real-world solutions

---
## **Ideal For**
Academic mini & major projects
Backend architecture demonstrations
AI workflow experimentation
Learning FastAPI and agent-based design

---
## ** CortexFlow AI** 
– Where intelligent agents collaborate to deliver smarter backend systems
