import asyncio

from sample_base_asyncio import run_browser

loop = asyncio.get_event_loop()
gather = asyncio.gather(run_browser(1), run_browser(2), run_browser(3))
loop.run_until_complete(gather)
