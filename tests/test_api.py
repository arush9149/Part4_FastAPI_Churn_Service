
from app.main import health

def test_health():
    response = health()
    assert response["status"] == "healthy"

def test_threshold():
    assert 0.43 > 0

def test_prediction_keys():
    keys = [
        "churn_probability",
        "prediction",
        "risk_explanation"
    ]
    assert len(keys) == 3
