name = "my crazy bug" #your bugs name
char = '@'            #your bugs character
x = 2                 #start point x
y = 4                 #start point y

def start(bug):
    while True:
        if bug.health<= 0 :
            break
        if bug.scan(0):
            bug.shoot(0)
        

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





















