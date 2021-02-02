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


def draw():
    global empty_map, bugs_list, bullets_list, m
    for i in range(len(bugs_list)):
        m.add_point(map.Point(bugs_list[i].X,
                              bugs_list[i].Y, bugs_list[i].char))

    print(settings.linux_clear_screen, end='')

    print(m.get_map(settings.world_width, settings.world_height))
    m.reset()
    empty_map = [[0]*settings.world_width]*settings.world_height
    time.sleep(settings.refresh_delay)


def main():
    # test
    bugs_list.append(bug.Bug('bug1', '1', 10, 1))
    bugs_list.append(bug.Bug('bug2', '2', 1, 10))
    bugs_list.append(bug.Bug('bug3', '3', 2, 2))
    bugs_list.append(bug.Bug('bug4', '4', 3, 3))
    draw()

if __name__ == "__main__":
    main()
