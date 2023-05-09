class TaxBrackets:
    def __init__(self, bracket, rate) -> None:
        self.bracket: Currency = bracket
        self.rate: float = rate

    def rate_percent(self):
        return self.rate * 100

class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    def __repr__(self):
        return f"{self.amount} {self.currency_code}"

    def __add__(self, other):
        if self.currency_code != other.currency_code:
            raise ValueError("Cannot add currencies with different currency codes")
        return Currency(self.amount + other.amount, self.currency_code)

    def __sub__(self, other):
        if self.currency_code != other.currency_code:
            raise ValueError("Cannot subtract currencies with different currency codes")
        return Currency(self.amount - other.amount, self.currency_code)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Currency(self.amount * other, self.currency_code)
        raise TypeError(f"Cannot multiply Currency by {type(other)}")

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    def __ne__(self, other):
        return not self.__eq__(other)
    