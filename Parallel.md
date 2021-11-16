# Parallel Processing
# Thread
<pre>
import time
import _thread

def thread_test(name, wait):
   i = 0
   while i <= 3:
      time.sleep(wait)
      print("Running %s\n" %name)
      i = i + 1

   print("%s has finished execution" %name)

if __name__ == "__main__":
    _thread.start_new_thread(thread_test, ("First Thread", 1))
    _thread.start_new_thread(thread_test, ("Second Thread", 2))
    _thread.start_new_thread(thread_test, ("Third Thread", 3))
</pre>
<pre>
import threading

if __name__=="__main__":
    thread_one = threading.Thread(target=thread_test, args=("First Thread", 1))
</pre>
# Thread Class which extends the Thread class and overrides it’s run() method.
<pre>
import time
import threading

class threadtester (threading.Thread):
    def __init__(self, id, name, i):
       threading.Thread.__init__(self)
       self.id = id
       self.name = name
       self.i = i
       
    def run(self):
       thread_test(self.name, self.i, 5)
       print ("%s has finished execution " %self.name)

def thread_test(name, wait, i):

    while i:
       time.sleep(wait)
       print ("Running %s \n" %name)
       i = i - 1

if __name__=="__main__":
    thread1 = threadtester(1, "First Thread", 1)
    thread2 = threadtester(2, "Second Thread", 2)
    thread3 = threadtester(3, "Third Thread", 3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
</pre>
## Synchronizing threads
<pre>
import threading
lock = threading.Lock()

def first_function():
    for i in range(5):
        <b>lock.acquire()</b>
        print ('lock acquired')
        print ('Executing the first funcion')
        <b>lock.release()</b>
</pre>

## Producer / Consumer using Queue
<pre>
from threading import Thread
from Queue import Queue
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

q = Queue()
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

for item in source():
    q.put(item)

q.join()       # block until all tasks are done
</pre>
