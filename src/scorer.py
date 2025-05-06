from typing import List, Dict


def _clamp(val: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, val))


def _linear(val: float, low: float, high: float) -> float:
    if high <= low:
        return 0.0
    return _clamp((val - low) / (high - low))


def score_account(features: Dict) -> Dict:
    login_score    = _linear(features['login_frequency'], 0.0, 0.5)
    seat_score     = features['seat_utilisation']
    ticket_score   = _clamp(1.0 - features['open_support_tickets'] / 5.0)
    recency_score  = _clamp(1.0 - features['days_since_last_login'] / 60.0)
    nps_score      = _linear(features['nps_score'], 0, 10)

    health = (
        login_score   * 0.25 +
        seat_score    * 0.25 +
        ticket_score  * 0.20 +
        recency_score * 0.20 +
        nps_score     * 0.10
    )
    health_pct = round(health * 100, 1)

    if health_pct >= 70:
        risk = 'low'
    elif health_pct >= 45:
        risk = 'medium'
    else:
        risk = 'high'

    return {
        **features,
        'health_score': health_pct,
        'churn_risk': risk,
    }


def score_all(accounts: List[Dict]) -> List[Dict]:
    scored = [score_account(a) for a in accounts]
    return sorted(scored, key=lambda x: x['health_score'])
