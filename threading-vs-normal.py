import calcSquare as c
import threadingImpl as t
import time

c_start_time = time.time()
c.calcSquare(1111111)
c.calcSquare(1111111)
c_end_time = time.time()

t_start_time = time.time()
t.runThread(1111111)
t_end_time = time.time()

print(f"Normal execution time for the function twice = {c_end_time-c_start_time:.2f}")
print(f"Execution time for multuthreading and function runs = {t_end_time-t_start_time:.2f}")