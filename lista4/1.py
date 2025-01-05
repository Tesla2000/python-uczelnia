import time

def measure_time(f):
    def wrap(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        print(f'Time elapsed: {time.time() - start} s')
    
    return wrap

@measure_time
def sleep_for(seconds: float):
    time.sleep(seconds)

sleep_for(1)
sleep_for(2)
