from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


# add your bug here
#
# format :
# import bugs.bug1, bugs.bug2, bugs.bug3, ...
# starts_list=[bug1.start, bug2.start, bug3.start, ...]

import bugs.bug1
starts_list=[bug1.start]



def addfuncs(fl):
    fl+=starts_list