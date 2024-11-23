import json
from typing import List, Dict
from clinic.patient import Patient
from clinic.doctor import Doctor
from clinic.appointment import Appointment
from clinic.diagnosis import Diagnosis
from clinic.medical_card import MedicalCard
from clinic.prescription import Prescription
from clinic.recipe import Recipe


class DataManager:

    @staticmethod
    def save_to_json(filename: str, data: dict) -> None:
        """Сохранение всех данных в один файл в формате JSON."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Данные успешно сохранены в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении в JSON: {e}")

    @staticmethod
    def load_from_json(filename: str) -> dict:
        """Загрузка всех данных из одного файла JSON."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(f"Данные успешно загружены из {filename}")
            return data
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Загруженные данные будут пустыми.")
            return {}
        except Exception as e:
            print(f"Ошибка при загрузке из JSON: {e}")
            return {}

    @staticmethod
    def save_all_data(filename: str = "clinic_data.json") -> None:
        """Сохранение всех данных в один JSON-файл."""
        data = {
            "patients": [patient.to_dict() for patient in Patient.patients_db],
            "appointments": [appointment.to_dict() for appointment in Appointment.appointments_db],
            "diagnoses": [diagnosis.to_dict() for diagnosis in Diagnosis.diagnoses_db],
            "medical_cards": [medical_card.to_dict() for medical_card in MedicalCard.medical_cards_db],
            "recipes": [recipe.to_dict() for recipe in Recipe.recipes_db]
        }
        DataManager.save_to_json(filename, data)

    @staticmethod
    def load_all_data(filename: str = "clinic_data.json") -> None:
        """Загрузка всех данных из одного JSON-файла."""
        data = DataManager.load_from_json(filename)
        if not data:
            print("Нет данных для загрузки.")
            return

        try:
            # Загрузка данных в базы соответствующих классов
            if "patients" in data:
                Patient.patients_db = [Patient.from_dict(patient) for patient in data["patients"]]
                print(f"Пациенты после загрузки: {Patient.patients_db}")

            if "appointments" in data:
                Appointment.appointments_db = [Appointment.from_dict(appointment) for appointment in data["appointments"]]

            if "diagnoses" in data:
                Diagnosis.diagnoses_db = [Diagnosis.from_dict(diagnosis) for diagnosis in data["diagnoses"]]

            if "medical_cards" in data:
                MedicalCard.medical_cards_db = [MedicalCard.from_dict(medical_card) for medical_card in data["medical_cards"]]

            if "recipes" in data:
                Recipe.recipes_db = [Recipe.from_dict(recipe) for recipe in data["recipes"]]

            print(f"Все данные успешно загружены из файла {filename}.")
        except Exception as e:
            print(f"Ошибка при обработке данных из файла {filename}: {e}")