from sample_base import run_browser

from concurrent import futures
import time

with futures.ThreadPoolExecutor() as executor:
    for i in range(3):
        future = executor.submit(run_browser, i)
        time.sleep(2)
