import pandas as pd

from common import (
    ENDPOINT,
    FEATURES_TO_SCRAP,
    SLUGS
)

from with_beautiful_soup.scraping import (
    get_rows
)

urls = [ENDPOINT + slug for slug in SLUGS]

my_columns = ['url']
my_columns.extend(list(FEATURES_TO_SCRAP.keys()))


def get_csv_file(file_output='drills.csv'):
    """Produce CSV file with Pandas library, using get_rows from scraping.py

    Args:
        file_output (str, optional): Custom filename. Defaults to 'drills.csv'.
    """
    all_rows = []

    for url in urls:
        all_rows.extend(get_rows(url))

    df = pd.DataFrame(all_rows, columns=my_columns)
    df.to_csv(
        file_output,
        encoding='utf-8',
        index=False,
        header=True)