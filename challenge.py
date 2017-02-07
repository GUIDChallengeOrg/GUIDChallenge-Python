import uuid
import time

start = time.time()

for i in range(0, 10000000):
  uuid.uuid4()
  
end = time.time()

print("Done in %.3fs" % (end-start))
