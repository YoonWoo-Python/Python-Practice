from time import *

s = 0
m = 0
h = 0

while True:
    s += 1
    print(h,"시간",m,"분",s,"초 경과")
    sleep(1)
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
        s = 0