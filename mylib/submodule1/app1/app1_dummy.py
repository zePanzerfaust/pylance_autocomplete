import time
from mylib.util import export


@export
def get_app1_dummy_1():
    """
    """
    return "get_app1_dummy_1"


@export
def execute_stuff():
    """
    """
    time.sleep(1)
    return True
