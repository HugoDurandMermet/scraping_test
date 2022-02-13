ENDPOINT = "https://www.manomano.fr/perceuse-1146"

SLUGS = ["", "?page=2", "?page=3"]

GROUP_TO_SCRAP = "ListingLayout_products"


FEATURES_TO_SCRAP = {
    'title': {
        'identifier_tag': 'div',
        'identifier_attribute': 'class',
        'identifier_string': 'title',
        'identifier_string_is_a_prefix': True,
        'value_container': 'text',
        'to_strip': None,
        'to_replace': None,
    },
    'current_price': {
        'identifier_tag': 'span',
        'identifier_attribute': 'data-testid',
        'identifier_string': 'price-main',
        'identifier_string_is_a_prefix': False,
        'value_container': 'text',
        'to_strip': None,
        'to_replace': ('€', '.'),
    },
    'average_rating': {
        'identifier_tag': 'span',
        'identifier_attribute': 'class',
        'identifier_string': 'stars',
        'identifier_string_is_a_prefix': True,
        'value_container': 'aria-label',
        'to_strip': '/5',
        'to_replace': None,
    },
    'number_of_ratings': {
        'identifier_tag': 'div',
        'identifier_attribute': 'class',
        'identifier_string': 'ratingsContainer',
        'identifier_string_is_a_prefix': True,
        'value_container': 'text',
        'to_strip': None,
        'to_replace': None,
    },
    'brand': {
        'identifier_tag': 'img',
        'identifier_attribute': 'data-testid',
        'identifier_string': 'brand-image',
        'identifier_string_is_a_prefix': False,
        'value_container': 'alt',
        'to_strip': 'brand image of "',
        'to_replace': None,
    }
}
