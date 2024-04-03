import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount_of_cents,expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters")
    ]
)
def test_smallest_possible_number_of_coins(amount_of_cents: int,
                                           expected_result: list) -> None:
    assert get_coin_combination(amount_of_cents) == expected_result
