from typing import List, Dict, Union
from clinic.patient import Patient
from clinic.diagnosis import Diagnosis


class MedicalCard:
    medical_cards: List['MedicalCard'] = []

    def __init__(self, patient: Patient, card_number: str):
        if not isinstance(patient, Patient):
            raise TypeError("patient должен быть экземпляром класса Patient.")
        if not card_number or not isinstance(card_number, str):
            raise ValueError("Номер карты должен быть непустой строкой.")

        self.patient = patient
        self.card_number = card_number

    from typing import List, Dict, Union
    from clinic.patient import Patient
    from clinic.diagnosis import Diagnosis

    class MedicalCard:
        medical_cards: List['MedicalCard'] = []

        def __init__(self, patient: Patient, card_number: str):
            if not isinstance(patient, Patient):
                raise TypeError("patient должен быть экземпляром класса Patient.")
            if not card_number or not isinstance(card_number, str):
                raise ValueError("Номер карты должен быть непустой строкой.")

            self.patient = patient
            self.card_number = card_number

        def to_dict(self) -> Dict[str, Union[str]]:
            return {
                "patient": self.patient.to_dict(),
                "card_number": self.card_number,
            }

        @classmethod
        def from_dict(cls, data: Dict[str, Union[str]]):
            try:
                # Логируем только данные пациента и номер карты
                print(f"Загруженные данные для MedicalCard: {data}")

                # Создаем объект пациента
                patient = Patient.from_dict(data["patient"])

                # Возвращаем объект без диагнозов
                return cls(patient=patient, card_number=data["card_number"])

            except Exception as e:
                print(f"Ошибка при создании MedicalCard: {e}")
                raise ValueError(f"Ошибка в MedicalCard.from_dict: {e}. Данные: {data}")

        @classmethod
        def add_medical_card(cls, card: 'MedicalCard') -> None:
            cls.medical_cards.append(card)

        @classmethod
        def get_all_medical_cards(cls) -> List['MedicalCard']:
            return cls.medical_cards

        @classmethod
        def delete_medical_card(cls, card: 'MedicalCard') -> None:
            cls.medical_cards.remove(card)
    def to_dict(self) -> Dict[str, Union[str]]:
        return {
            "patient": self.patient.to_dict(),
            "card_number": self.card_number,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str]]):
        try:
            # Логируем только данные пациента и номер карты
            print(f"Загруженные данные для MedicalCard: {data}")

            # Создаем объект пациента
            patient = Patient.from_dict(data["patient"])

            # Возвращаем объект без диагнозов
            return cls(patient=patient, card_number=data["card_number"])

        except Exception as e:
            print(f"Ошибка при создании MedicalCard: {e}")
            raise ValueError(f"Ошибка в MedicalCard.from_dict: {e}. Данные: {data}")

    @classmethod
    def add_medical_card(cls, card: 'MedicalCard') -> None:
        cls.medical_cards.append(card)

    @classmethod
    def get_all_medical_cards(cls) -> List['MedicalCard']:
        return cls.medical_cards

    @classmethod
    def delete_medical_card(cls, card: 'MedicalCard') -> None:
        cls.medical_cards.remove(card)