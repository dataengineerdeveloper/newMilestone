from concurrent.futures import thread
import secrets
import threading
import schedule
import time


def job():
    print("estou rodando na thread %s" % threading.currentThread())
    
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
    
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)
schedule.every(10).seconds.do(run_threaded, job)


while 1:
    schedule.run_pending()
    time.sleep(1)