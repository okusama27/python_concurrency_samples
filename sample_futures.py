from sample_base import run_browser

from concurrent import futures
import time

with futures.ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(5):
        future = executor.submit(run_browser, i)
        time.sleep(2)
