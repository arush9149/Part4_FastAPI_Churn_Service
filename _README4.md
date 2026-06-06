
# D2C Customer Churn Prediction API

## Overview

This project provides a FastAPI service for predicting customer churn risk.

The API uses the Logistic Regression churn model developed in Part 3 and returns:

- Churn probability
- Predicted class (0 = No Churn, 1 = Churn)
- Risk explanation

---

## Project Structure

.
├── app/
│   └── main.py
├── tests/
│   └── test_cases.py
├── model.pkl
├── requirements.txt
├── monitoring_plan.md
└── README.md

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Run API

uvicorn app.main:app --reload

---

## Endpoints

### Health Check

GET /health

Response:

{
  "status": "healthy"
}

---

### Single Prediction

POST /predict

Example Request:

{
  "city_tier": "Tier 1",
  "age_group": "25-34",
  "acquisition_channel": "Instagram",
  "loyalty_tier": "Silver",
  "preferred_category": "Skin Care",
  "marketing_consent": "Yes",
  "recency_days": 30,
  "frequency_180d": 5,
  "monetary_180d": 4000,
  "return_rate_180d": 0.05,
  "avg_discount_pct_180d": 10,
  "avg_rating_180d": 4.5,
  "category_diversity_180d": 3,
  "ticket_count_90d": 0,
  "negative_ticket_rate_90d": 0.0,
  "avg_resolution_hours_90d": 0.0,
  "days_since_signup": 400,
  "sessions_30d": 12,
  "product_views_30d": 50,
  "cart_adds_30d": 6,
  "wishlist_adds_30d": 2,
  "abandoned_carts_30d": 1,
  "email_opens_30d": 5,
  "campaign_clicks_30d": 2,
  "last_visit_days_ago": 3
}

Example Response:

{
  "churn_probability": 0.18,
  "prediction": 0,
  "risk_explanation": "Low churn risk"
}

---

### Batch Prediction

POST /batch_predict

Accepts a list of customer payloads and returns predictions for all customers.

---

## Testing

Three API test payloads are available in:

tests/test_cases.py

---

## Monitoring

Refer to monitoring_plan.md for:

- Data drift monitoring
- Prediction monitoring
- Business outcome monitoring
- API monitoring
- Retraining triggers
- Responsible use guidance
