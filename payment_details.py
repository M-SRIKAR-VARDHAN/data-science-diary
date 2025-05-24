import os ,sys
from os.path import dirname,join,abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from courses import course_details

def pay():
    print("i am pay")

course_details.course()