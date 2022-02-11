import time
import logging
import threading, time
from random import randint
from functools import wraps
import os

FORMAT = '(%(user)s)Running: %(message)s'
logging.basicConfig(filename='machine.log',
                    filemode='a',
                    format=FORMAT,
                    datefmt='%H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger('machine')

def log(fn):
    @wraps(fn)
    def time_func(*args, **kwargs):
        d = {'user': os.environ["USER"]}

        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        start_time = time.time()
        runtime = '0.000 ms'
        elapsed_time = start_time - start_time
        t.start()
        while t.is_alive():
            elapsed_time = (time.time() - start_time)
        if elapsed_time:
            m, s = divmod(elapsed_time, 60)
            ms = s * 1000
            if ms < 10:
                runtime = "{0:3.2} ms".format(ms)
            else:
                runtime = "{0:3.2} s".format(s)

        fn_name = fn.__name__.split('_')
        capital = lambda word: str.capitalize(word)
        fn_name = list(map(capital, fn_name))
        fn_name = ' '.join(fn_name)
        msg = f'{fn_name:<19}'
        msg += '[ exec-time = {runtime} ]'.format(runtime=runtime)
        logger.info(msg, extra=d)
        return fn(*args, **kwargs)
    return time_func

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)