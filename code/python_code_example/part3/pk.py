
'''
    炸金花小游戏？
    写的并不好
    苏宁面试题
    题目要求在这：http://hehe_thirtyseven.gitee.io/images/pk.png
    要求用时1小时
    实际用时2小时...
'''
import random

class poke():
    def __init__(self):
        self.pokelist = []
        self.sendlist = []
        for i in range(0,13):
            for j in range(0,4):
                self.pokelist.append((i,j))

    def printpoke(self):
        print(self.sendlist)

    def makecard(self):
        pokemap = {}
        count = 0
        while count<15:
            number = random.randint(0,51)
            if number not in pokemap.values():
                pokemap.update({count:number})
                count += 1
            else:
                continue

        for i in pokemap.keys():
            self.sendlist.append(self.pokelist[pokemap[i]])

    def sendcard(self):
        playerlist = []
        for _ in range(3):
            playerlist.append(self.sendlist.pop())
        return playerlist

class player():
    def __init__(self,pokelist:list):
        self.pokelist = pokelist
        self.pokelist.sort()
        print(self.pokelist)
        self.card1 = self.pokelist[0]
        self.card2 = self.pokelist[1]
        self.card3 = self.pokelist[2]

        self.socredict = {
            "singal":0,
            "double":False,
            "fdouble":False,
            "gdouble":False,
            "leopard":False,
            "total":0
        }

    def doall(self):
        for i in range(3):
            carenumber = self.pokelist[i]
            self.socredict["singal"] += 12-carenumber[0]

        self.socredict["total"] += self.socredict["singal"]

        # none
        if self.card1[0] == self.card2[0] or self.card1[0] == self.card3[0] or self.card2[0] == self.card3[0]:
            self.socredict["double"] = True
            self.socredict["total"] += 50

        if self.card1[0] == self.card2[0] -1 == self.card3[0] - 2:
            self.socredict["fdouble"] = True
            self.socredict["total"] += 100
            if self.card1[1] == self.card2[1] == self.card3[1]:
                self.socredict["gdouble"] = True
                self.socredict["total"] += 150

        # none
        if self.card1[0] == self.card2[0] == self.card3[0]:
            self.socredict["leopard"] = True
            self.socredict["total"] += 200

        print(self.socredict)

if __name__ == '__main__':
    newpoke = poke()
    newpoke.makecard()
    newpoke.printpoke()

    player1 = player(newpoke.sendcard())
    player1.doall()

    player2 = player(newpoke.sendcard())
    player2.doall()

    player3 = player(newpoke.sendcard())
    player3.doall()

    player4 = player(newpoke.sendcard())
    player4.doall()

    player5 = player(newpoke.sendcard())
    player5.doall()

    socrelist = []
    socrelist.append((player1.socredict["total"], 1))
    socrelist.append((player2.socredict["total"], 2))
    socrelist.append((player3.socredict["total"], 3))
    socrelist.append((player4.socredict["total"], 4))
    socrelist.append((player5.socredict["total"], 5))
    socrelist.sort(reverse=True)
    print(socrelist)
    it = iter(socrelist)
    num = 1
    for i in it:
        print("第%d名:%d号选手|得分%d"%(num,i[1],i[0]))
        num += 1
