name = "my second crazy bug" #your bugs name
char = '#'            #your bugs character
x = 7                #start point x
y = 4                 #start point y

def start(bug):
    while True:
        if bug.health<= 0:
            break
        if bug.scan(181):
            bug.shoot(181)
        if bug.X<bug.width:
            bug.move_right()


#a bug format :

# name = "my crazy bug" #your bugs name
# char = '@'            #your bugs character
# x = 5                 #start point x
# y = 5                 #start point y
# def start(bug):       #start function
#     while True:
#         if bug.health<= 0:
#             break
#         bug.move_down()
#         bug.move_left()
#         bug.move_up()
#         bug.move_right()





















