import pgzrun
import random
WIDTH=1000
HEIGHT=580

basket=Actor('basket')
ball=Actor('basketball')
ball.x=random.randint(50,WIDTH-50)
ball.y=0
basket.x=WIDTH/2
basket.y=HEIGHT-50
ballspeed=5
gameover=False
score=0

def draw():
    if not gameover:
        screen.blit('court',(0,0))
        basket.draw()
        ball.draw()
        screen.draw.text(f"Score:{score}",center=(WIDTH/10,10),fontsize=35,color='white')
    else:
        screen.blit('game_over',(0,0))
        screen.draw.text(f"Your final score is {score}",center=(WIDTH/2,20),fontsize=35,color='white')

def timeup():
    global gameover
    gameover=True

def update():
    global score
    ball.y+=ballspeed
    if not gameover:
        if keyboard.D and basket.right<WIDTH:
            basket.x=basket.x+10
        elif keyboard.A and basket.left>0:
            basket.x=basket.x-10
        if ball.colliderect(basket):
            score=score+1
            ball.x=random.randint(50,WIDTH-50)
            ball.y=0
        if ball.y==580:
            ball.x=random.randint(50,WIDTH-50)
            ball.y=0
clock.schedule(timeup,60)
pgzrun.go()
