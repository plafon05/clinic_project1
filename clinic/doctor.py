from typing import Dict


class Doctor:
    def __init__(self, name: str, specialty: str):
        if not name or not isinstance(name, str):
            raise ValueError("Имя врача должно быть непустой строкой.")
        if not specialty or not isinstance(specialty, str):
            raise ValueError("Специальность врача должна быть непустой строкой.")
        self.name = name
        self.specialty = specialty

    def to_dict(self) -> Dict[str, str]:
        return {"name": self.name, "specialty": self.specialty}

    @classmethod
    def from_dict(cls, data: Dict[str, str]):
        return cls(name=data["name"], specialty=data["specialty"])