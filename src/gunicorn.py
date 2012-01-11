import os
 
def numCPUs():
    if not hasattr(os, "sysconf"):
       raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")
 
bind = "127.0.0.1:3034"
workers = 3 #numCPUs() * 2 + 1
backlog = 2048
worker_class =  "gevent"
logfile ="~/logs/gunicorn.log"