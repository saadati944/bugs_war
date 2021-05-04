import prop


# add your bug here
#
# format :
# import bugs.bug1, bugs.bug2, bugs.bug3, ...
# starts_list=[bug1.start, bug2.start, bug3.start, ...]

import bugs.bug1, bugs.bug2
bugs_list=[bug1, bug2]




# don't touch these lines
# |  |  |  |  |  |  |  |
# v  v  v  v  v  v  v  v
def addfuncs(fl, props):
    for i in range(len(bugs_list)):
        fl.append(bugs_list[i].loop)
        props.append(prop.Prop(bugs_list[i].name, bugs_list[i].char, bugs_list[i].x, bugs_list[i].y))
