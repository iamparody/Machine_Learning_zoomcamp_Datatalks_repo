# ML Zoomcamp Week 5 - Deployment Exercise

## Folder Structure
uv_homework/
├─ pipeline_v1.bin # Local model
├─ pipeline_v2.bin # Docker base image model
├─ main.py # Predict single record
├─ app.py # FastAPI app
├─ test_client.py # Test POST requests
├─ Dockerfile # Dockerfile for deployment
├─ pyproject.toml
├─ uv.lock
├─ venv/ or .venv/



---

## Local Prediction (Q3)

.\venv\Scripts\Activate.ps1
pip install scikit-learn
python main.py
Expected: Probability of conversion: 0.282

FastAPI Service (Q4)
powershell
Copy code
pip install fastapi uvicorn requests
uvicorn app:app --reload
python test_client.py
Expected: {"conversion_probability": 0.356}

Docker Simulation (Q5-Q6)
Base image: agrigorev/zoomcamp-model:2025 (size 121 MB)

Dockerfile


FROM agrigorev/zoomcamp-model:2025
WORKDIR /code
COPY app.py .
RUN pip install uvicorn fastapi requests
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
Build & Run


docker build -t mlzoomcamp_hw5 .
docker run -d -p 8000:8000 mlzoomcamp_hw5
Test Client


import requests

url = "http://127.0.0.1:8000/predict"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

print(requests.post(url, json=client).json())
Expected probability: 0.59


---

This is short, self-contained, and all Markdown-ready for submission.  

I can also make an **even shorter “one-page cheat sheet” version** with only commands if you want someth
