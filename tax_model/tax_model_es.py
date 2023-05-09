from shared.value_objects import TaxBrackets
from multipledispatch import dispatch
from dataclasses import dataclass
from uuid import UUID

class TaxModelState:
    def __init__(self) -> None:
        self.id= None
        self.name= None
        self.brackets = None
        self.version= 0


class TaxModel:
    def __init__(self) -> None:
        self._domain_events = list[TaxModelEvent]
        self._state = TaxModelState()


    @dispatch
    def execute():
        pass

# Events
@dataclass
class TaxModelEvent():
    id: UUID
    tax_model_id: UUID
    timestamp: float

class TaxModelCreated(TaxModelEvent):
    pass

# Commands