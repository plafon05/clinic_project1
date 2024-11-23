from typing import Dict, Union, List


class Patient:
    # Инициализация атрибута на уровне класса
    patients_db: List['Patient'] = []

    def __init__(self, name: str, age: int, gender: str, patient_id: int):
        if not name or not isinstance(name, str):
            raise ValueError("Имя пациента должно быть непустой строкой.")
        if age <= 0 or not isinstance(age, int):
            raise ValueError("Возраст пациента должен быть положительным целым числом.")
        if not gender or not isinstance(gender, str):
            raise ValueError("Пол пациента должен быть непустой строкой.")
        if patient_id <= 0 or not isinstance(patient_id, int):
            raise ValueError("ID пациента должен быть положительным целым числом.")
        self.name = name
        self.age = age
        self.gender = gender
        self.patient_id = patient_id

    def __repr__(self):
        return f"Patient(name={self.name}, age={self.age}, gender={self.gender}, patient_id={self.patient_id})"

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int]]) -> 'Patient':
        """Создает объект Patient из словаря."""
        try:
            return cls(
                name=data["name"],
                age=data["age"],
                gender=data["gender"],
                patient_id=data["patient_id"]
            )
        except KeyError as e:
            print(f"Ошибка: отсутствует обязательное поле {e} в данных {data}")
            raise

    def to_dict(self) -> Dict[str, Union[str, int]]:
        """Преобразует объект Patient в словарь."""
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "patient_id": self.patient_id
        }

    @classmethod
    def get_all_patients(cls) -> List['Patient']:
        """Возвращает список всех пациентов."""
        return cls.patients_db

    @classmethod
    def add_patient(cls, patient: 'Patient') -> None:
        """Добавляет пациента в базу данных."""
        cls.patients_db.append(patient)

    @classmethod
    def delete_patient(cls, patient: 'Patient') -> None:
        """Удаляет пациента из базы данных."""
        cls.patients_db.remove(patient)