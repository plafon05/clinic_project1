from clinic.patient import Patient
from clinic.doctor import Doctor
from clinic.appointment import Appointment
from clinic.diagnosis import Diagnosis
from clinic.medical_card import MedicalCard
from clinic.prescription import Prescription
from clinic.data_manager import DataManager

def main_menu():
    print("\n=== Главное меню ===")
    print("1. Управление пациентами")
    print("2. Управление врачами")
    print("3. Управление записями на прием")
    print("4. Управление диагнозами")
    print("5. Управление медицинскими картами")
    print("6. Управление рецептами")
    print("7. Сохранить данные")
    print("8. Загрузить данные")
    print("0. Выход")
    return input("Выберите действие: ")

def manage_patients():
    print("\n=== Управление пациентами ===")
    print("1. Добавить пациента")
    print("2. Просмотреть всех пациентов")
    print("3. Удалить пациента")
    choice = input("Выберите действие: ")

    if choice == "1":
        try:
            name = input("Введите имя пациента: ")
            age = int(input("Введите возраст пациента: "))
            patient = Patient(name=name, age=age)
            print("Пациент успешно добавлен.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        print("\nСписок пациентов:")
        for patient in Patient.get_all_patients():
            print(f"Имя: {patient.name}, Возраст: {patient.age}")

    elif choice == "3":
        try:
            name = input("Введите имя пациента для удаления: ")
            patient = next(p for p in Patient.get_all_patients() if p.name == name)
            Patient.delete_patient(patient)
            print("Пациент успешно удален.")
        except StopIteration:
            print("Пациент с таким именем не найден.")
        except ValueError as e:
            print(f"Ошибка: {e}")

def manage_doctors():
    print("\n=== Управление врачами ===")
    print("1. Добавить врача")
    print("2. Просмотреть всех врачей")
    choice = input("Выберите действие: ")

    if choice == "1":
        try:
            name = input("Введите имя врача: ")
            specialty = input("Введите специальность врача: ")
            doctor = Doctor(name=name, specialty=specialty)
            print("Врач успешно добавлен.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        print("\nСписок врачей:")
        for doctor in Doctor.get_all_doctors():
            print(f"Имя: {doctor.name}, Специальность: {doctor.specialty}")

def manage_appointments():
    print("\n=== Управление записями на прием ===")
    print("1. Добавить запись")
    print("2. Просмотреть все записи")
    choice = input("Выберите действие: ")

    if choice == "1":
        try:
            patient_name = input("Введите имя пациента: ")
            doctor_name = input("Введите имя врача: ")
            date = input("Введите дату приема (например, 2024-11-22): ")

            patient = next(p for p in Patient.get_all_patients() if p.name == patient_name)
            doctor = next(d for d in Doctor.get_all_doctors() if d.name == doctor_name)
            appointment = Appointment(patient=patient, doctor=doctor, date=date)
            print("Запись на прием успешно добавлена.")
        except StopIteration:
            print("Пациент или врач не найден.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        print("\nСписок записей:")
        for appointment in Appointment.get_all_appointments():
            print(f"Пациент: {appointment.patient.name}, Врач: {appointment.doctor.name}, Дата: {appointment.date}")

def manage_data():
    print("\n=== Управление данными ===")
    print("1. Сохранить данные")
    print("2. Загрузить данные")
    choice = input("Выберите действие: ")

    if choice == "1":
        try:
            DataManager.save_all_data()
            print("Данные успешно сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")
    elif choice == "2":
        try:
            DataManager.load_all_data()
            print("Данные успешно загружены.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

def main():
    while True:
        choice = main_menu()

        if choice == "1":
            manage_patients()
        elif choice == "2":
            manage_doctors()
        elif choice == "3":
            manage_appointments()
        elif choice == "7":
            manage_data()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Необработанная ошибка: {e}")