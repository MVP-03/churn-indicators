from typing import Dict, List


REQUIRED_ACCOUNT_FIELDS = ('account_id', 'company', 'mrr_usd', 'logins_last_90d',
                            'seats_used', 'seats_total', 'open_support_tickets',
                            'days_since_last_login', 'nps_score')


def validate_account_row(row: Dict) -> List[str]:
    errors = []
    for field in REQUIRED_ACCOUNT_FIELDS:
        if field not in row:
            errors.append(f'missing field: {field}')
    mrr = row.get('mrr_usd', 0)
    try:
        if float(mrr) < 0:
            errors.append('mrr_usd must be >= 0')
    except (TypeError, ValueError):
        errors.append('mrr_usd must be numeric')
    return errors


def validate_all(accounts: List[Dict]) -> Dict[str, List[str]]:
    return {
        str(acc.get('account_id', i)): validate_account_row(acc)
        for i, acc in enumerate(accounts)
    }
