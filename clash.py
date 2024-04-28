import pyautogui as pag
import random as r
import src.base as base
from time import sleep
import src.attack as attack
import src.maths


monitor_width = 0
monitor_height = 0




if __name__ == '__main__':
    #sleep(3)
    #init()
    #attack.find_base(1500, 0)
    #print(attack.count_resources("gold"))
    #print(attack.count_resources("elixir"))
    #screenshot()
    #attack.start_attack()
    #attack.find_base(2500, 0)
    #base.collect_resources()
    #base.train_troops()
    for i in range(15):
        print(r.randint(1,20))

#gold at top 200, elixir at top 250
#numbers start at left 100, 20 diff, 30 if space
#region=(100, 200, 20, 30)
#region=(int(monitor_width/19.8), int(monitor_height/6.1),
 #                   int(monitor_width/19.8 + monitor_width/80), int(monitor_height/6.1 + monitor_height/37.5))
 #region=(monitor_width/19.8, monitor_height/6.1, monitor_width/80, monitor_height/37.5))