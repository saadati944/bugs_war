name = "sniper" #your bugs name
char = 'O'            #your bugs character
x = 2                 #start point x
y = 4                 #start point y



deg=0

def start(bug):
    global deg
    while True:
        if bug.health<= 0 :
            break
        if bug.X>0:
            bug.move_left()
        if bug.Y>0:
            bug.move_up()
        if bug.scan(deg):
            bug.shoot(deg)
        deg -=10
        if deg < -90:
            deg = 0
        

#a bug format :

# name = "my crazy bug" #your bugs name
# char = '@'            #your bugs character
# x = 5                 #start point x
# y = 5                 #start point y
# def start(bug):       #start function
#     while True:
#         bug.move_down()
#         bug.move_left()
#         bug.move_up()
#         bug.move_right()





















