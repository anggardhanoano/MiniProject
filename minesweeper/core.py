import random

class Bomb :
    list_of_bomb = []
    dict_bomb = {}
    def __init__(self, row, col) :
        self.row = row
        self.col = col

        for i in range(int(self.row)) :
            for j in range(int(self.col)) :
                Bomb.list_of_bomb.append((i,j))

        self.shuffle()
    
    def shuffle(self) :
        self.shuf = ["bomb", "clear", "clear"]

        for i in range(len(Bomb.list_of_bomb)) :
            Bomb.dict_bomb[Bomb.list_of_bomb[i]] = random.choice(self.shuf)
        return Bomb.dict_bomb
    
