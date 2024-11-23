from typing import Dict, List, Union
from clinic.patient import Patient

class Recipe:
    """Класс, представляющий рецепт пациента."""

    recipes_db: List['Recipe'] = []  # База данных рецептов

    def __init__(self, patient: Patient, medication: str, dosage: str, duration: str):
        """
        Инициализация рецепта.
        :param patient: Пациент, которому выдан рецепт.
        :param medication: Лекарство, которое прописано.
        :param dosage: Дозировка лекарства.
        :param duration: Продолжительность лечения.
        """
        if not isinstance(patient, Patient):
            raise TypeError("patient должен быть экземпляром класса Patient.")
        if not medication or not isinstance(medication, str):
            raise ValueError("Медикамент должен быть строкой.")
        if not dosage or not isinstance(dosage, str):
            raise ValueError("Дозировка должна быть строкой.")
        if not duration or not isinstance(duration, str):
            raise ValueError("Продолжительность должна быть строкой.")

        self.patient = patient
        self.medication = medication
        self.dosage = dosage
        self.duration = duration

        Recipe.recipes_db.append(self)

    def to_dict(self) -> Dict[str, Union[Dict, str]]:
        """Преобразует объект рецепта в словарь."""
        return {
            "patient": self.patient.to_dict(),
            "medication": self.medication,
            "dosage": self.dosage,
            "duration": self.duration
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[Dict, str]]) -> 'Recipe':
        """Создает объект Recipe из словаря."""
        try:
            patient = Patient.from_dict(data["patient"])
            medication = data["medication"]
            dosage = data["dosage"]
            duration = data["duration"]
            return cls(patient=patient, medication=medication, dosage=dosage, duration=duration)
        except KeyError as e:
            raise ValueError(f"Ошибка в Recipe.from_dict: Отсутствует обязательное поле {e}.")
        except Exception as e:
            raise ValueError(f"Ошибка в Recipe.from_dict: {e}")

    @staticmethod
    def get_all_recipes() -> List['Recipe']:
        """Возвращает список всех рецептов."""
        return Recipe.recipes_db

    @staticmethod
    def delete_recipe(recipe: 'Recipe') -> None:
        """Удаляет рецепт из базы данных."""
        if recipe in Recipe.recipes_db:
            Recipe.recipes_db.remove(recipe)
        else:
            raise ValueError("Рецепт не найден.")