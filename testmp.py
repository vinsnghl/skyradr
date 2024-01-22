from multiprocessing import Process
from time import sleep
from datetime import datetime
from datetime import timedelta

print('hello from GLOBAL AREA2')


def f(name):
    print('hello from CHILD PROCESS', name , " " , __name__)



aircraft = [1,2,3,4]
processtable = {}
now = datetime.now()
print(now)
sleep(2)
later  = datetime.now()
print(later)
print(later - now)
print(type(later - now))
elapse = later - now
mytimelimit = timedelta(seconds=1)
if elapse > mytimelimit:
    print("ELAPSE IS GREATER")
else:
    print('MYLIMIT IS GREATER')



print('hello from GLOBAL AREA')
if __name__ == '__main__':
    print('hello from __MAIN__ AREA')
    for i in aircraft:
        p = Process(target=f, args=('bob',))
        p.start()
        





    

    