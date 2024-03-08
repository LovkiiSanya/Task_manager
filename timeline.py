import datetime


def user_set_deadline():
    year = int(input("Укажите год нашего дедлайна: "))
    month = int(input("Укажите месяц: "))
    day = int(input("Число: "))
    hour = int(input("Час(24 часовой формат): "))
    minute = int(input("Минуту: "))
    if datetime.datetime(
        year, month, day, hour, minute
    ) - datetime.datetime.now() > datetime.timedelta(0):
        return datetime.datetime(year, month, day, hour, minute).strftime(
            "%m/%d/%Y, %H:%M:%S"
        )
    else:
        print("Ошибка,вместо дедлайена установлена текущая дата")
        return datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
