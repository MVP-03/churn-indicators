import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.features import extract_features
from src.scorer import score_account, score_all
from src.alerts import high_risk_accounts, at_risk_mrr

HEALTHY = {
    'account_id': 'a-h', 'company': 'HealthyCo', 'mrr_usd': '5000',
    'logins_last_90d': '60', 'seats_used': '18', 'seats_total': '20',
    'open_support_tickets': '0', 'days_since_last_login': '2',
    'days_since_onboarding': '300', 'nps_score': '9',
}
RISKY = {
    'account_id': 'a-r', 'company': 'RiskyCo', 'mrr_usd': '3000',
    'logins_last_90d': '2', 'seats_used': '1', 'seats_total': '20',
    'open_support_tickets': '6', 'days_since_last_login': '55',
    'days_since_onboarding': '120', 'nps_score': '2',
}


def test_healthy_account_gets_low_risk():
    features = extract_features([HEALTHY])[0]
    scored = score_account(features)
    assert scored['churn_risk'] == 'low'
    assert scored['health_score'] >= 70


def test_risky_account_gets_high_risk():
    features = extract_features([RISKY])[0]
    scored = score_account(features)
    assert scored['churn_risk'] == 'high'
    assert scored['health_score'] < 45


def test_score_all_sorted_ascending():
    features = extract_features([HEALTHY, RISKY])
    scored = score_all(features)
    assert scored[0]['health_score'] <= scored[1]['health_score']


def test_high_risk_accounts_filter():
    features = extract_features([HEALTHY, RISKY])
    scored = score_all(features)
    high = high_risk_accounts(scored)
    assert all(a['churn_risk'] == 'high' for a in high)


def test_at_risk_mrr_includes_medium_and_high():
    features = extract_features([HEALTHY, RISKY])
    scored = score_all(features)
    mrr = at_risk_mrr(scored)
    assert mrr >= 3000


def test_seat_utilisation_computed():
    features = extract_features([HEALTHY])[0]
    assert abs(features['seat_utilisation'] - 0.9) < 0.01


def test_login_frequency_computed():
    features = extract_features([HEALTHY])[0]
    assert features['login_frequency'] == round(60 / 90, 3)
