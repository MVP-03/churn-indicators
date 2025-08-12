RISK_THRESHOLDS = {
    'low':    70.0,
    'medium': 45.0,
    'high':    0.0,
}

FEATURE_WEIGHTS = {
    'login_frequency':      0.25,
    'seat_utilisation':     0.25,
    'open_support_tickets': 0.20,
    'days_since_last_login':0.20,
    'nps_score':            0.10,
}

MAX_SUPPORT_TICKETS = 5
LOGIN_WINDOW_DAYS   = 90
RECENCY_WINDOW_DAYS = 60
