from typing import Dict, Union
from clinic.patient import Patient
from clinic.doctor import Doctor


class Appointment:
    def __init__(self, patient: Patient, doctor: Doctor, date: str):
        if not isinstance(patient, Patient):
            raise TypeError("patient должен быть экземпляром класса Patient.")
        if not isinstance(doctor, Doctor):
            raise TypeError("doctor должен быть экземпляром класса Doctor.")
        if not date or not isinstance(date, str):
            raise ValueError("Дата должна быть непустой строкой.")
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def to_dict(self) -> Dict[str, Union[str, Dict]]:
        return {
            "patient": self.patient.to_dict(),
            "doctor": self.doctor.to_dict(),
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, Dict]]):
        patient = Patient.from_dict(data["patient"])
        doctor = Doctor.from_dict(data["doctor"])
        return cls(patient=patient, doctor=doctor, date=data["date"])