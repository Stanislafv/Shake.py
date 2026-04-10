import tkinter as tk
import random
root = tk.Tk()
root.title("Shake.py")
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

snake = [(2,2),(2,0),(1,0)]

game_over = False
kletra_size = 20
x = 0
y = 0
x_apple = 2000
y_apple = 2000
scor = 3

rotate = "right"
current_rotate = "right"
def move():
    canvas.delete("all")
    global game_over
    global scor
    global new_head_coord
    global x
    global y
    global current_rotate
    global rotate
    global snake_cell
    #поворот
    if rotate == "right" and current_rotate != "left":
        current_rotate = "right"
        x=1
        y=0
    elif rotate == "top" and current_rotate != "down":
        current_rotate = "top"
        x = 0
        y=-1
    elif rotate == "left" and current_rotate != "right":
        current_rotate = "left"
        x=-1
        y=0
    elif rotate == "down" and current_rotate != "top":
        current_rotate = "down"
        x=0
        y=1

    new_head_x = (((snake[0])[0])+x)
    new_head_y = (((snake[0])[1])+y)

    new_head_coord = (new_head_x, new_head_y)

    if new_head_coord in snake:
        game_over = True
        canvas.delete("all")
        canvas.create_text(200, 200, text="GAME OVER", fill="white", font=("Arial", 30))
        return

    snake.insert(0, new_head_coord)

    #кушать
    if new_head_coord != (x_apple,y_apple):
        snake.pop()
    else:
        apple()
        scor += 1
    if new_head_x == 20:
        snake.insert(0,((new_head_x-19),new_head_y))
        snake.pop()
    elif new_head_x == 0:
        snake.insert(0,((new_head_x+19),new_head_y))
        snake.pop()
    elif new_head_y == 20:
        snake.insert(0,(new_head_x,(new_head_y-20)))
        snake.pop()
    elif new_head_y == -1:
        snake.insert(0,(new_head_x,(new_head_y+21)))
        snake.pop()
    for segment in snake:
        seg_x = segment[0]*kletra_size
        seg_y = segment[1]*kletra_size
        canvas.create_rectangle(seg_x, seg_y, seg_x + kletra_size, seg_y + kletra_size, fill="green")
#выборстороны
def direct(event):
    global rotate
    if event.keysym == "Up":
        rotate = "top"
    elif event.keysym == "Left":
        rotate = "left"    
    elif event.keysym == "Down":
        rotate = "down"    
    elif event.keysym == "Right":
        rotate = "right"        

def apple():
    global x_apple
    global y_apple
    x_apple = random.randint(1,19)
    y_apple = random.randint(1,19)

def generate():
    global x_apple
    global y_apple
    canvas.create_rectangle((x_apple*kletra_size), (y_apple*kletra_size), (x_apple*kletra_size)+kletra_size, (y_apple*kletra_size)+kletra_size, fill="red")

def score():
    global scor
    canvas.create_text(45, 20, text=("Счёт:",scor), font=("Courier New", 16, "bold"), fill="white")

def loop():
    if game_over == False:
        root.after((int(200/(scor/3))), loop)
        move()
        generate()
        score()

loop()
apple()

#забиндитьчтоб
root.bind('<Up>', direct)
root.bind('<Down>', direct)
root.bind('<Left>', direct)
root.bind('<Right>', direct)

root.mainloop()