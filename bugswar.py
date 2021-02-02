import os
import bug
import time
import bullet
import settings
import threading

import map

IsLinux = os.name != "nt"
Time = 0

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
    global Time, calculate_time
    for i in range(len(bugs_list)):
        if bugs_list[i] == False:
            continue
        if bugs_list[i].health<=0:
            b = bugs_list[i]
            bugs_list[i] = False
            del b
    for i in range(len(bugs_list)):
        if bugs_list[i] == False:
            continue
        m.add_point(bugs_list[i].X, bugs_list[i].Y, bugs_list[i].char)
    for i in range(len(bullets_list)):
        if bullets_list[i] == False:
            continue
        p = bullets_list[i].calculatePos(Time)
        if p[0]<0 or p[0]>=settings.world_width or p[1]<0 or p[1]>=settings.world_height:
            bullets_list[i] = False
            continue
        for j in range(len(bugs_list)):
            if bugs_list[j] == False:
                continue
            if bugs_list[j].X==p[0] and bugs_list[j].Y==p[1] and bugs_list[j] != p[2]:
                bugs_list[j].health -= settings.bullet_decrease_health
                bullets_list[i] = False
                break
        m.add_point(p[0], p[1], settings.bullet_char)

    if IsLinux:
        print(settings.linux_clear_screen, end='')
    else:
        _=os.system("cls")
        
    print(m.get_map())
    for b in bugs_list:
        if b == False:
            continue
        print(b.name, ":", b.health, '                  ')
    print('                                   ')
    m.reset()
    time.sleep(abs(settings.refresh_delay - (time.time() - calculate_time)))


def create_bullet(x, y, deg, shooter):
    global Time, bullets_list
    bullets_list.append(bullet.Bullet(x, y, deg, Time, shooter))

def start_game():
    global Time, calculate_time
    while True:
        draw()
        calculate_time = time.time()
        Time += 1
        bc = 0
        for b in bugs_list:
            if b==False:
                continue
            bc += 1
            if bc >= 2:
                bc = -1
                break
        if bc != -1:
            for b in bugs_list:
                if b != False:
                    b.health = 0
                    input(f"\n\nthe winner is : {b.name} ({b.char})\npress enter to exit ...")
                    os.sys.exit()
            break

def main():
    global Time

    if IsLinux:
        _=os.system("clear")
    else:
        _=os.system("cls")
    
    for i in range(len(start_functions)):
        b = bug.Bug(start_properties[i].name, start_properties[i].char, start_properties[i].x, start_properties[i].y, create_bullet, bugs_list)
        bugs_list.append(b)
    
    for i in range(len(start_functions)):
        t = threading.Thread(target=start_functions[i], args=(bugs_list[i],))
        threads.append(t)
        t.start()
    
    # for t in threads:
    #     t.join()
    
    # while True:
    #     draw()
    #     Time += 1

    starter = threading.Thread(target=start_game)
    starter.start()
    for t in threads:
        t.join()
    starter.join()

    draw()
    
    


if __name__ == "__main__":
    main()
