from typing import Dict, Union


class Patient:
    def __init__(self, name: str, age: int):
        if not name or not isinstance(name, str):
            raise ValueError("Имя пациента должно быть непустой строкой.")
        if age <= 0 or not isinstance(age, int):
            raise ValueError("Возраст пациента должен быть положительным целым числом.")
        self.name = name
        self.age = age

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {"name": self.name, "age": self.age}

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int]]):
        return cls(name=data["name"], age=data["age"])