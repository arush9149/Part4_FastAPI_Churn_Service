from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib

app = FastAPI(
    title="D2C Churn Prediction API"
)

model = joblib.load("model.pkl")

THRESHOLD = 0.43

class CustomerFeatures(BaseModel):

    city_tier: str
    age_group: str
    acquisition_channel: str
    loyalty_tier: str | None = None
    preferred_category: str
    marketing_consent: str

    recency_days: int
    frequency_180d: int
    monetary_180d: float
    return_rate_180d: float
    avg_discount_pct_180d: float
    avg_rating_180d: float

    category_diversity_180d: int
    ticket_count_90d: int
    negative_ticket_rate_90d: float
    avg_resolution_hours_90d: float

    days_since_signup: int
    sessions_30d: int
    product_views_30d: int
    cart_adds_30d: int
    wishlist_adds_30d: int
    abandoned_carts_30d: int

    email_opens_30d: int
    campaign_clicks_30d: int
    last_visit_days_ago: int

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(customer: CustomerFeatures):

    df = pd.DataFrame([customer.model_dump()])

    probability = float(
        model.predict_proba(df)[0][1]
    )

    prediction = int(
        probability >= THRESHOLD
    )

    if probability >= 0.70:
        risk = "High churn risk"
    elif probability >= THRESHOLD:
        risk = "Medium churn risk"
    else:
        risk = "Low churn risk"

    return {
        "churn_probability": round(probability, 4),
        "prediction": prediction,
        "risk_explanation": risk
    }

@app.post("/batch_predict")
def batch_predict(
    customers: List[CustomerFeatures]
):

    df = pd.DataFrame(
        [c.model_dump() for c in customers]
    )

    probabilities = model.predict_proba(df)[:,1]

    results = []

    for p in probabilities:

        pred = int(p >= THRESHOLD)

        if p >= 0.70:
            risk = "High churn risk"
        elif p >= THRESHOLD:
            risk = "Medium churn risk"
        else:
            risk = "Low churn risk"

        results.append({
            "churn_probability": round(float(p), 4),
            "prediction": pred,
            "risk_explanation": risk
        })

    return {"results": results}
