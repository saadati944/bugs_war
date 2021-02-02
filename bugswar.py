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
start_functions = []
import bugs
bugs.addfuncs(start_functions)


def draw():
    st = time.time()
    for i in range(len(bugs_list)):
        m.add_point(bugs_list[i].X, bugs_list[i].Y, bugs_list[i].char)

    print(settings.linux_clear_screen, end='')

    print(m.get_map())
    m.reset()
    time.sleep(abs(settings.refresh_delay - (time.time() - st)))


def main():
    print("test")
    for f in start_functions:
        f("hello world")
    
    


if __name__ == "__main__":
    main()
