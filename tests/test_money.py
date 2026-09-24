from decimal import Decimal

import pytest

from foundations.money import InvalidMoneyError, Money


def test_money_rounds_to_two_decimal_places() -> None:
    assert Money.from_text("12.345").amount == Decimal("12.35")


def test_money_addition_requires_matching_currency() -> None:
    with pytest.raises(InvalidMoneyError):
        Money.from_text("1", "USD").add(Money.from_text("1", "EUR"))


def test_negative_amount_is_rejected() -> None:
    with pytest.raises(InvalidMoneyError):
        Money.from_text("-1")
