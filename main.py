from msvcrt import getwch
from os import system
from random import randrange

def main():
    sc=Screen.get_instance()
    player=Player(0,0)
    help=Help()
    state=0
    while True:
        c=getwch()
        if c in "wasd":
            player.move(c)
        elif c=="q":
            break
        elif c == " ":
            if help.is_correct(player.x,player.y):
                state=1
        sc.clear_board()
        if state==0:
            help.draw()
            player.draw()
        if state==1:
            help.show_help()

        sc.update()
 
 
class Help:
    def __init__(self) -> None:
        sc=Screen.get_instance()
        self.x=randrange(sc.width)
        self.y=randrange(sc.height)
        self.new_x=randrange(sc.width)
        self.new_y=randrange(sc.height)
        
    def draw(self):
        sc=Screen.get_instance()
        sc.board[self.x][self.y]="*"

    def is_correct(self,x,y):
        if x==self.x and y==self.y:
            return True
        return False
        
    def show_help(self):
        sc=Screen.get_instance()
        sc.print(f"{self.new_help.x} {self.new_help.y}")
        # print(f"{self.new_help.x} {self.new_help.y}")
        
        
class Player:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    
    def move(self,direction):
        if direction == "w":
            self.y-=1
        elif direction == "a":
            self.x-=1            
        elif direction == "s":
            self.y+=1            
        elif direction == "d":
            self.x+=1
    
    def draw(self):
        sc=Screen.get_instance()
        sc.board[self.x][self.y]="E"
                             
    
class Screen:
    instance=None
    
    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = cls(20,8)
        return cls.instance
        
    
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.board=[["." for j in range(height)] for i in range(width)]
        
    def update(self):
        system("cls")
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[j][i],end="")
            print()
            
            
    def clear_board(self):
        self.board=[["." for j in range(self.height)] for i in range(self.width)]
        
    def print(self,string,x,y):
        for i, s in enumerate(string):
            self.board[x+i][y]=s




if __name__=="__main__":
    main()