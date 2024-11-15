import turtle as t 
import random as r 

t.setup(700,700)
t.bgcolor('pink')
t.speed(1)
t.penup()

t.shape('square')
t.color('green')

game_running = True 

# 시작 화면
def startmsg(msg1, msg2):
    global game_running 
    game_running = True 
    
    t.clear()
    t.goto(0,100)
    t.write(msg1, False, 'center', ("",20))
    t.goto(0,-100)
    t.write(msg2,False, 'center', ("",15))
    t.home()

startmsg('지렁이 게임','[Space for Start]')

#종료화면
def endmsg():
    global game_running 
    game_running = False 
    t.clear()
    t.goto(0,100)
    t.write('게임이 끝났습니다',False,'center',("",20))
    t.goto(0,-100)
    t.write('[Space for Restart]',False, 'center', ("",15))
    t.home()
    

# 울타리 그리기 
pen = t.Turtle()
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.setposition(-303,303)
pen.pendown()
pen.pensize(2)

for x in range(4):
    pen.forward(600)
    pen.right(90)



def move_forward():
    if not game_running :
        return 
    t.forward(10)
    if t.xcor()>=300 or t.xcor()<=-300 or t.ycor()>=300 or t.ycor()<=-300:
        endmsg()
        return       
    t.ontimer(move_forward,0)
    
def r():
    t.setheading(0)
    move_forward()
def u():   
    t.setheading(90)
    move_forward()
def l():
    t.setheading(180)
    move_forward()
def d():
    t.setheading(270)
    move_forward()
    
def start():
    t.clear()
    
t.onkeypress(r,'Right')
t.onkeypress(l,'Left')
t.onkeypress(d,'Down')
t.onkeypress(u,'Up')
t.onkeypress(start,'space')

        
t.listen()
t.done()