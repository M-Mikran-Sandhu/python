import time as t

time_now=t.localtime()

print("transaction completed at:",str(time_now.tm_hour)+":"+str(time_now.tm_min)+":"+str(time_now.tm_sec))
print(str(time_now.tm_mday)+"-"+str(time_now.tm_mon)+"-"+str(time_now.tm_year))

t.sleep(2)

time_niw=t.time()

delivery_time=time_niw+(86400*7)

#print(t.localtime(delivery_time))

print("Delivery on "+str(time_now.tm_mday)+"-"+str(time_now.tm_mon)+"-"+str(time_now.tm_year))

