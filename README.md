# AiExamteeth
Overview

AiExamteeth is a hackathon prototype that uses AI to analyze dental X-ray images. It detects cavities, maps them to tooth numbers/regions (Universal or FDI notation), and generates dentist-style outputs. The system also includes a chatbot that explains findings in patient-friendly language and can simulate insurance cost estimates.

⚠️ Disclaimer: This is a prototype for educational/demo purposes only — not a medical device and not intended for clinical diagnosis.

Features

X-ray analysis: Uses YOLOv8 (or mock fallback) to detect caries.

Tooth numbering: Maps detections to tooth IDs and regions (MO/DO/BO/LO).

Visual overlay: Draws bounding boxes on the X-ray.

Dentist-style output: Lists findings in standardized notation.

Patient chatbot: Powered by OpenAI API to explain results in plain language.

Insurance engine (mock): Produces a JSON estimate of plan vs patient costs.

Two demo options:

Gradio UI (app.py) — fast prototype

Flask + HTML/CSS (server.py) — realistic web app
