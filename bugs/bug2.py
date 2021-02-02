name = "my second crazy bug" #your bugs name
char = '#'            #your bugs character
x = 8                 #start point x
y = 8                 #start point y

def start(bug):
    while True:
        bug.move_down()
        bug.scan(12)
        bug.move_left()
        bug.scan(12)
        bug.move_up()
        bug.scan(12)
        bug.move_right()
        bug.scan(12)

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





















