from pathlib import Path
import joblib, pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.schemas import CustomerInput
ROOT=Path(__file__).resolve().parent.parent
model=joblib.load(ROOT/"models"/"champion.joblib")
app=FastAPI(title="Telco Churn API")
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/", response_class=HTMLResponse)
def home(): return (ROOT/"templates"/"index.html").read_text(encoding="utf-8")
@app.post("/predict")
def predict(customer: CustomerInput):
    x=pd.DataFrame([customer.model_dump()]); p=float(model.predict_proba(x)[0,1]); y=int(model.predict(x)[0])
    return {"prediction":y,"churn_probability":p,"risk_level":"Bajo" if p<.3 else "Medio" if p<.7 else "Alto"}
