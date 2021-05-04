name = "circle" #your bugs name
char = '@'            #your bugs character
x = 15                #start point x
y = 15                 #start point y


dir = 0
def loop(bug):
    global dir
    if dir == 0:
        if bug.X<15:
            bug.move_right()
            bug.shoot(0)
        else:
            dir = 1
    elif dir == 1:
        if bug.Y<15:
            bug.move_down()
            bug.shoot(-90)
        else:
            dir = 2
    elif dir == 2:
        if bug.X>5:
            bug.move_left()
            bug.shoot(181)
        else:
            dir = 3
    elif dir == 3:
        if bug.Y>5:
            bug.move_up()
            bug.shoot(90)
        else:
            dir = 0



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

