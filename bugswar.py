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
start_functions  = []
start_properties = []
import bugs
bugs.addfuncs(start_functions, start_properties)


def draw():
    st = time.time()
    for i in range(len(bugs_list)):
        m.add_point(bugs_list[i].X, bugs_list[i].Y, bugs_list[i].char)

    print(settings.linux_clear_screen, end='')

    print(m.get_map())
    m.reset()
    time.sleep(abs(settings.refresh_delay - (time.time() - st)))


def main():
    print("starting game ...")
    for i in range(len(start_functions)):
        b = bug.Bug(start_properties[i].name, start_properties[i].char, start_properties[i].x, start_properties[i].y)
        bugs_list.append(b)
    
    

    draw()
    
    


if __name__ == "__main__":
    main()
