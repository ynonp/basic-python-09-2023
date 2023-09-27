import sys
import shutil

me = sys.argv[0]
for arg in sys.argv[1:]:
    shutil.copy(me, arg)
