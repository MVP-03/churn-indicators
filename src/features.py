from typing import List, Dict


def extract_features(accounts: List[Dict]) -> List[Dict]:
    result = []
    for acc in accounts:
        logins_90d = int(acc.get('logins_last_90d', 0) or 0)
        seats_used = int(acc.get('seats_used', 0) or 0)
        seats_total = int(acc.get('seats_total', 1) or 1)
        support_tickets = int(acc.get('open_support_tickets', 0) or 0)
        days_since_login = int(acc.get('days_since_last_login', 0) or 0)
        days_since_onboard = int(acc.get('days_since_onboarding', 0) or 0)
        nps = int(acc.get('nps_score', 7) or 7)
        mrr = float(acc.get('mrr_usd', 0) or 0)

        seat_utilisation = seats_used / seats_total if seats_total else 0.0
        login_frequency = logins_90d / 90.0

        result.append({
            'account_id': acc.get('account_id'),
            'company': acc.get('company'),
            'mrr_usd': mrr,
            'logins_90d': logins_90d,
            'login_frequency': round(login_frequency, 3),
            'seat_utilisation': round(seat_utilisation, 3),
            'open_support_tickets': support_tickets,
            'days_since_last_login': days_since_login,
            'days_since_onboarding': days_since_onboard,
            'nps_score': nps,
        })
    return result
