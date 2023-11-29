from tkinter import*
import random

def next_turn(row,column):
    global player
    if(button[row][column]['text']==""and winner()is False):
        if(player==players[0]):
            button[row][column]['text']=player
            if(winner() is False):
                player=players[1]
                lable.config(text=players[1]+"turn")
            elif(winner() is True):
                lable.config(text=players[0]+" vectory")
            elif(winner()=="tie"):
                lable.config(text="tie")
        else:
            
                button[row][column]['text']=player
                if(winner() is False):
                    player=players[0]
                    lable.config(text=players[0]+"turn")
                elif(winner() is True):
                    lable.config(text=players[1]+" vectory")
                elif(winner()=="tie"):
                    lable.config(text="tie")   
def new_game():
    pass
def winner():
    for row in range(3):
        if(button[row][0]['text']==button[row][1]['text']==button[row][2]['text']!=''):
             return True
    for column in range(3):
        if(button[0][column]['text']==button[1][column]['text']==button[2][column]['text']!=''):
             return True
    if(button[0][0]['text']==button[1][1]['text']==button[2][2]['text']!=''):
         return True
    elif(button[2][0]['text']==button[1][1]['text']==button[0][2]['text']!=''):
        return True
    elif (space() is False):
        return "tie"
    else:
        return False
def space():
    space=9
    for row in range(3):
        for column  in range(3):
            if button[row][column]['text']!='':
                space-=1
    if(space==0):
        return False
    

windo=Tk()
windo.title("tic-tac-tio")
players=["x","o"]
player=random.choice(players)
button=[[0,0,0],[0,0,0],[0,0,0]]
lable=Label(text=player+"turn",font=('consolas',40))
lable.pack(side='top')
restart_button=Button(text='restart',font=('consolas',40),command=new_game())
restart_button.pack(side='bottom')
frame=Frame(windo)
frame.pack()
for row in range(3):
    for column in range(3):
        button[row][column]=Button(frame,text='',font=('italic'),width=5,height=2,
                                command=lambda row=row,column=column:next_turn(row,column))
        button[row][column].grid(row=row,column=column)
windo.mainloop()
