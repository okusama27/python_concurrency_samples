from sample_base import run_browser

import time
import threading

for i in range(5):
    if threading.active_count() > 3:
        time.sleep(5)
        continue

    thread = threading.Thread(target=run_browser, args=(i,))
    thread.start()
    time.sleep(2)
