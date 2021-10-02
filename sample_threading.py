from sample_base import run_browser

import time
import threading

for i in range(3):
    thread = threading.Thread(target=run_browser, args=(i,))
    thread.start()
    time.sleep(2)
