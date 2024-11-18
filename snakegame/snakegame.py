import turtle as t 
import random 
import time 

# 게임 환경 설정 
t.setup(600,600)
t.bgpic('D:/python_study/python_study/snakegame/img_file/background2.gif') 
t.speed(0)
t.penup()
t.hideturtle()

# 사용자 설정 
# 방향별 이미지 등록
head_images = {
    "right": "D:/python_study/python_study/snakegame/img_file/snake_head_right.gif",
    "up": "D:/python_study/python_study/snakegame/img_file/snake_head_up.gif",
    "left": "D:/python_study/python_study/snakegame/img_file/snake_head_left.gif",
    "down": "D:/python_study/python_study/snakegame/img_file/snake_head_down.gif",
    "body": "D:/python_study/python_study/snakegame/img_file/snake_body.gif"
}

tscreen = t.Screen()
for direction, image in head_images.items():
    tscreen.addshape(image)

# 머리와 몸통 터틀 생성
head = t.Turtle()
head.penup()
head.shape(head_images["up"])
head.speed(0)
current_direction = "up"

body = t.Turtle()  # 몸통 전용 터틀
body.penup()
body.hideturtle()  # 몸통 터틀은 스탬프만 찍음
body.shape(head_images['body'])
body.speed(0)

# 나머지 꼬리 관리
body_stamps = []  # 꼬리 도장 리스트
max_tail_length = 1  # 초기 꼬리 길이

#스타트 메시지 출력
msg = t.Turtle()
msg.hideturtle()
msg.penup()

#먹이 생성
f = t.Turtle()
f.hideturtle()
f.penup()
f.speed(0)

chick = "D:/python_study/python_study/snakegame/img_file/chick.gif"
tscreen = t.Screen()
tscreen.addshape(chick)
f.shape(chick)


game_running = True #게임 시작 상태
start_lock = False #게임 시작 시, spacebar lock을 위한 변수  
score = 0 

# 시작 화면
def startmsg(msg1, msg2):
    global game_running 
    game_running = True 
    
    msg.clear()
    msg.goto(0,100)
    msg.write(msg1, False, 'center', ("",20))
    msg.goto(0,-100)
    msg.write(msg2,False, 'center', ("",15))
    msg.home()

startmsg('Snake Game','[Space for Start]')

#종료화면
def endmsg():
    global game_running, start_lock, score, over
    game_running = False 
    start_lock = False 
    f.hideturtle()

    over = t.Turtle()
    scr = t.Screen()
    scr.addshape('D:/python_study/python_study/snakegame/img_file/game_over.gif')
    over.shape('D:/python_study/python_study/snakegame/img_file/game_over.gif')
    over.penup()
    over.speed(0)
    over.goto(0,100)
    msg.goto(0,-50)
    msg.write(f'Score:{score}',False,'center',("",20))
    msg.goto(0,-100)
    msg.write('[Space for Restart]',False, 'center', ("",15))
    msg.home()
    

# 먹이 생성 
def feed_init():
    global fx, fy
    fx = random.randint(-240, 240)
    fy = random.randint(-240, 240)
    f.setposition(fx,fy)
    f.showturtle()

#먹이 위치 재배치 
def feed_reset():
    global fx, fy,max_tail_length, score
    f.hideturtle()
    fx = random.randint(-240, 240)
    fy = random.randint(-240, 240)
    f.setposition(fx,fy)
    f.showturtle()
    max_tail_length += 2
    score += 10

positions = []
# 유저 이동 
def move_forward():
    global score
    if not game_running :  #게임 종료 시 정지 
        return 
    
    prev_head_pos = head.pos()
    
    if score<=400:
        speed = 8 - int((score/50)*4)
    else :
        speed = 1

    head.forward(7+int(score/100))
    
    #첫 번째 몸통 이동
    body.setposition(prev_head_pos)
    
    #나머지 꼬리 도장 
    new_stamp = body.stamp()
    body_stamps.append(new_stamp)

    # 오래된 꼬리 제거
    if len(body_stamps) > max_tail_length:
        oldest_stamp = body_stamps.pop(0)  # 가장 오래된 꼬리 제거
        body.clearstamp(oldest_stamp)  # 화면에서 스탬프 삭제

        
    #울타리에 닿으면 게임 종료 
    if head.xcor()>=250 or head.xcor()<=-250 or head.ycor()>=250 or head.ycor()<=-250:
        endmsg()
        return   
    #먹이를 먹을 경우, 먹이 위치 재설정 
    global fx, fy    
    if abs(head.xcor() - fx)<=10 and abs(head.ycor() -fy)<=10:
        feed_reset()
    
    #위치 갱신 
    t.ontimer(move_forward,speed)


# keyboard 입력 설정 
def start():
    global start_lock, game_running, score, max_tail_length,body_stamps,over, prev_head_pos

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
        max_tail_length = 1  # 초기 꼬리 길이
        body.clearstamps()  # 모든 도장 삭제
        body_stamps.clear()
        
        msg.clear()
        body.setposition(0, -20)
        head.setposition(0, 0)
        head.shape(head_images["up"])
        head.setheading(90)
        feed_init()
        move_forward()
        

def r():
    global current_direction
    if game_running and current_direction != "right":
        current_direction = "right"
        head.shape(head_images["right"])
        head.setheading(0)
def u():   
    global current_direction
    if game_running and current_direction != "up":
        current_direction = "up"
        head.shape(head_images["up"])
        head.setheading(90)
def l():
    global current_direction
    if game_running and current_direction != "left":
        current_direction = "left"
        head.shape(head_images["left"])
        head.setheading(180)
def d():
    global current_direction
    if game_running and current_direction != "down":
        current_direction = "down"
        head.shape(head_images["down"])
        head.setheading(270)
    
    
t.onkeypress(r,'Right')
t.onkeypress(l,'Left')
t.onkeypress(d,'Down')
t.onkeypress(u,'Up')
t.onkeypress(start,'space')

        
t.listen()
t.done()