from typing import Dict, List


class Doctor:
    doctors: List['Doctor'] = []

    def __init__(self, name: str, specialty: str):
        if not name or not isinstance(name, str):
            raise ValueError("Имя врача должно быть непустой строкой.")
        if not specialty or not isinstance(specialty, str):
            raise ValueError("Специальность врача должна быть непустой строкой.")
        self.name = name
        self.specialty = specialty

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "specialty": self.specialty,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]):
        try:
            return cls(
                name=data["name"],
                specialty=data["specialty"],
            )
        except KeyError as e:
            raise ValueError(f"Отсутствует обязательное поле: {e}")

    @classmethod
    def add_doctor(cls, doctor: 'Doctor') -> None:
        cls.doctors.append(doctor)

    @classmethod
    def get_all_doctors(cls) -> List['Doctor']:
        return cls.doctors

    @classmethod
    def delete_doctor(cls, doctor: 'Doctor') -> None:
        if doctor not in cls.doctors:
            raise ValueError("Такой врач не найден в списке.")
        cls.doctors.remove(doctor)