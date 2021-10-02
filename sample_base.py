import time
from pathlib import Path
from msedge.selenium_tools import Edge, EdgeOptions

EDGE_DRIVER = "msedgedriver.exe"
BASE_URL = "https://kamekokamekame.net"


def run_browser(num):
    p = Path(".") / EDGE_DRIVER

    # システム側が出すエラーログを消す処理
    options = EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.use_chromium = True

    driver = Edge(options=options, executable_path=p)
    driver.get(BASE_URL)

    for _ in range(10):
        print(f"{num} - {driver.title}")
        a_tags = driver.find_elements_by_tag_name("a")
        for a_tag in a_tags[(6 + num) :]:
            if len(a_tag.get_attribute("href")) > 50:
                links = driver.find_elements_by_link_text(a_tag.text)
                links[0].click()
                break

        time.sleep(1)

    driver.quit()


if __name__ == "__main__":
    run_browser(1)
