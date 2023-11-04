import pytest


def inc(x):
    return x+1


def test_answer():
    assert inc(5) == 6
    assert inc(5) == 6


def test_answer2():
    assert inc(5) != 8
    assert inc(5) == 6


def raiser():
    raise SystemExit


def test_raiser():
    pytest.raises(SystemExit)

