import random
import re
import shelve
import sys
import threading

import time
import xlrd


class Player:
    def __init__(self):
        self.name = 'guest'
        self.play_time = 0
        self.success = 0
        self.fail = 0
        self.play_time2 = 0
        self.success2 = 0
        self.fail2 = 0

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
    def just_head(neck=True, win=False):
        if win:
            print("       │      ┌─┐")
            print("       │      │  │ <YA!")
            print("       │      └┬┘")
        else:
            print("       │      ┌┴┐")
            print("       │      │  │")
            if neck:
                print("       │      └┬┘")
            else:
                print("       │      └─┘")

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
        Draw.just_head(False)
        for x in range(9):
            print("       │")
        print("   ￣￣￣￣￣￣￣￣￣￣￣￣")

    @staticmethod
    def body():
        print("        _________")
        for x in range(2):
            print("       │        │")
        Draw.just_head()
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
        Draw.just_head()
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
        Draw.just_head()
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
        Draw.just_head()
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
        Draw.just_head()
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
        Draw.just_head()
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
        Draw.just_head(win=True)
        print("       │        │")
        print("       │    ＼  │  ／")
        print("       │      ＼│／")
        print("       │        │")
        print("       │        /\\")
        print("       │       /  \\")
        print("       │      /    \\")
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


rnd = 0
py = Player()
while True:
    wb = xlrd.open_workbook('senior_7000.xls')
    shra = random.randint(0, 5)
    sh = wb.sheet_by_index(shra)
    all_rows = sh.nrows

    ra = random.randrange(0, all_rows - 1)
    que = sh.cell(ra, 0).value
    pos = que.find('@')

    question = que[:pos]
    hint = que[pos + 1:]
    _copy = question
    painter = Draw()
    while not rnd:
        py.set_name()
        shel_file = shelve.open('record.shv')
        if py.name == 'del player':
            for n in shel_file.keys():
                print(n)
            want_to_delete = input('請輸入你要刪掉的玩家名: ')
            if want_to_delete in shel_file.keys():
                del shel_file[want_to_delete]
                print()
        elif py.name in shel_file.keys():
            print('hey {name}, 有一個你之前的紀錄, 要繼續嗎?'.format(name=py.name))
            print('1: 繼續上次的紀錄')
            print('2: 不要繼續並覆蓋前次紀錄')
            print('3: 自動幫我更改這次的名字')
            print('4: 讓我改一下名字')
            inp = 0
            while inp < 1 or inp > 4:
                tmp = True
                try:
                    inp = int(input())
                except ValueError:
                    print('請輸入 1~4')
                    tmp = False
                if (inp < 1 or inp > 4) and tmp:
                    print('請輸入 1~4')
            if inp == 1:
                py = shel_file[py.name]
            elif inp == 2:
                break
            elif inp == 3:
                name_reg = re.compile(r'(.*)_(\d+)$')
                while py.name in shel_file.keys():
                    num = name_reg.search(py.name)
                    if num is None:
                        py.name += '_2'
                    else:
                        suffix = num.group(2)
                        py.name = name_reg.sub(r'\1_{n}'.format(n=int(suffix) + 1), py.name)
            elif inp == 4:
                continue
            shel_file.close()
            break
        else:
            break

    rnd += 1
    length = len(question)
    block = []
    for i in range(length):
        block += '_'
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
            bingo = False
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

            if painter.answer in question:
                index = question.find(painter.answer)
                len_a = len(painter.answer)
                block[index:index + len_a] = painter.answer
                question = question[:index] + '_' * len_a + question[index + len_a:]
                bingo = True

            if bingo:  # if find
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
            if mode == 1:
                py.success += 1
            else:
                py.success2 += 1
            print("answer is : ", end="")
            print(_copy + '  ' + hint)
            break
        elif bre == 0:
            if mode == 1:
                py.fail += 1
            else:
                py.fail2 += 1
            print("answer is : ", end="")
            print(_copy + '  ' + hint)
            break

    if mode == 1:
        py.play_time += 1
    else:
        py.play_time2 += 1
    con = input("還要再來一場嗎?[Y/n]: ").lower()
    if con == 'n':
        print('\nHey', py.name + ', 你總共玩了', py.play_time, '場普通模式,\n其中',
              py.success, '場成功, ', py.fail, '場失敗, ', end='')
        print('成功率約 {}%.'.format(py.success / py.play_time * 100) if py.play_time else '成功率約 --%.')
        print('\n另外, 你總共玩了', py.play_time2, '場限時模式,\n其中',
              py.success2, '場成功, ', py.fail2, '場失敗, ', end='')
        print('成功率約 {}%.'.format(py.success2 / py.play_time2 * 100) if py.play_time2 else '成功率約 --%.')
        print('共有 {} 人因你而死(X'.format(py.fail + py.fail2))
        shel_file = shelve.open('record.shv')
        shel_file[py.name] = py
        shel_file.close()
        break

print('\n\nClose after 1 minute.')
time.sleep(60)
