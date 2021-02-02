#refresh rate of the game
framerate = 40

#size of the world (characters)(int)
world_width = 20
world_height = 20

#waitings (secconds)(float)
wait_after_move = 0.2
wait_after_shoot= 0.2
wait_after_scan = 0.05

#health (int)
bug_max_health = 100
bullet_decrease_health = 10
collision_decrease_health = 5

#bullets character (str)
bullet_char = '.'

#bullets speed (float)
bullet_speed = 1.0





# !!! don't touch these !!!
refresh_delay = 1.000/framerate
linux_clear_screen = "\033[0;0H"
related_bullet_speed = bullet_speed * 25 / framerate