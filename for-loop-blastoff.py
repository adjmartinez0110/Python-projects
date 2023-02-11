#we will use the for loop to create a countdown before a rocket blasts off
import time

print("Rocket launching in...")

for i in range(10,0,-1):
  print(i)
  time.sleep(2)

print("Blast off!")