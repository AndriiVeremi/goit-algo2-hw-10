from models import Teacher

def create_schedule(subjects, teachers):
    """
    Складає розклад, використовуючи жадібний алгоритм.

    На кожному кроці вибирає викладача, який може викладати найбільшу
    кількість ще не покритих предметів. У випадку однакової кількості,
    перевага надається молодшому викладачу.
    """
    uncovered_subjects = set(subjects)
    schedule = []
    available_teachers = list(teachers)

    while uncovered_subjects:
        best_teacher = None
        max_covered_count = 0

        # Пошук найкращого викладача на поточному етапі
        for teacher in available_teachers:
            covered_by_teacher = teacher.can_teach_subjects.intersection(uncovered_subjects)
            current_covered_count = len(covered_by_teacher)

            # Критерії вибору:
            # 1. Більше покритих предметів
            # 2. Або стільки ж, але викладач молодший
            if current_covered_count > max_covered_count:
                max_covered_count = current_covered_count
                best_teacher = teacher
            elif current_covered_count == max_covered_count and best_teacher and teacher.age < best_teacher.age:
                best_teacher = teacher
        
        # Якщо не знайдено викладача, який може покрити хоча б один з решти предметів
        if best_teacher is None:
            return None  # Неможливо покрити всі предмети

        # Призначення предметів найкращому знайденому викладачу
        subjects_to_assign = best_teacher.can_teach_subjects.intersection(uncovered_subjects)
        best_teacher.assigned_subjects = subjects_to_assign
        schedule.append(best_teacher)

        # Оновлення списку непокритих предметів та доступних викладачів
        uncovered_subjects -= subjects_to_assign
        available_teachers.remove(best_teacher)

    return schedule
