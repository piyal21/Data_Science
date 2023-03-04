import time
t1 = time.time()



s= 0
for i in range(0,10 ):
    s = s+1
    
print("sum is : ", s)
t2= time.time()

print(t2-t1)