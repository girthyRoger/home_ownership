from shared.value_objects import Currency

class TaxModel:
    def __init__(self, federal_brackets, federal_rates, state_brackets=None, state_rates=None):
        self.federal_brackets:list[Currency] = federal_brackets
        self.federal_rates:list = federal_rates
        self.state_brackets:list[Currency] = state_brackets
        self.state_rates:list = state_rates



