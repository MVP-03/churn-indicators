import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.features import extract_features
from src.scorer import score_all
from src.alerts import print_alerts, at_risk_mrr

DATA = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'accounts.csv')


def main() -> None:
    with open(DATA, newline='', encoding='utf-8') as f:
        raw = list(csv.DictReader(f))

    features = extract_features(raw)
    scored = score_all(features)

    print(f"\n  Health Scores  ({len(scored)} accounts)")
    print(f"  {'Company':<26} {'Health':>7}  {'Risk':<8}  {'MRR':>8}  {'Last login':>10}")
    print(f"  {'-'*26} {'-'*7}  {'-'*8}  {'-'*8}  {'-'*10}")
    for acc in scored:
        print(
            f"  {acc['company']:<26} "
            f"{acc['health_score']:>6.1f}%  "
            f"{acc['churn_risk']:<8}  "
            f"${acc['mrr_usd']:>7,.0f}  "
            f"{acc['days_since_last_login']:>9}d"
        )

    print(f"\n  At-risk MRR: ${at_risk_mrr(scored):,.0f}")
    print()
    print_alerts(scored)
    print()


if __name__ == '__main__':
    main()
