import random
from core import Bomb
from tkinter import *
from tkinter.messagebox import showinfo

class Interface(Frame) :
   
    answer = [True,False]
    row = 5
    column = 5

    def __init__(self, master):
        baris = Interface.row  
        kolom = Interface.column
        self.master = master
        self.master.title("Minesweeper")
        super().__init__(master) # super from Frame
        title = Label(master, text = "Welcome to Noanosweeper", font = ("Helvetica", 12, "bold"))
        title.pack()
        bom = Bomb(baris,kolom)
        self.bomku = bom.dict_bomb
        self.num = list(self.bomku.values())
        self.count = self.num.count("clear")
        
        for i in range(baris) :
            for j in range(kolom) :
                self.button = Button(self, command = lambda i=i,j=j : self.get_coor(i,j), height = 1, width = 1)
                self.button.grid( row = i+2, column = j)
        self.reset = Button(self, text = "reset", command = self.reset)
        self.reset.grid( row = 7, column = 0, columnspan = 5)
            

    def get_coor(self,row, col) :
        baris = Interface.row  
        kolom = Interface.column
        self.row = row
        self.col = col
        if self.bomku[(self.row,self.col)] == "bomb" :
            for i in range(baris) :
                for j in range(kolom) :
                    if self.bomku[(i,j)] == "bomb" :
                        self.button_fake = Button(self, activebackground = "red", bg = "red", text = ":O", height = 1, width = 1)
                        self.button_fake.grid( row = i+2, column = j)
                    else :
                        self.button_fake = Button(self, text = ":)", height = 1, width = 1,activebackground = "blue", bg = "blue")
                        self.button_fake.grid( row = i+2, column = j)
            showinfo(message = "HAHAHA you lose")
            
        else :
            self.button_fake = Button(self, text = ":)", height = 1, width = 1,activebackground = "blue", bg = "blue")
            self.button_fake.grid( row = self.row+2, column = self.col)
            self.count -= 1
            
            if random.choice(Interface.answer) == True :
                a = [ x for x in range(2,Interface.row+1)]
                for i in range(2,random.choice(a)) :
                    for j in range(2,random.choice(a)) :
                        if self.bomku[(i,j)] != "bomb" :
                            self.button_fake = Button(self, text = ":)", height = 1, width = 1,activebackground = "blue", bg = "blue")
                            self.button_fake.grid( row = i, column = j)
                            self.count -= 1
                            

            if self.count == 0 :
                showinfo(message = "congrats you win the game!")
                self.button_fake.destroy()
                self.reset = Button(self, text = "reset", command = self.reset)
                self.reset.grid( row = 4, column = 0, columnspan = 2)
                

    def reset(self) :
        
        baris = Interface.row  
        kolom = Interface.column
        bom = Bomb(baris,kolom)
        self.bomku = bom.dict_bomb
        self.num = list(self.bomku.values())
        self.count = self.num.count("clear")
                
        for i in range(baris) :
            for j in range(kolom) :
                self.button = Button(self, command = lambda i=i,j=j : self.get_coor(i,j), height = 1, width = 1)
                self.button.grid( row = i+2, column = j)



def main() :        
    root = Tk()
    app = Interface(root)
    app.pack()
    root.mainloop()


if __name__ == '__main__':
    main()





