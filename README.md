🔬 Deep Research Agent

An AI-powered Deep Research Agent that automatically plans research, performs multiple web searches, generates a detailed research report, and sends the final report via email.

🚀 Live Demo

**Note on Deployment:** This application is hosted on Render's free tier. If the service has been inactive, the initial startup may take approximately 1 minute. Please allow some time for the application to wake up on the first visit.
👉 https://deep-research-agent-ktwl.onrender.com/

📌 Features
🧠 Planner Agent - Breaks the user's research query into multiple search tasks.
🔎 Custom Web Search Tool - Uses the Serper API to perform web searches.
⚡ Parallel Searching - Performs multiple searches concurrently using AsyncIO.
📝 Writer Agent - Combines the collected research and generates a detailed Markdown report.
📧 Email Agent - Converts the report into a clean email and sends it.
📊 Structured Outputs - Uses Pydantic models for structured agent responses.
🌐 Web Interface - Built with Gradio.
☁️ Deployment - Deployed on Render.

🏗️ Architecture

                    User Query
                        │
                        ▼
                 ┌─────────────┐
                 │ Planner Agent│
                 └──────┬──────┘
                        │
                 Search Queries
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
     Search Agent  Search Agent  Search Agent
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                 Custom Web Search
                        │
                        ▼
                    Serper API
                        │
                        ▼
                 Research Results
                        │
                        ▼
                  Writer Agent
                        │
                        ▼
                  Final Report
                        │
                        ▼
                  Email Agent
                        │
                        ▼
                 Email / Notification
                 
🛠️ Tech Stack
Python
OpenAI Agents SDK
Gemini
Serper API
Pydantic
AsyncIO
Gradio
Render
