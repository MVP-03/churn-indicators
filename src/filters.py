from typing import List, Dict


def by_risk(accounts: List[Dict], risk: str) -> List[Dict]:
    return [a for a in accounts if a.get('churn_risk') == risk]


def above_mrr(accounts: List[Dict], threshold: float) -> List[Dict]:
    return [a for a in accounts if a.get('mrr_usd', 0) >= threshold]


def below_health(accounts: List[Dict], score: float) -> List[Dict]:
    return [a for a in accounts if a.get('health_score', 100) < score]


def escalate_candidates(accounts: List[Dict], mrr_floor: float = 1000.0) -> List[Dict]:
    high_risk = by_risk(accounts, 'high')
    return above_mrr(high_risk, mrr_floor)
