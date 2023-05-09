from shared.value_objects import Currency, TaxBrackets
from tax_model.tax_model import TaxModel
from datetime import time


class Household:
    def __init__(self) -> None:
        self.incomes:list[Income] = list()

    def add_income(self, income:Currency, tax_model:TaxModel, name:str=None):
        if name == None:
            name = f"Income {len(self.incomes)+1}"

        if any(income.name == name for income in self.incomes):
            raise ValueError(f"name {name} is already taken. Please choose another name")
        else:
            add_income = Income(income=income, name=name, tax_model=tax_model)
        
        self.incomes.append(add_income)
    
    def income_after_tax(self):
        return self.incomes[0].income_after_tax()
        # return sum(income.income_after_tax() for income in self.incomes)

    def total_tax(self):
        return self.incomes[0].total_tax()


class Income:
    def __init__(self,name, income:Currency, tax_model:TaxModel, deduction:Currency=Currency(25900,"USD")):
        self.name = name
        self.tax_model = tax_model
        self.income = income
        self.deduction = deduction #TODO: Move to TaxModel

    def _calculate_tax(self, tax_brackets:tuple[TaxBrackets]):
        income_after_deduction = self.income-self.deduction
        if income_after_deduction.currency_code !=tax_brackets[0].bracket.currency_code:
            raise ValueError("Income currency code is different to tax model currency code")
    
        tax_due = Currency(0,self.income.currency_code)
        last_bracket = Currency(0, self.income.currency_code)
        for tax_bracket in tax_brackets:
            bracket = tax_bracket.bracket
            rate = tax_bracket.rate
            if income_after_deduction.amount <= bracket.amount:
                tax_due += Currency(income_after_deduction.amount - last_bracket.amount, self.income.currency_code) * rate
                break
            else:
                tax_due += Currency(bracket.amount - last_bracket.amount, self.income.currency_code) * rate
            last_bracket = tax_bracket.bracket
        return tax_due

    def total_tax(self):
        """
        Calculates federal and state taxes given an income in the form of a Currency object      
        """
        federal_tax_due = self._calculate_tax(tax_brackets=self.tax_model.federal_brackets)
        state_tax_due = self._calculate_tax(tax_brackets=self.tax_model.state_brackets)                

        return federal_tax_due, state_tax_due        
    
    def marginal_tax_rate(self):
        """
        Calculates the marginal tax rate given an income in the form of a Currency object
        """        
        federal_tax_due = self._calculate_tax(tax_brackets=self.tax_model.federal_brackets)
        state_tax_due = self._calculate_tax(tax_brackets=self.tax_model.state_brackets)                
        total_tax_due = federal_tax_due + state_tax_due
        
        return total_tax_due / self.income

    def income_after_tax(self):
        """
        Calculates the income after tax given an income in the form of a Currency object
        """

        federal_tax_due = self._calculate_tax(tax_brackets=self.tax_model.federal_brackets)        
        state_tax_due = self._calculate_tax(tax_brackets=self.tax_model.state_brackets)
        
        total_tax_due = federal_tax_due + state_tax_due
        income_after_tax = self.income - total_tax_due
        
        return income_after_tax

        
