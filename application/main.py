import datetime as dt

from application.db.salary import calculate_salary
from application.people import get_employees
from application.game import Gamer

if __name__ == '__main__':
    calculate_salary()
    get_employees()

    name = input('Привет! Как тебя зовут?')
    attempt = int(input('Сколько попыток ты хочешь?'))
    range_game = 10
    gamer = Gamer(name, attempt, range_game)
    gamer.game()

    print(dt.datetime.date(dt.datetime.now()))