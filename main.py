import argparse
import time

from with_beautiful_soup.get_csv import (
    get_csv_file
)
from with_scrapy.spiders.drills_spider import DrillsSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Scrape the first three pages of ManoMano Drills'
    )
    parser.add_argument(
        "--lib",
        type=str,
        required=True,
        help="(str) Options [ BeautifulSoup, Scrapy ]"
    )

    parser.add_argument(
        "--output",
        type=str,
        help="(str) Custom name for the CSV file (default: drills)"
    )

    args = parser.parse_args()

    lib_choice = args.lib.lower()

    start_time = time.time()

    if lib_choice == 'beautifulsoup':
        if args.output:
            filename = args.output + '.csv'
            get_csv_file(filename)
        else:
            get_csv_file()

        runtime = round(time.time() - start_time, 2)
        print("CSV file exported")
        print("Script with Beautiful Soup executed in: {}s".format(runtime))

    elif lib_choice == 'scrapy':
        process = CrawlerProcess(get_project_settings())

        if args.output:
            filename = args.output + '.csv'
            process.settings.set('FEED_URI', filename, priority='cmdline')

        process.crawl(DrillsSpider)
        process.start()

        runtime = round(time.time() - start_time, 2)
        print("CSV file exported")
        print("Script with Scrapy executed in: {}s".format(runtime))

    else:
        print("Unknown command")
