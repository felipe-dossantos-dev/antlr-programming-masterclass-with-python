from typing import Any
from pydantic import BaseModel

NOTES = {
    "C8": 51,
    "B7": 50,
    "A7": 49,
    "G7": 48,
    "F7": 47,
    "E7": 46,
    "D7": 45,
    "C7": 44,
    "B6": 43,
    "A6": 42,
    "G6": 41,
    "F6": 40,
    "E6": 39,
    "D6": 38,
    "C6": 37,
    "B5": 36,
    "A5": 35,
    "G5": 34,
    "F5": 33,
    "E5": 32,
    "D5": 31,
    "C5": 30,
    "B4": 29,
    "A4": 28,
    "G4": 27,
    "F4": 26,
    "E4": 25,
    "D4": 24,
    "C4": 23,
    "B3": 22,
    "A3": 21,
    "G3": 20,
    "F3": 19,
    "E3": 18,
    "D3": 17,
    "C3": 16,
    "B2": 15,
    "A2": 14,
    "G2": 13,
    "F2": 12,
    "E2": 11,
    "D2": 10,
    "C2": 9,
    "B1": 8,
    "A1": 7,
    "G1": 6,
    "F1": 5,
    "E1": 4,
    "D1": 3,
    "C1": 2,
    "B0": 1,
    "A0": 0,
}

class BazilioException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ProcedureDefinition(BaseModel):
    name: str
    args: list[str]
    instructions: Any