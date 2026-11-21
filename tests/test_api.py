from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
SAMPLE={"tenure":5,"MonthlyCharges":85.5,"TotalCharges":427.5,"Contract":"Month-to-month","InternetService":"Fiber optic"}
def test_health():
    response=client.get("/health")
    assert response.status_code==200
    assert response.json()=={"status":"ok"}
def test_home():
    response=client.get("/")
    assert response.status_code==200
    assert "Telco Churn Predictor" in response.text
def test_predict():
    response=client.post("/predict",json=SAMPLE)
    assert response.status_code==200
    body=response.json()
    assert body["prediction"] in (0,1)
    assert 0<=body["churn_probability"]<=1
def test_validation():
    response=client.post("/predict",json={**SAMPLE,"tenure":-1})
    assert response.status_code==422
