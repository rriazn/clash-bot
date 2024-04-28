import pyautogui as pag
import src.maths as maths
from time import sleep


monitor_width = 0
monitor_height = 0


def init(mw, mh):
    global monitor_width, monitor_height
    monitor_width = mw
    monitor_height = mh


def start_attack():
    attack_button = pag.locateOnScreen("images/buttons/attack.PNG", confidence=0.8)
    if not attack_button:
        print("couldn't find attack button")
        return False
    pag.leftClick(attack_button)
    sleep(maths.rand(1))
    find_battle = pag.locateOnScreen("images/buttons/find_battle.PNG", confidence=0.8)
    if not find_battle:
        print("couldn't find battle button")
        return False
    pag.leftClick(find_battle)
    return True


def count_resources(resource):
    max_it = 7
    top = 0
    if resource == "gold":
        top = 190
    elif resource == "elixir":
        top = 250
    elif resource == "dark elixir":
        top = 310
        max_it = 5
    resources = []
    offset = 0
    i = 0
    k = 0
    while i < max_it and offset <= 12:
        x = None
        k += 1
        for j in range(10):
            x = pag.locateOnScreen("images/digits/" + str(j) + ".PNG", region=(90 + i*20 + offset, top, 30, 40), confidence=0.8)
            #pag.screenshot(region=(90 + i * 20 + offset, top, 30, 40)).save(r"test" + str(k) + ".PNG")
            if x:
                #pag.screenshot(region=(90 + i * 20 + offset, top, 30, 40)).save(r"test" + str(k) + ".PNG")
                resources.append(j)
                break
        if not x:
            offset += 3
        else:
            i += 1
    if len(resources) == 0:
        print("Couldn't find resource \"" + resource + "\"")
        return 0
    return int(''.join(map(str, resources)))


def find_base(min_loot, min_dark):
    dark = False
    if min_dark > 0:
        dark = True
    next_button = pag.locateOnScreen("images/buttons/next_button.PNG", confidence=0.8)
    if not next_button:
        return False
    while True:
        sleep(5)
        gold = count_resources("gold")
        elixir = count_resources("elixir")
        if dark:
            dark_elixir = count_resources("dark elixir")
            if dark_elixir < min_dark:
                pag.leftClick(next_button)
                continue
        rsum = gold + elixir
        print(rsum)
        if rsum < min_loot or gold < min_loot / 3 or elixir < min_loot / 3:
            print("next village")
            pag.leftClick(next_button)
            continue
        break


def attack():
    town_hall = pag.locateOnScreen("images/buildings/town_hall_l2.PNG", confidence=0.8)
    while not town_hall:
        print("couldn't find townhall")
        find_base(10000000, 0)
        sleep(5)
        town_hall = pag.locateOnScreen("images/buildings/town_hall_l2.PNG", confidence=0.8)
    zone_ne = pag.locateOnScreen("images/other/zone_ne.PNG", confidence=0.8)
    zone_nw = pag.locateOnScreen("images/other/zone_nw.PNG", confidence=0.8)
    zone_se = pag.locateOnScreen("images/other/zone_se.PNG", confidence=0.8)
    zone_sw = pag.locateOnScreen("images/other/zone_sw.PNG", confidence=0.8)
    if not(zone_se or zone_ne or zone_sw or zone_nw):
        print("couldn't find one edge")