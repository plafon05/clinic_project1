from typing import Dict, Union, List
from clinic.patient import Patient
from clinic.doctor import Doctor


class Appointment:
    appointments: List['Appointment'] = []

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

    def __repr__(self):
        return f"Appointment(date={self.date}, doctor={self.doctor}, patient={self.patient})"

    def to_dict(self) -> Dict[str, Union[str, Dict]]:
        return {
            "patient": self.patient.to_dict(),
            "doctor": self.doctor.to_dict(),
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, Dict]]):
        try:
            patient = Patient.from_dict(data["patient"])
            if isinstance(data.get("doctor"), dict):
                doctor = Doctor.from_dict(data["doctor"])
            elif "doctor_id" in data:
                # Получить объект Doctor по ID, если он доступен
                doctor = next((doc for doc in Doctor.get_all_doctors() if doc.doctor_id == data["doctor_id"]), None)
                if not doctor:
                    raise ValueError(f"Доктор с ID {data['doctor_id']} не найден.")
            else:
                raise ValueError("Отсутствует обязательное поле: 'doctor' или 'doctor_id'")

            date = data["date"]
            if not isinstance(date, str):
                raise ValueError("Поле 'date' должно быть строкой.")
            return cls(patient=patient, doctor=doctor, date=date)
        except KeyError as e:
            raise ValueError(f"Отсутствует обязательное поле: {e}")
        except Exception as e:
            raise ValueError(f"Ошибка при создании Appointment: {e}")

    @classmethod
    def add_appointment(cls, appointment: 'Appointment') -> None:
        cls.appointments.append(appointment)

    @classmethod
    def get_all_appointments(cls) -> List['Appointment']:
        return cls.appointments

    @classmethod
    def delete_appointment(cls, appointment: 'Appointment') -> None:
        cls.appointments.remove(appointment)