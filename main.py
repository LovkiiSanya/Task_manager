import schedule
import datetime

task_dict = {}


class Task:
    def __init__(self, name, deadline, type, status):
        self.name = name
        self.deadline = deadline
        self.type = type
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
            "Привет,выбери категорию заданий :(Бытовые дела = 1),(Тренировка = 2),(Домашняя работа = 3)"
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
        schedule.every(60).seconds.do(
            Task.checkdeadline, over=Task.taskdeadline(), now=datetime.datetime.now()
        )

    def status_check():
        if Task.checkdeadline() == "Увы,время вышло!":
            print("mission failed")
        else:
            print("Время есть, хилимся живём")


class cleaning(Task):
    def __init__(self, name, deadline, item, status):
        super().__init__(name, deadline, status)
        self.item = item

    def kindofitem():
        item = input("Какой предмет или комнату будем приводить в порядок?")
        return item


class training(Task):
    def __init__(self, name, deadline, muscle, status):
        super().__init__(name, deadline, status)
        self.muscle = muscle

    def kindofmuscle():
        muscle = input("Какую группу мышц прорабатываем?: ")
        return muscle


class student(Task):
    def __init__(self, name, deadline, homework, status):
        super().__init__(name, deadline, status)
        self.homework = homework

    def kindofhomework():
        homework = input("Какие уроки надо сделать?:")
        return homework


while True:

    task_name = Task.taskname()
    print("Отлично, пусть будет", task_name)
    dead_line = Task.taskdeadline()
    print("Задание ", task_name, "записано на", dead_line)
    task_type = Task.tasktype()
    if task_type == 1:
        cleaning.kindofitem()
        Task.status_check()
