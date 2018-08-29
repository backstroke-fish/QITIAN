from test_GIL import *
import time

t = time.time()
for i in range(10):
    count(1, 1)
print("line CPU:", time.time() - t)