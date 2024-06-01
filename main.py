import turtle as t
import random
import time
delay=0.2
score=0
high_score=0
s = t.Screen()
s.title("Snake Game")
s.bgcolor("green")
s.setup(width=600, height=600)
# head of the snake
head=t.Turtle()
head.width(40)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "Stop"

#food
food = t.Turtle()
food.speed(0)
colors=random.choice(['black', 'magenta', 'cyan', 'yellow', 'orange'])
shapes=random.choice(['turtle', 'circle',])
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280,280))

#scoreboard
sb = t.Turtle()
sb.speed(0)
sb.penup()
sb.goto(0,260)
sb.pendown()
sb.write("Score: 0,High Score : 0", font = (None, 24), align = "center")
sb.hideturtle()

#key directions
def up():
    if head.direction != 'down':
        head.direction='up'
def down():
    if head.direction != 'up':
        head.direction='down'
def left():
    if head.direction != 'right':
        head.direction='left'
def right():
    if head.direction != 'left':
        head.direction='right'
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
s.listen()
s.onkeypress(up, 'Up')
s.onkeypress(down, 'Down')
s.onkeypress(right, 'Right')
s.onkeypress(left, 'Left')
segments=[]
while True:
  s.update()
  if head.xcor()>300 or head.xcor()<-300 or head.ycor() > 300 or head.ycor()<-300:
    time.sleep(1)
    head.goto(0,0)
    head.direction="Stop"
    colors=random.choice(['black','magenta','cyan','yellow','orange'])
    shapes=random.choice(['turtle', 'circle',])
    for segment in segments:
        segment.goto(1000,1000)
    segments.clear()
    score = 0
    delay = 0.1
    sb.clear()
    sb.write("Score: {},High Score : {}".format(score, high_score),
             align="center", font=("candara", 24, "bold"))
  if head.distance(food) < 20:
    x=random.randint(-300, 300)
    y=random.randint(-300, 300)
    food.goto(x,y)
    # Adding segment
    new_segment = t.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("red")
    new_segment.penup()
    segments.append(new_segment)
    delay = 0.1
    score += 1
    if score> high_score: 
      high_score=score
    sb.clear()
    sb.write("Score: {},High Score : {}".format(score, high_score),
             align="center", font=("candara", 24, "bold", ))
  for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)
  if len (segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)
  move()
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction="Stop"
      colors=random.choice(['black','magenta','cyan','yellow','orange'])
      shapes=random.choice(['turtle', 'circle',])
      for segment in segments:
          segment.goto(1000,1000)
      segments.clear()
      score = 0
      delay = 0.1
      sb.clear()
      sb.write("Score: {},High Score : {}".format(score, high_score),
               align="center", font=("candara", 24, "bold"))
  time.sleep(delay)
  
t.done()
