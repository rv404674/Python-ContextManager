This Repo is created to understand the meaning of context Managers in python by writing some code.

System Resources - files, locks, connections.
'with' statement simplies dealing with the acquisition and realising with these resources.

Eg.
some_lock = threading.Lock()

# Harmful:
some_lock.acquire()
try:
    # Do something...
finally:
    some_lock.release()

# Better:
with some_lock:
    # Do something...
