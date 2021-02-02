import os
import bug
import time
import bullet
import settings
import threading

import map

IsLinux = os.name != "nt"


m = map.Map()

# bugs in the world
bullets_list = []
bugs_list = []

threads = []

start_functions  = []
start_properties = []

import bugs
bugs.addfuncs(start_functions, start_properties)


calculate_time = time.time()

def draw():
    for i in range(len(bugs_list)):
        if bugs_list[i] == False:
            continue
        m.add_point(bugs_list[i].X, bugs_list[i].Y, bugs_list[i].char)

    print(settings.linux_clear_screen, end='')

    print(m.get_map())
    for b in bugs_list:
        if b == False:
            continue
        print(b.name, ":", b.health, '                  ')
    print('                                   ')
    m.reset()
    time.sleep(abs(settings.refresh_delay - (time.time() - calculate_time)))


def check_stats():
    global calculate_time
    calculate_time = time.time()
    for i in range(len(bugs_list)):
        if bugs_list[i] == False:
            continue
        if bugs_list[i].health<=0:
            b = bugs_list[i]
            bugs_list[i] = False
            del b
        



def main():
    print("starting game ...")
    for i in range(len(start_functions)):
        b = bug.Bug(start_properties[i].name, start_properties[i].char, start_properties[i].x, start_properties[i].y)
        bugs_list.append(b)
    
    for i in range(len(start_functions)):
        t = threading.Thread(target=start_functions[i], args=(bugs_list[i],))
        threads.append(t)
        t.start()
    
    # for t in threads:
    #     t.join()
    
    while True:
        check_stats()
        draw()
        

    draw()
    
    


if __name__ == "__main__":
    main()
