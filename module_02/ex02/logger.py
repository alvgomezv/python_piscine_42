# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/29 15:33:49 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/29 17:15:15 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint
import os

def log(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        total = f"{(end - start)if(end - start)>=1 else (end - start)*1000:.3f} {'s'if(end - start)>=1 else'ms':2}"
        string = (f"({os.environ['USER']})Running: {function.__name__.replace('_',' ').title():20}[ exec-time = {total} ]")
        with open("./machine.log", "a") as file:
            file.write(string + '\n')
        return result
    return wrapper
 
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