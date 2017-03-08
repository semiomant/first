from datetime import datetime


def datetest():
    now = datetime.now()
    str = "Time: {now.hour}:{now.minute} Date: {now.day}.{now.month}".format(**vars())
    print(str)
    print(now.ctime())


datetest()
