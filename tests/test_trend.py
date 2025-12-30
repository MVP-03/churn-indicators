import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from trend import score_trend, momentum, at_risk_trajectory, annotate_trend


def test_improving():
    assert score_trend([40.0, 45.0, 52.0]) == 'improving'


def test_declining():
    assert score_trend([70.0, 60.0, 50.0]) == 'declining'


def test_stable():
    assert score_trend([55.0, 57.0, 56.0]) == 'stable'


def test_insufficient():
    assert score_trend([60.0]) == 'insufficient_data'


def test_momentum_positive():
    assert momentum([50.0, 55.0, 60.0]) > 0


def test_at_risk_trajectory_true():
    assert at_risk_trajectory([60.0, 50.0, 40.0, 30.0]) is True


def test_at_risk_trajectory_false():
    assert at_risk_trajectory([60.0, 70.0, 80.0]) is False


def test_annotate_trend():
    acc = [{'account_id': 'a1', 'health_score': 60.0, 'churn_risk': 'medium'}]
    history = {'a1': [50.0, 55.0, 60.0]}
    result = annotate_trend(acc, history)
    assert result[0]['trend'] == 'improving'
    assert result[0]['momentum'] > 0
