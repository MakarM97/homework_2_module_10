from threading import Thread
from collections import defaultdict
import time

# class Knight(Thread):
#     def __init__(self, name, skill, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.skill = skill
#         self.fight = defaultdict(int)
#
#     def run(self):
#         enemy = 100
#         self. fight = enemy - self.skill
#         sleep = self.skill
#         for fight in range(enemy):
#             print(f'Sir {self.name} сражается 1 день, врагов осталось - {enemy} ')
#             time.sleep(sleep)
#         if self.fight != 0:
#             print(f'Sir {self.name} сражается 1 день, врагов осталось - {enemy} ')
#         else:
#             print(f' Sir {self.name} одержал победу спустя дней')
#
#
# knight1 = Knight('Sir Galahad', 20)
# knight2 = Knight('Sir Lancelot', 10)
#
# print('Sir Galahad, на нас напали!')
# print('Sir Lancelot, на нас напали!')
#
# knight1.start()
# knight2.start()
#
# knight1.join()
# knight2.join()
#
# print('Все битвы закончились!')


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        days = 0
        enemies = 100
        while enemies > 0:
            days += 1
            enemies -= self.skill
            print("{} защищал королевство {} день. Осталось {} врагов".format(self.name, days, enemies))
            time.sleep(1)


knight1 = Knight("Sir Galahad", 20)
knight2 = Knight("Sir Lancelot", 10)

print('Sir Galahad, на нас напали!')
print('Sir Lancelot, на нас напали!')

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Защита королевства завершена")