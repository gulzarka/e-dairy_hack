import random


from datacenter.models import (
    Schoolkid, Mark, Chastisement, Commendation, Lesson
                               )


def find_schoolkid(child_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=child_name)
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько учеников. Укажите полное ФИО')
        return None
    except Schoolkid.DoesNotExist:
        print(f'Ученик "{child_name}" не найден')
        return None


def fix_marks(child_name):
    schoolkid = find_schoolkid(child_name)
    if schoolkid:
        Mark.objects.filter(
                schoolkid=schoolkid,
                points__lt=4
        ).update(points=5)
        print('Все двойки и тройки этого ученика заменены на пятерки!')


def remove_chastisements(child_name):
    schoolkid = find_schoolkid(child_name)
    if schoolkid:
        schoolkid_chastiments = Chastisement.objects.filter(
                schoolkid=schoolkid
        )
        schoolkid_chastiments.delete()
        print('Все замечания этого ученика удалены!')


def create_commendation(child_name, subject_title):
    schoolkid = find_schoolkid(child_name)
    if schoolkid:
        try:
            lesson = random.choice(Lesson.objects.filter(
                                        subject__title=subject_title,
                                        year_of_study=schoolkid.year_of_study,
                                        group_letter=schoolkid.group_letter
                                        ))
            commendation_text = ['Так держать!', 'Уже лучше!', 'Замечательно!', 'Талантливо!']  
            Commendation.objects.create(
                text=random.choice(commendation_text),
                created=lesson.date, schoolkid=schoolkid,
                subject=lesson.subject, teacher=lesson.teacher
                )
            print('Добавлена новая запись!')
        except Lesson.DoesNotExist:
            print('Урок не найден, введите верное название предмета')
