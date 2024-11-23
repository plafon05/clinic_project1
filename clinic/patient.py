from typing import Dict, Union, List


class Patient:
    patients: List['Patient'] = []

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

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {"name": self.name, "age": self.age, "gender": self.gender, "patient_id": self.patient_id}

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int]]):
        return cls(name=data["name"], age=data["age"], gender=data["gender"], patient_id=data["patient_id"])

    @classmethod
    def get_all_patients(cls) -> List['Patient']:
        return cls.patients

    @classmethod
    def add_patient(cls, patient: 'Patient') -> None:
        cls.patients.append(patient)

    @classmethod
    def delete_patient(cls, patient: 'Patient') -> None:
        cls.patients.remove(patient)
