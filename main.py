from household.household import Household

from tax_model import tax_model as tm
from shared import value_objects as vo
from uuid import uuid4


federal_brackets = (
    tm.TaxBrackets(vo.Currency(20550, "USD"),0.1),
    tm.TaxBrackets(vo.Currency(83550,"USD"),0.12),
    tm.TaxBrackets(vo.Currency(178150,"USD"),0.22),
    tm.TaxBrackets(vo.Currency(340100,"USD"),0.24),
    tm.TaxBrackets(vo.Currency(431900,"USD"),0.32),
    tm.TaxBrackets(vo.Currency(647850,"USD"),0.35),
    tm.TaxBrackets(vo.Currency(9999999,"USD"),0.37)
)

state_brackets = (
    tm.TaxBrackets(vo.Currency(1000,"USD"),0.01),
    tm.TaxBrackets(vo.Currency(3000,"USD"),0.02),
    tm.TaxBrackets(vo.Currency(5000,"USD"),0.03),
    tm.TaxBrackets(vo.Currency(7000,"USD"),0.04),
    tm.TaxBrackets(vo.Currency(10000,"USD"),0.05),
    tm.TaxBrackets(vo.Currency(9999999,"USD"),0.0575)
)


tax_model = tm.TaxModel(
    id=uuid4(), 
    name="GA income, filing jointly", 
    federal_brackets=federal_brackets,
    state_brackets=state_brackets
    )

household = Household()

household.add_income(income=vo.Currency(200000, "USD"),tax_model=tax_model, name="Combined income")

federal, state = household.total_tax()

income_after_tax = household.income_after_tax()

print(income_after_tax)