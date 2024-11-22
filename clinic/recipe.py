class Recipe:
    """Класс, представляющий рецепт пациента."""

    recipes_db = []  # База данных рецептов

    def __init__(self, patient, medication: str, dosage: str, duration: str):
        """Инициализация рецепта.

        :param patient: Пациент, которому выдан рецепт.
        :param medication: Лекарство, которое прописано.
        :param dosage: Дозировка лекарства.
        :param duration: Продолжительность лечения.
        """
        self.patient = patient
        self.medication = medication
        self.dosage = dosage
        self.duration = duration
        Recipe.recipes_db.append(self)

    @staticmethod
    def get_all_recipes():
        """Возвращает список всех рецептов."""
        return Recipe.recipes_db

    @staticmethod
    def delete_recipe(recipe):
        """Удаляет рецепт из базы данных."""
        if recipe in Recipe.recipes_db:
            Recipe.recipes_db.remove(recipe)
        else:
            raise ValueError("Рецепт не найден.")