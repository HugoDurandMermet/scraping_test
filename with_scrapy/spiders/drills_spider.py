import scrapy

from common import (
    ENDPOINT,
    SLUGS,
    GROUP_TO_SCRAP,
    FEATURES_TO_SCRAP
)


class DrillsSpider(scrapy.Spider):
    """Scrapy spider to run scraping process

    Args:
        scrapy (class): Library module used for scraping

    Yields:
        dict: Data per drill
    """
    name = "drills"
    start_urls = [ENDPOINT + slug for slug in SLUGS]

    def parse(self, response):
        main_document_identifier = '//div[contains(@class, "{}")]'.format(
            GROUP_TO_SCRAP
        )
        drill_group = response.xpath(main_document_identifier)
        for drill in drill_group.css('a'):
            to_yield = {
                'url': drill.attrib['href']
            }

            for feature_name in FEATURES_TO_SCRAP:
                feature_object = FEATURES_TO_SCRAP[feature_name]
                xpath = './/{tag}[contains(@{attribute}, "{string}")]'.format(
                    tag=feature_object['identifier_tag'],
                    attribute=feature_object['identifier_attribute'],
                    string=feature_object['identifier_string']
                )

                if feature_object['value_container'] == 'text':
                    xpath = 'string({})'.format(xpath)
                else:
                    xpath += '/@{}'.format(feature_object['value_container'])

                value = drill.xpath(xpath).get()

                if value:
                    if feature_object['to_strip'] is not None:
                        value = value.strip(feature_object['to_strip'])

                    if feature_object['to_replace'] is not None:
                        original, replacement = feature_object['to_replace']
                        value = value.replace(original, replacement)

                to_yield[feature_name] = value

            yield to_yield
