import random
import string
from datetime import datetime


def getRandomString(length):
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    return x


def getFileNameDateTime(prefix: str):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    return prefix + "-" + dt_string
