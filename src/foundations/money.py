from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal


class InvalidMoneyError(ValueError):
    """Raised when a monetary value is invalid."""


@dataclass(frozen=True, slots=True)
class Money:
    amount: Decimal
    currency: str = "USD"

    def __post_init__(self) -> None:
        if not self.currency or len(self.currency) != 3 or not self.currency.isupper():
            raise InvalidMoneyError("currency must be a three-letter uppercase code")
        if self.amount < 0:
            raise InvalidMoneyError("amount cannot be negative")

    @classmethod
    def from_text(cls, value: str, currency: str = "USD") -> Money:
        try:
            amount = Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        except Exception as exc:
            raise InvalidMoneyError("amount must be a valid decimal") from exc
        return cls(amount, currency)

    def add(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise InvalidMoneyError("currencies must match")
        return Money(self.amount + other.amount, self.currency)

    def format(self) -> str:
        return f"{self.currency} {self.amount:.2f}"
