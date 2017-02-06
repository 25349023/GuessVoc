import random
import sys
import threading
import time

import xlrd


class Player:
    def __init__(self):
        self.name = 'guest'

    def set_name(self):
        self.name = input("your name is: ")


class Draw:
    def __init__(self):
        self.answer = ''
        self.get_answer = False
        self.inExtraLife = False
        self.speak = 0
        self.timesUp = False

    def front_ques(self):
        self.answer = '!'
        for x in range(length):
            print(block[x], end=" ")
        print('\n')
        print(hint)
        print("↑ 有{}個字母, 猜一個字母: ".format(str(length)), end='')
        sys.stdout.flush()

    def ques(self):
        self.front_ques()
        self.get_answer = False
        input1 = input()
        self.get_answer = True
        self.answer = input1 if input1 != '' else self.answer
        if self.timesUp:
            self.timesUp = False

    @staticmethod
    def gibbet():
        print("        _________")
        for x in range(2):
            print("       │        │")
        for x in range(12):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def head():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ┌─┴─┐")
        print("       │      │   │")
        print("       │      └───┘")
        for x in range(9):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def body():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ┌─┴─┐")
        print("       │      │   │")
        print("       │      └─┬─┘")
        for x in range(3):
            print("       │        │")
        for x in range(6):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def sim_hand():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ┌─┴─┐")
        print("       │      │   │")
        print("       │      └─┬─┘")
        print("       │        │")
        print("       │       /│")
        print("       │      / │")
        for x in range(6):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def dou_hand():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ┌─┴─┐")
        print("       │      │   │")
        print("       │      └─┬─┘")
        print("       │        │")
        print("       │       /│\\")
        print("       │      / │ \\")
        for x in range(6):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def sim_foot():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ┌─┴─┐")
        print("       │      │   │")
        print("       │      └─┬─┘")
        print("       │        │")
        print("       │       /│\\")
        print("       │      / │ \\")
        print("       │        │")
        print("       │       /")
        print("       │      /")
        print("       │     /")
        for x in range(3):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def dou_foot():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ┌─┴─┐")
        print("       │      │   │")
        print("       │      └─┬─┘")
        print("       │        │")
        print("       │       /│\\")
        print("       │      / │ \\")
        print("       │        │")
        print("       │       / \\")
        print("       │      /   \\")
        print("       │     /     \\")
        for x in range(3):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def died():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ┌─┴─┐")
        print("       │      │   │")
        print("       │      └─┬─┘")
        for x in range(7):
            print("       │")
        print("       │ ──/  ＼ － ＿")
        print("       │   ＼ _ ／  －\\ ┘ ")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")
        print("you lose!")

    @staticmethod
    def win():
        print("        _________")
        for x in range(2):
            print("       │        │")
        print("       │      ")
        print("       │      ┌───┐")
        print("       │      │   │ <YA!")
        print("       │      └─┬─┘")
        print("       │        │")
        print("       │    ＼  │  ／")
        print("       │      ＼│／")
        print("       │        │")
        print("       │       / \\")
        print("       │      /   \\")
        print("       │     /     \\")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    def paint(self, typ):
        if typ == 0:
            self.gibbet()
        elif typ == 1:
            self.head()
        elif typ == 2:
            self.body()
        elif typ == 3:
            self.sim_hand()
        elif typ == 4:
            self.dou_hand()
        elif typ == 5:
            self.sim_foot()
        elif typ == 6:
            self.dou_foot()
        elif typ == 7:
            self.died()
        else:
            self.gibbet()


wb = xlrd.open_workbook('senior_7000.xls')
shra = random.randrange(0, 5)
sh = wb.sheet_by_index(shra)
all_rows = sh.nrows

ra = random.randrange(0, all_rows - 1)
que = sh.cell(ra, 0).value
pos = que.find('@')

question = que[:pos]
hint = que[pos + 1:]
_copy = question
py = Player()
painter = Draw()
py.set_name()
length = len(question)
block = []
for i in range(length):
    block += '_'
bingo = 0
bre = 0
print("hello, " + py.name)
mode = 0
while mode != 1 and mode != 2:
    tmp = True
    try:
        mode = int(input('你想要玩什麼模式? 1:普通模式,  2:限時(5秒)模式  [1/2]: '))
    except ValueError:
        print('請輸入 1 或 2')
        tmp = False
    if (mode != 1 and mode != 2) and tmp:
        print('請輸入 1 或 2')

print('\nGAME START!!')
while True:
    wrong = 0
    while True:
        bingo = 0
        painter.paint(wrong)
        if mode == 2:
            if not painter.timesUp:
                tdraw = threading.Thread(target=painter.ques, daemon=True)
                tdraw.start()
                tdraw.join(5)
            else:
                painter.front_ques()
                if painter.inExtraLife:
                    tdraw.join()
                else:
                    tdraw.join(5)
            if not painter.get_answer:
                painter.timesUp = True
            else:
                painter.timesUp = False
                painter.speak += 1
                tdraw = None
                del tdraw
        else:
            painter.ques()

        for i in range(length):
            if painter.answer == question[i]:
                block[i] = painter.answer
                question = question[:i] + '_' + question[(i + 1):]
                bingo = 1
                break

        if bingo == 1:  # if find
            print()
            print("Yes,it's true!")
            print()
        else:
            print()
            print("No,it's wrong." if not painter.timesUp else "Time's up!")
            print()
            wrong += 1

        if mode == 2:
            if wrong == 7 and painter.speak == 0:
                wrong -= 1
                print('EXTRA LIFE!!!')
                painter.inExtraLife = True
            else:
                painter.inExtraLife = False

        if wrong == 7:
            painter.paint(wrong)
            break

        for i in range(length):
            if block[i] == '_':
                break
            elif block[i] != '_' and i == (length - 1):
                bre = 1

        if bre == 1:
            break

    if bre == 1:
        painter.win()
        print("answer is : ", end="")
        print(_copy + '  ' + hint)
        break
    elif bre == 0:
        print("answer is : ", end="")
        print(_copy + '  ' + hint)
        break

print('\nClose after 5 second.')
time.sleep(5)
