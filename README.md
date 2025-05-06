# churn-indicators

Python tool for computing customer health scores from usage signals and flagging at-risk accounts before they churn.

## Architecture

```
src/
  features.py     extract_features() — normalises raw CRM/usage data into feature dict
  scorer.py       score_account(), score_all() — weighted health score 0-100 and risk tier
  alerts.py       high_risk_accounts(), at_risk_mrr(), print_alerts()
  main.py         entry point — loads CSV, scores, prints table and alerts
data/
  accounts.csv    sample account data (anonymised)
tests/
  test_scorer.py
```

## Health score components

| Signal | Weight | Notes |
|---|---|---|
| Login frequency (logins / 90 days) | 25% | Low logins = disengaged |
| Seat utilisation (used / total) | 25% | Low utilisation = weak adoption |
| Open support tickets | 20% | High tickets = friction or dissatisfaction |
| Days since last login | 20% | Recency matters as much as frequency |
| NPS score | 10% | Direct satisfaction signal |

## Quickstart

```bash
pip install -r requirements.txt
python -m src.main
pytest tests/
```

## Motivation

Built after a QBR where three accounts churned in the same month and the CS team said they had no early warning. I mapped the signals we had available in the CRM and usage logs and built a simple composite score. We ran it weekly from then on and contacted accounts before their renewal conversations.

## Future work

- Add contract renewal date to surface accounts churning within 90 days
- Connect to CRM API instead of CSV export
- Add email digest output for CS team
