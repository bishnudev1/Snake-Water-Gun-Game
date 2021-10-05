from tkinter import * 
from PIL import Image,ImageTk
from random import randint

goku_root = Tk()
goku_root.title("Snake,Water & Gun Game")
goku_root.configure(bg="white")


Bishnudev = Label(goku_root,font=70,text="Snake, Water & Gun Game By Bishnudev",fg="skyblue").grid(row=0,column=2)
user_indicator = Label(goku_root,font=50,text="USER").grid(row=0,column=0)
comp_indicator = Label(goku_root,font=50,text="COMPUTER").grid(row=0,column=4)
msg = Label(goku_root,font=50,fg="black")
msg.grid(row=1,column=2)


water_img = ImageTk.PhotoImage(Image.open("water.png"))
snake_img = ImageTk.PhotoImage(Image.open("snake.png"))
gun_img = ImageTk.PhotoImage(Image.open("gun.png"))
water_comp_img = ImageTk.PhotoImage(Image.open("water.png"))
snake_comp_img = ImageTk.PhotoImage(Image.open("water.png"))
gun_comp_img = ImageTk.PhotoImage(Image.open("water.png"))

user_label = Label(goku_root,image=snake_img,bg="white")
comp_label = Label(goku_root,image=snake_img,bg="white")
user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)


compChoices = ["water","snake","gun"]
def choice(x):
              compstack = compChoices[randint(0,2)]
              if compstack == "water":
                            comp_label.configure(image = water_img)
              elif compstack == "snake":
                            comp_label.configure(image = snake_img)
              else:
                            comp_label.configure(image = gun_img)


              if(x == "water"):
                              user_label.configure(image = water_img)
              elif(x == "snake"):
                              user_label.configure(image = snake_img)
              elif(x == "gun"):
                              user_label.configure(image = gun_img)

              check_win(x,compstack)

snake = Button(goku_root,width=20,height=2,text="SNAKE",bg="yellow",fg="black",command=lambda:choice("snake")).grid(row=2,column=2)
water = Button(goku_root,width=20,height=2,text="WATER",bg="blue",fg="black",command=lambda:choice("water")).grid(row=2,column=1)
gun = Button(goku_root,width=20,height=2,text="GUN",bg="yellow",fg="black",command=lambda:choice("gun")).grid(row=2,column=3)

def updateM(x):
              msg['text'] = x

def check_win(player,computer):
                              if player == computer:
                                      updateM("It's Tie !")
                              elif player == "water":
                                  if computer == "snake":
                                                        updateM("You Lost !")
                                  else:
                                                        updateM("You Won !")
                              elif player == "gun":
                                  if computer == "water":
                                                        updateM("You Lost !")
                                  else:
                                                        updateM("You Won !")
                              elif player == "snake":
                                  if computer == "gun":
                                                        updateM("You Lost !")
                                  else:
                                                        updateM("You Won !")


goku_root.mainloop()