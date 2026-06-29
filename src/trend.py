from typing import List, Dict


def score_trend(snapshots: List[float]) -> str:
    if len(snapshots) < 2:
        return 'insufficient_data'
    delta = snapshots[-1] - snapshots[0]
    if delta >= 5:
        return 'improving'
    if delta <= -5:
        return 'declining'
    return 'stable'


def momentum(snapshots: List[float]) -> float:
    if len(snapshots) < 2:
        return 0.0
    deltas = [snapshots[i] - snapshots[i - 1] for i in range(1, len(snapshots))]
    return round(sum(deltas) / len(deltas), 2)


def at_risk_trajectory(snapshots: List[float], threshold: float = 45.0) -> bool:
    if len(snapshots) < 3:
        return False
    recent = snapshots[-3:]
    return all(recent[i] < recent[i - 1] for i in range(1, len(recent))) and snapshots[-1] < threshold


def annotate_trend(scored_accounts: List[Dict], history: Dict[str, List[float]]) -> List[Dict]:
    result = []
    for acc in scored_accounts:
        aid = acc['account_id']
        snaps = history.get(aid, [acc['health_score']])
        result.append({
            **acc,
            'trend':              score_trend(snaps),
            'momentum':           momentum(snaps),
            'at_risk_trajectory': at_risk_trajectory(snaps),
        })
    return result
