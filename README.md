# Bugs War

Control your bug with writing codes

# Create your own

1. Create a new file in `bugs` folder with `.py` extension and with this structure :
    ```python
    name = "sniper"
    char = '@'
    #starting point for the bug
    x = 15
    y = 3
    
    # this is the main loop and will be invoked repeatedly
    def loop(bug):
        #write your codes here
        #|  |  |  |
        #v  v  v  v

        #۸  ۸  ۸  ۸
        #|  |  |  |
    ```
1. Add your bug in this file `bugs/__init__.py`
    ```python
    import bugs.bug1, bugs.bug2, bugs.YourBugName, ...
    bugs_list=[bug1, bug2, YourBugName, ...]
    ```
1. Start the program and see how your bug kills other bugs
    ```bash
    python bugswar.py
    ```

# Coding a bug

In the loop function of your bugs code file, you will get a bug object that has these properties :

- `bug.move_right()`
- `bug.move_left()`
- `bug.move_up()`
- `bug.move_down()`
- `bug.scan(deg)`  #returns a boolean
- `bug.shoot(deg)`

Bugs health
- `bug.health`

Position of the bug (zero indexed):
- `bug.X`
- `bug.Y`

World size:
- `bug.width`
- `bug.height`

Each operation takes some time to complete, so using less operations can be an advantage