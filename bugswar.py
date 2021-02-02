import os
import bug
import time
import bullet
import settings
import threading

from bugs import *
import map

IsLinux = os.name != "nt"


m = map.Map()

# bugs in the world
bullets_list = []
bugs_list = []


def draw():
    st = time.time()
    for i in range(len(bugs_list)):
        m.add_point(bugs_list[i].X, bugs_list[i].Y, bugs_list[i].char)

    print(settings.linux_clear_screen, end='')

    print(m.get_map())
    m.reset()
    time.sleep(abs(settings.refresh_delay - (time.time() - st)))


def main():
    # test
    bugs_list.append(bug.Bug('bug1', '1', 19, 1))
    bugs_list.append(bug.Bug('bug2', '2', 1, 9))
    bugs_list.append(bug.Bug('bug3', '3', 2, 2))
    bugs_list.append(bug.Bug('bug4', '4', 3, 3))
    draw()
    
    


if __name__ == "__main__":
    main()
