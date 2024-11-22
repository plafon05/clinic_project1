from typing import List, Dict, Union
from clinic.patient import Patient
from clinic.diagnosis import Diagnosis


class MedicalCard:
    medical_cards: List['MedicalCard'] = []
    def __init__(self, patient: Patient, card_number: str, diagnoses: List[Diagnosis] = None):
        if not isinstance(patient, Patient):
            raise TypeError("patient должен быть экземпляром класса Patient.")
        if not card_number or not isinstance(card_number, str):
            raise ValueError("Номер карты должен быть непустой строкой.")
        if diagnoses and not all(isinstance(diagnosis, Diagnosis) for diagnosis in diagnoses):
            raise TypeError("Все элементы diagnoses должны быть экземплярами класса Diagnosis.")
        self.patient = patient
        self.card_number = card_number
        self.diagnoses = diagnoses if diagnoses else []

    def to_dict(self) -> Dict[str, Union[str, List[Dict]]]:
        return {
            "patient": self.patient.to_dict(),
            "card_number": self.card_number,
            "diagnoses": [diagnosis.to_dict() for diagnosis in self.diagnoses]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, List[Dict]]]):
        patient = Patient.from_dict(data["patient"])
        diagnoses = [Diagnosis.from_dict(d) for d in data.get("diagnoses", [])]
        return cls(patient=patient, card_number=data["card_number"], diagnoses=diagnoses)

    @classmethod
    def add_medical_card(cls, card: 'MedicalCard') -> None:
        cls.medical_cards.append(card)

    @classmethod
    def get_all_medical_cards(cls) -> List['MedicalCard']:
        return cls.medical_cards

    @classmethod
    def delete_medical_card(cls, card: 'MedicalCard') -> None:
        cls.medical_cards.remove(card)