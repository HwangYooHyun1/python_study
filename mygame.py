import turtle as t 
import random 
import time 

# 게임 환경 설정 
t.setup(600,600)
t.bgpic('img_file/background2.gif') 
t.speed(0)
t.penup()

# 사용자 설정 
# 방향별 이미지 등록
head_images = {
    "right": "img_file/snake_head_right.gif",
    "up": "img_file/snake_head_up.gif",
    "left": "img_file/snake_head_left.gif",
    "down": "img_file/snake_head_down.gif",
    "body": "img_file/snake_body.gif"
}

tscreen = t.Screen()
for direction, image in head_images.items():
    tscreen.addshape(image)

current_direction = "down"
t.shape(head_images[current_direction])
tails = []
tails.append(t)

# 울타리 그리기 
#pen = t.Turtle()
#pen.penup()
#pen.speed(0)
#pen.color('black')
#pen.hideturtle()
#pen.setposition(-250,250)
#pen.pendown()
#pen.pensize(2)

#for x in range(4):
#    pen.forward(500)
#    pen.right(90)

#먹이 생성
f = t.Turtle()
f.hideturtle()
f.penup()
f.speed(0)

apple = "img_file/chick.gif"
tscreen = t.Screen()
tscreen.addshape(apple)
f.shape(apple)

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
    global game_running, start_lock, score, over
    game_running = False 
    start_lock = False 
    f.hideturtle()
    clear_tails()

    over = t.Turtle()
    scr = t.Screen()
    scr.addshape('img_file\game_over.gif')
    over.shape('img_file\game_over.gif')
    over.penup()
    over.speed(0)
    over.goto(0,100)
    
    t.goto(0,-50)
    t.write(f'Score:{score}',False,'center',("",20))
    t.goto(0,-100)
    t.write('[Space for Restart]',False, 'center', ("",15))
    t.home()
    

# 먹이 생성 
def feed_init():
    global fx, fy
    fx = random.randint(-240, 240)
    fy = random.randint(-240, 240)
    f.setposition(fx,fy)
    f.showturtle()

#먹이 위치 재배치 
def feed_reset():
    global fx, fy
    f.hideturtle()
    fx = random.randint(-240, 240)
    fy = random.randint(-240, 240)
    f.setposition(fx,fy)
    f.showturtle()
    add_tail()

positions = []
# 유저 이동 
def move_forward():
    if not game_running :  #게임 종료 시 정지 
        return 

    t.forward(4)
    global positions 
    positions.append(t.pos())  # 머리의 위치를 기록

    #오래된 위치 제거(배열 크기 관리)
    if len(positions) > len(tails) * 10:
        positions.pop(0)

    #울타리에 닿으면 게임 종료 
    if t.xcor()>=250 or t.xcor()<=-250 or t.ycor()>=250 or t.ycor()<=-250:
        endmsg()
        return   
    #먹이를 먹을 경우, 먹이 위치 재설정 
    global fx, fy    
    if abs(t.xcor() - fx)<=10 and abs(t.ycor() -fy)<=10:
        feed_reset()

    move_tails() #꼬리 위치 갱신 
    t.ontimer(move_forward,40)


#꼬리 이동 동기화 
def move_tails():
    if not game_running:
        return 
    
    # 꼬리의 각 부분이 앞의 부분을 따라감
    for i in range(1, len(tails)):
        tails[i].goto(positions[(-len(tails) + i)*4])

    # 머리의 이전 위치를 기록에서 제거
    if len(positions) > 100:
        positions.pop(0)


#꼬리 생성
def add_tail():
    global score, tails
    score += 10
    at = t.Turtle()
    at.penup()
    at.hideturtle()
    at.shape(head_images['body'])
    at.color(205/255, 220/255, 57/255)

    last_tail_position = tails[-1].pos()
    at.goto(last_tail_position)
    at.showturtle()
    tails.append(at)

#꼬리 초기화 
def clear_tails():
    global tails
    for tail in tails[1:]:
        tail.hideturtle()
        tail.clear()
        del tail

# keyboard 입력 설정 
def start():
    global start_lock, game_running, score, positions, tails, over
    if not start_lock:
        # 종료 이미지 숨기기 및 제거
        if 'over' in globals() and over is not None:
            over.hideturtle()
            over.clear()
            over = None  # 참조 제거

        # 초기화
        game_running = True
        start_lock = True
        score = 0
        positions = []
        clear_tails()  # 꼬리 초기화

        t.clear()
        t.setposition(0, 0)
        t.setheading(0)
        tails = [t]  # 머리만 남김
        feed_init()
        move_forward()

def r():
    global current_direction
    if game_running and current_direction != "right":
        current_direction = "right"
        t.shape(head_images["right"])
        t.setheading(0)
def u():   
    global current_direction
    if game_running and current_direction != "up":
        current_direction = "up"
        t.shape(head_images["up"])
        t.setheading(90)
def l():
    global current_direction
    if game_running and current_direction != "left":
        current_direction = "left"
        t.shape(head_images["left"])
        t.setheading(180)
def d():
    global current_direction
    if game_running and current_direction != "down":
        current_direction = "down"
        t.shape(head_images["down"])
        t.setheading(270)
    
    
t.onkeypress(r,'Right')
t.onkeypress(l,'Left')
t.onkeypress(d,'Down')
t.onkeypress(u,'Up')
t.onkeypress(start,'space')

        
t.listen()
t.done()