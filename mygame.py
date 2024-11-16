import turtle as t 
import random 
import time 

# 게임 환경 설정 
t.setup(700,700)
t.bgcolor('pink')
t.speed(1)
t.penup()

#사용자 설정 
t.shape('square')
t.color('green')
tails = []
tails.append(t)

# 울타리 그리기 
pen = t.Turtle()
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.setposition(-305,305)
pen.pendown()
pen.pensize(2)

for x in range(4):
    pen.forward(600)
    pen.right(90)

#먹이 생성
f = t.Turtle()
f.hideturtle()
f.penup()
f.speed(0)
f.shape('circle')
f.color('red')

game_running = True #게임 시작 상태
start_lock = False #게임 시작 시, spacebar lock을 위한 변수  
score = 0 

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
    global game_running, start_lock
    game_running = False 
    start_lock = False 

    f.clear()
    t.goto(0,100)
    t.write('게임이 끝났습니다',False,'center',("",20))
    t.goto(0,-100)
    t.write('[Space for Restart]',False, 'center', ("",15))
    t.home()
    

# 먹이 생성 
def feed_init():
    global fx, fy
    fx = random.randint(-290, 290)
    fy = random.randint(-290, 290)
    f.setposition(fx,fy)
    f.showturtle()

#먹이 위치 재배치 
def feed_reset():
    global fx, fy
    f.hideturtle()
    fx = random.randint(-290, 290)
    fy = random.randint(-290, 290)
    f.setposition(fx,fy)
    f.showturtle()
    add_tail()

positions = []
# 유저 이동 
def move_forward():
    if not game_running :  #게임 종료 시 정지 
        return 

    global positions 
    positions.append(t.pos())  # 머리의 위치를 기록
    t.forward(3)

    #오래된 위치 제거(배열 크기 관리)
    if len(positions) > len(tails) * 10:
        positions.pop(0)

    #울타리에 닿으면 게임 종료 
    if t.xcor()>=300 or t.xcor()<=-300 or t.ycor()>=300 or t.ycor()<=-300:
        endmsg()
        return   
    #먹이를 먹을 경우, 먹이 위치 재설정 
    global fx, fy    
    if abs(abs(t.xcor()) - abs(fx))<=10 and abs(abs(t.ycor()) -abs(fy))<=10:
        feed_reset()

    move_tails() #꼬리 위치 갱신 
    t.ontimer(move_forward,0)


#꼬리 이동 동기화 
def move_tails():
    if not game_running:
        return 
    
    # 꼬리의 각 부분이 앞의 부분을 따라감
    for i in range(1, len(tails)):
        tails[i].goto(positions[(-len(tails) + i)*9])

    # 머리의 이전 위치를 기록에서 제거
    if len(positions) > 100:
        positions.pop(0)


#꼬리 생성
def add_tail():
    global score, tails
    score += 1
    at = t.Turtle()
    at.penup()
    at.hideturtle()
    at.shape('square')
    at.color('green')

    last_tail_position = tails[-1].pos()
    at.goto(last_tail_position)
    at.showturtle()
    tails.append(at)



# keyboard 입력 설정 
def start():
    global start_lock
    if not start_lock:
        game_running = True
        t.clear()
        feed_init()
        start_lock = True   #게임 시작 시, spacebar lock 

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
    
    
t.onkeypress(r,'Right')
t.onkeypress(l,'Left')
t.onkeypress(d,'Down')
t.onkeypress(u,'Up')
t.onkeypress(start,'space')

        
t.listen()
t.done()