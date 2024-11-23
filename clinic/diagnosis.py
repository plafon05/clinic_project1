from typing import Dict, Union, List
from clinic.patient import Patient


class Diagnosis:
    diagnoses: List['Diagnosis'] = []

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
        """Преобразует объект в словарь."""
        return {
            "patient": self.patient.to_dict(),
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, List[Dict]]]):
        try:
            # Извлекаем данные пациента
            patient = Patient.from_dict(data["patient"])

            # Извлекаем описание и дату диагноза
            description = data["description"]
            date = data["date"]

            # Создаем объект Diagnosis
            return cls(patient=patient, description=description, date=date)

        except KeyError as e:
            raise ValueError(f"Отсутствует обязательное поле: {e}")
        except Exception as e:
            raise ValueError(f"Ошибка при создании Diagnosis: {e}")


    @classmethod
    def add_diagnosis(cls, diagnosis: 'Diagnosis') -> None:
        """Добавляет диагноз в общий список."""
        cls.diagnoses.append(diagnosis)

    @classmethod
    def get_all_diagnoses(cls) -> List['Diagnosis']:
        """Возвращает список всех диагнозов."""
        return cls.diagnoses

    @classmethod
    def delete_diagnosis(cls, diagnosis: 'Diagnosis') -> None:
        """Удаляет диагноз из общего списка."""
        if diagnosis not in cls.diagnoses:
            raise ValueError("Такой диагноз не найден в списке.")
        cls.diagnoses.remove(diagnosis)
