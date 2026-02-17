import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from filters import by_risk, above_mrr, below_health, escalate_candidates


ACCOUNTS = [
    {'account_id': 'a1', 'churn_risk': 'high',   'mrr_usd': 5000.0, 'health_score': 30.0},
    {'account_id': 'a2', 'churn_risk': 'medium',  'mrr_usd': 2000.0, 'health_score': 55.0},
    {'account_id': 'a3', 'churn_risk': 'low',     'mrr_usd':  500.0, 'health_score': 80.0},
    {'account_id': 'a4', 'churn_risk': 'high',    'mrr_usd':  200.0, 'health_score': 25.0},
]


def test_by_risk():
    assert len(by_risk(ACCOUNTS, 'high')) == 2


def test_above_mrr():
    assert len(above_mrr(ACCOUNTS, 1000.0)) == 2


def test_below_health():
    assert len(below_health(ACCOUNTS, 50.0)) == 2


def test_escalate_candidates():
    candidates = escalate_candidates(ACCOUNTS, mrr_floor=1000.0)
    assert len(candidates) == 1
    assert candidates[0]['account_id'] == 'a1'
