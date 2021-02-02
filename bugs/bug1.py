name = "my crazy bug" #your bugs name
char = '@'            #your bugs character
x = 5                 #start point x
y = 5                 #start point y

def start(bug):
    while True:
        if bug.health<= 0 :
            break
        bug.health -= 10
        bug.move_down()
        bug.move_left()
        bug.move_up()
        bug.move_right()

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





















