# 🧮 Calculator API

A simple FastAPI-based microservice that performs basic arithmetic operations (addition, subtraction, multiplication, division).  
This project demonstrates clean development practices and applies several [12-Factor App](https://12factor.net/) principles.

## 🚀 Features

- FastAPI application with clean routing
- Environment-based configuration using `pydantic-settings`
- Docker support for easy deployment
- RESTful endpoints for basic arithmetic operations
- CI-ready structure for testing and automation

## 🔧 Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic Settings
- Pytest
- Docker
- GitHub Actions (for CI/CD)

## 📂 Project Structure


▶️ Running Locally
1. Clone the repo
git clone https://github.com/Tech-74-root/Fuse_API.git
cd calculator-api

2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt

3. Launch the app
uvicorn app.main:app --reload
Then visit: http://127.0.0.1:8000/docs

