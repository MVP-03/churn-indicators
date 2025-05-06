from typing import List, Dict


def high_risk_accounts(scored: List[Dict]) -> List[Dict]:
    return [a for a in scored if a['churn_risk'] == 'high']


def at_risk_mrr(scored: List[Dict]) -> float:
    return round(sum(a['mrr_usd'] for a in scored if a['churn_risk'] in ('high', 'medium')), 2)


def format_alert(account: Dict) -> str:
    return (
        f"[ALERT] {account['company']} — "
        f"health {account['health_score']}% | "
        f"last login {account['days_since_last_login']}d ago | "
        f"tickets {account['open_support_tickets']} | "
        f"MRR ${account['mrr_usd']:,.0f}"
    )


def print_alerts(scored: List[Dict]) -> None:
    high = high_risk_accounts(scored)
    if not high:
        print("  No high-risk accounts.")
        return
    print(f"  High-risk accounts ({len(high)}):")
    for acc in high:
        print(f"    {format_alert(acc)}")
    print(f"\n  At-risk MRR: ${at_risk_mrr(scored):,.0f}")
