from dataclasses import dataclass
@dataclass(frozen=True)
class Locator:
    by:str
    value:str
