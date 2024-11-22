from typing import Dict, Union
from clinic.patient import Patient


class Diagnosis:
    def __init__(self, patient: Patient, description: str, date: str):
        if not isinstance(patient, Patient):
            raise TypeError("patient должен быть экземпляром класса Patient.")
        if not description or not isinstance(description, str):
            raise ValueError("Описание диагноза должно быть непустой строкой.")
        if not date or not isinstance(date, str):
            raise ValueError("Дата должна быть непустой строкой.")
        self.patient = patient
        self.description = description
        self.date = date

    def to_dict(self) -> Dict[str, Union[str, Dict]]:
        return {
            "patient": self.patient.to_dict(),
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, Dict]]):
        patient = Patient.from_dict(data["patient"])
        return cls(patient=patient, description=data["description"], date=data["date"])