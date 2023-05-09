from shared.value_objects import TaxBrackets
from uuid import UUID


class TaxModel:
    def __init__(self, id:UUID, name:str, federal_brackets:tuple[TaxBrackets], state_brackets:tuple[TaxBrackets]=None) -> None:
        self.id= id
        self.name= name
        self.federal_brackets= federal_brackets
        self.state_brackets = state_brackets

