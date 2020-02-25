"""This module starts a json parser"""

from ulrs_to_parse import get_total_num_pages, create_all_sector_pages
from create_json_offer import get_products_on_pages, ProductPageInfo
from settings import sectors_search_url


def start_sector_parser(sector_url):
    """This func launch parser"""
    sector_pages_qt = get_total_num_pages(sector_url)
    all_sector_pages = create_all_sector_pages(sector_pages_qt, sector_url)
    for url in all_sector_pages:
        page_soup_objects = get_products_on_pages(url)
        for item_soup_object in page_soup_objects:
            data = ProductPageInfo(item_soup_object)
            data.create_offers()


if __name__ == "__main__":
    for sector_url in sectors_search_url:
        start_sector_parser(sector_url)
