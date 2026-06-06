
# Monitoring Plan

## 1. Data Drift Monitoring
Track changes in input feature distributions such as:
- recency_days
- frequency_180d
- monetary_180d
- sessions_30d

Investigate significant deviations from training data.

## 2. Prediction Distribution
Monitor:
- Average churn probability
- Percentage of customers predicted as churners

Large shifts may indicate model degradation.

## 3. Business Outcomes
Track:
- Actual churn rate
- Retention campaign success rate
- Revenue retained from intervention campaigns

Compare outcomes against model predictions.

## 4. API Monitoring
Track:
- API uptime
- Request volume
- Response time
- Error rates

Investigate abnormal spikes in failures.

## 5. Retraining Triggers
Retrain the model when:
- Prediction performance declines significantly
- Data drift is detected
- New customer behavior patterns emerge
- At least 6 months of new data becomes available

## Responsible Use

This API should be used to prioritize retention efforts and identify potentially at-risk customers.

The output should not be used as the sole basis for denying services, benefits, or opportunities. Human review and business context should always be considered before taking action.
