import asyncio
from math import atan
import random
from pathlib import Path
import time

from msedge.selenium_tools import Edge, EdgeOptions
from selenium.common.exceptions import (
    ElementNotVisibleException,
    InvalidSelectorException,
    NoSuchElementException,
    InvalidSwitchToTargetException,
    NoSuchAttributeException,
)

EDGE_DRIVER = "msedgedriver.exe"
BASE_URL = "https://kamekokamekame.net"


async def run_browser(num):
    p = Path(".") / EDGE_DRIVER

    # システム側が出すエラーログを消す処理
    options = EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.use_chromium = True

    driver = Edge(options=options, executable_path=p)
    driver.get(BASE_URL)

    for _ in range(10):
        try:
            print(f"{num} - {driver.title}")
            a_tags = driver.find_elements_by_tag_name("a")
            link_no = random.randrange(6, 11)
            for a_tag in a_tags[link_no:]:
                if BASE_URL in a_tag.get_attribute("href"):
                    links = driver.find_elements_by_link_text(a_tag.text)
                    links[0].click()
                    await asyncio.sleep(1)
                    break
        except ElementNotVisibleException:
            print("ElementNotVisibleException")
            continue
        except InvalidSelectorException:
            print("InvalidSelectorException")
            continue
        except InvalidSwitchToTargetException:
            print("InvalidSwitchToTargetException")
            continue
        except NoSuchAttributeException:
            print("NoSuchAttributeException")
            continue
        except NoSuchElementException:
            print("NoSuchElementException")
            continue

    driver.quit()


if __name__ == "__main__":
    run_browser(1)
