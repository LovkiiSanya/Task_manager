import schedule
import datetime
import random
import time

task_dict = {}


def rndnumb():
    numb = random.randint(1, 1000000)
    return numb


class Task:
    def __init__(self, name, deadline, status):
        self.name = name
        self.deadline = deadline

        self.status = status

    def taskname():
        name = input("Давайте сразу дадим название нашему заданию: ")
        return name

    def taskdeadline():
        year = int(input("Укажите год нашего дедлайна: "))
        month = int(input("Укажите месяц: "))
        day = int(input("Число: "))
        hour = int(input("Час(24 часовой формат): "))
        minute = int(input("Минуту: "))
        return datetime.datetime(year, month, day, hour, minute)

    def tasktype():
        print(
            "Выбери категорию заданий :(Бытовые дела = 1),(Тренировка = 2),(Домашняя работа = 3)"
        )
        type = int(input())
        if 1 <= type <= 3:
            return type
        else:
            print("Что-то пошло не так, давайте еще разок")

    def checkdeadline():
        over = Task.taskdeadline()
        now = datetime.datetime.now()
        if over - now <= datetime.timedelta(seconds=0):
            return print("Увы,время вышло!")
        else:
            return print("Осталось ", (over - now))

    def schedule_init():
        fu = "Задача просрочена, фу"
        keys = [key for key in task_dict if task_dict[key] == fu]
        print(keys)

    def status_check():
        if Task.checkdeadline() == "Увы,время вышло!":
            print("mission failed")
        else:
            print("Время есть, хилимся живём")


class cleaning(Task):
    def __init__(self, name, deadline, item, status):
        super().__init__(name, deadline, status)
        self.item = item

    def task_info():
        task_id = rndnumb()
        item_cleaning = cleaning.kindofitem()
        task_deadline = Task.taskdeadline()
        if task_deadline - datetime.datetime.now() <= datetime.timedelta(seconds=0):
            cleaning_status = "Задача просрочена, фу"
        else:
            cleaning_status = "Задача активна, поднажмём"

        task_cleaning = cleaning(
            task_name,
            task_deadline.strftime("%Y-%m-%d-%H.%M.%S"),
            item_cleaning,
            cleaning_status,
        )
        task_dict[task_id] = task_cleaning
        print(task_dict)

    def kindofitem():
        item = input("Какой предмет или комнату будем приводить в порядок?")
        return item

    def __repr__(self):
        cleaning = type(self).__name__
        return (
            f"{cleaning}({self.name!r},{self.deadline!r},{self.item!r},{self.status!r})"
        )

    def __str__(self):
        return f"Задание: {self.name} Срок годности: {self.deadline} Комната/предмет: {self.item} Статус: {self.status}"


class training(Task):
    def __init__(self, name, deadline, muscle, status):
        super().__init__(name, deadline, status)
        self.muscle = muscle

    def task_info():
        task_id = rndnumb()
        muscle_training = training.kindofmuscle()
        task_deadline = Task.taskdeadline()
        if task_deadline - datetime.datetime.now() <= datetime.timedelta(seconds=0):
            cleaning_status = "Задача просрочена, фу"
        else:
            cleaning_status = "Задача активна, поднажмём"
        task_training = training(
            task_name,
            task_deadline.strftime("%Y-%m-%d-%H.%M.%S"),
            muscle_training,
            cleaning_status,
        )
        task_dict[task_id] = task_training
        print(task_dict)

    def kindofmuscle():
        muscle = input("Какую группу мышц прорабатываем?: ")
        return muscle

    def __repr__(self):
        training = type(self).__name__
        return f"{training}({self.name!r},{self.deadline!r},{self.muscle!r},{self.status!r})"

    def __str__(self):
        return f"Задание: {self.name} Срок годности: {self.deadline} Мышца: {self.muscle} Статус: {self.status}"


class student(Task):
    def __init__(self, name, deadline, homework, status):
        super().__init__(name, deadline, status)
        self.homework = homework

    def task_info():
        task_id = rndnumb()
        homework_task = student.kindofhomework()
        task_deadline = Task.taskdeadline()
        if task_deadline - datetime.datetime.now() <= datetime.timedelta(seconds=0):
            cleaning_status = "Задача просрочена, фу"
        else:
            cleaning_status = "Задача активна, поднажмём"
        student_task = student(
            task_name,
            task_deadline.strftime("%Y-%m-%d-%H.%M.%S"),
            homework_task,
            cleaning_status,
        )
        task_dict[task_id] = student_task
        print(task_dict)

    def kindofhomework():
        homework = input("Какие уроки надо сделать?:")
        return homework

    def __repr__(self):
        student = type(self).__name__
        return f"{student}({self.name!r},{self.deadline!r},{self.homework!r},{self.status!r})"

    def __str__(self):
        return f"Задание: {self.name} Срок годности: {self.deadline} Комната/предмет: {self.homework} Статус: {self.status}"


while True:

    task_name = Task.taskname()
    print("Отлично, пусть будет", task_name)
    task_type = Task.tasktype()
    if task_type == 1:
        cleaning.task_info()
    if task_type == 2:
        training.task_info()
    if task_type == 3:
        student.task_info()

    CRUDoperation = int(
        input(
            "Если хотите просмотреть имеющиеся задачи нажмите(1), чтобы удалить(2), или изменить(3),запустить авто-проверку заданий (0)"
        )
    )
    if CRUDoperation == 1:
        check_tusk = int(input("хотите посмотреть все задачи?(1),по конкретному ID(2)"))
        if check_tusk == 1:
            print(task_dict)
        if check_tusk == 2:
            check_tusk_id = int(input("Введите ваш ID:"))
            if check_tusk_id in task_dict:
                print(task_dict.get(check_tusk_id))
            else:
                print("Такого ID в базе нет!")
    if CRUDoperation == 2:
        del_tusk = int(input("Введите ID задания которое надо удалить: "))
        task_dict.pop(del_tusk)
        print("Удалено!БимБим БомБом")

    if CRUDoperation == 3:
        change_task = int(input("По какому ID меняем задание?: "))
        if type(task_dict[change_task]) == cleaning:
            task_name = Task.taskname()
            print("Отлично, пусть будет", task_name)
            task_type = Task.tasktype()
            cleaning.task_info()
        if type(task_dict[change_task]) == training:
            task_name = Task.taskname()
            print("Отлично, пусть будет", task_name)
            task_type = Task.tasktype()
            training.task_info()
        if type(task_dict[change_task]) == student:
            task_name = Task.taskname()
            print("Отлично, пусть будет", task_name)
            task_type = Task.tasktype()
            student.task_info()
    if CRUDoperation == 0:
        schedule.every(5).seconds.do(Task.schedule_init)
        while True:
            schedule.run_pending()
            time.sleep(1)
