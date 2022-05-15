import pytest


@pytest.fixture()
def zeros():
    return [0, 0, 0]


def test_example(zeros):
    zeros.append(0)
    assert len(zeros) == 4
