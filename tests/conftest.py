import pytest


@pytest.fixture
def sample_account():
    return {
        'account_id': 'test-001', 'company': 'Acme Corp',
        'mrr_usd': 2500.0, 'logins_last_90d': 45,
        'seats_used': 8, 'seats_total': 10,
        'open_support_tickets': 1, 'days_since_last_login': 3,
        'days_since_onboarding': 90, 'nps_score': 8,
    }


@pytest.fixture
def high_risk_account():
    return {
        'account_id': 'test-002', 'company': 'At-Risk Inc',
        'mrr_usd': 1000.0, 'logins_last_90d': 2,
        'seats_used': 1, 'seats_total': 10,
        'open_support_tickets': 4, 'days_since_last_login': 55,
        'days_since_onboarding': 180, 'nps_score': 3,
    }
