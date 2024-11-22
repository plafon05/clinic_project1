from typing import Dict
from clinic.patient import Patient


class Prescription:
    def __init__(self, patient: Patient, medication: str, dosage: str, duration: str):
        if not isinstance(patient, Patient):
            raise TypeError("patient должен быть экземпляром класса Patient.")
        if not medication or not isinstance(medication, str):
            raise ValueError("Название лекарства должно быть непустой строкой.")
        if not dosage or not isinstance(dosage, str):
            raise ValueError("Дозировка должна быть непустой строкой.")
        if not duration or not isinstance(duration, str):
            raise ValueError("Продолжительность должна быть непустой строкой.")
        self.patient = patient
        self.medication = medication
        self.dosage = dosage
        self.duration = duration

    def to_dict(self) -> Dict[str, str]:
        return {
            "patient": self.patient.to_dict(),
            "medication": self.medication,
            "dosage": self.dosage,
            "duration": self.duration
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]):
        patient = Patient.from_dict(data["patient"])
        return cls(patient=patient, medication=data["medication"], dosage=data["dosage"], duration=data["duration"])