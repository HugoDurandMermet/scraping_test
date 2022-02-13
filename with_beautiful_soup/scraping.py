from bs4 import BeautifulSoup
import urllib.request

from common import (
    FEATURES_TO_SCRAP,
    GROUP_TO_SCRAP
)


def get_rows(url):
    """Retrieve features data for each product and returns them
    as a list of rows, to be processed in a dataframe.

    Args:
        url (str): Link of the page to be scraped

    Returns:
        list: A list of list, containing all datas retrieved on the url
    """
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, 'lxml')
    drill_group = soup.find_all(
            "div",
            class_=lambda value: value and value.startswith(GROUP_TO_SCRAP)
        )[0]

    rows = []

    for a in drill_group.find_all('a', href=True, recursive=False):
        row = []
        row.append(a['href'])
        for name in FEATURES_TO_SCRAP:
            feature = FEATURES_TO_SCRAP[name]
            if feature['identifier_attribute'] == 'class':
                if feature['identifier_string_is_a_prefix']:
                    response = a.find_all(
                        feature['identifier_tag'],
                        class_=lambda value: value and value.startswith(
                                feature["identifier_string"]
                            )
                        )
                else:
                    response = a.find_all(
                        feature['identifier_tag'],
                        class_=feature["identifier_string"]
                    )
            else:
                response = a.find_all(
                    feature['identifier_tag'],
                    attrs={
                        feature['identifier_attribute']:
                        feature["identifier_string"]
                    }
                )

            if response:
                element = response[0]
                if feature['value_container'] == 'text':
                    value = element.text
                else:
                    value = element[feature['value_container']]

                if feature['to_strip'] is not None:
                    value = value.strip(feature['to_strip'])

                if feature['to_replace'] is not None:
                    original, replacement = feature['to_replace']
                    value = value.replace(original, replacement)

                row.append(value)

            else:
                row.append(None)

        rows.append(row)

    return rows
