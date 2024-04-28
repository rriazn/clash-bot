import pyautogui as pag
from time import sleep
import src.maths as maths


monitor_width = 0
monitor_height = 0


def init(mw, mh):
    global monitor_width, monitor_height
    monitor_width = mw
    monitor_height = mh


def collect_resources():
    gold = pag.locateOnScreen("images/other/collect_gold.PNG", confidence=0.8)
    i = 0
    while gold and i < 8:
        print("found Gold")
        pag.leftClick(gold)
        sleep(maths.rand(1))
        gold = pag.locateOnScreen("images/other/collect_gold.PNG", confidence=0.8)
        i = i + 1

    elixir = pag.locateOnScreen("images/other/collect_elixir.PNG", confidence=0.8)
    i = 0
    while elixir and i < 8:
        print("found Elixir")
        pag.leftClick(elixir)
        sleep(maths.rand(1))
        elixir = pag.locateOnScreen("images/other/collect_elixir.PNG", confidence=0.8)
        i = i + 1


def train_troops():
    barrack = pag.locateOnScreen("images/buildings/barrack_l2.PNG", confidence=0.8)
    if not barrack:
        return
    print("found barrack")
    pag.leftClick(barrack)
    sleep(maths.rand(1))
    train_button = pag.locateOnScreen("images/buttons/train_troops_barrack.PNG", confidence=0.8)
    if not train_button:
        return
    pag.leftClick(train_button)
    sleep(maths.rand(1))
    barbarian = pag.locateOnScreen("images/troops/barbarian.PNG", confidence=0.8, grayscale=False)
    while barbarian:
        pag.doubleClick(barbarian)
        barbarian = pag.locateOnScreen("images/troops/barbarian.PNG", confidence=0.8, grayscale=False)
    x_button = pag.locateOnScreen("images/buttons/x_button.PNG", confidence=0.8)
    if not x_button:
        print("couldn't find x button")
        return
    pag.leftClick(x_button)

