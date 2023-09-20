import random2
from progress.bar import Bar

class Gamer:
    def __init__(self, name, attempt, range_game):
        self.name = name
        self.attempt = attempt
        self.range_game = range_game
    def game(self):
        number = random2.randint(1, self.range_game)
        bar = Bar('Attampts\n', max=self.attempt)
        for _ in range(self.attempt):
            bar.next()
            guess = int(input('\nВведи число: '))

            if guess < number:
                print('Твое число меньше того, что я загадал.')

            elif guess > number:
                print('Твое число больше загаданного мной.')

            elif guess == number:
                break
            bar.finish()

        if guess == number:
            print(f'Ух ты, {self.name}! Ты угадал мое число!')
        else:
            print(f'А вот и не угадал! Я загадал число {number}')