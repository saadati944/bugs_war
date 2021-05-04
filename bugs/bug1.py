name = "sniper"       #bug name
char = 'O'            #bug character
x = 2                 #start point x
y = 4                 #start point y


deg=0

def loop(bug):
    global deg
    if bug.X>0:
        bug.move_left()
    if bug.Y>0:
        bug.move_up()
    if bug.scan(deg):
        bug.shoot(deg)
    deg -=10
    if deg < -90:
        deg = 0
        

# bug format :

# name = "my crazy bug"
# char = '@'
# x = 5
# y = 5
# def loop(bug):
#     bug.move_down()
#     bug.move_left()
#     bug.move_up()
#     bug.move_right()

