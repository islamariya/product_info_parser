""""This modules creates list of all urls needed to be parsed in each sector"""

from bs4 import BeautifulSoup
from validators import url as url_validator

from helper_func import get_html
from settings import logging


def get_total_num_pages(sector_url):
    """This func gets a total number of pages to parse in each sector.
    sector_url is a link from list sectors_search_url presented in settings.py
    For example,  https://5karmanov.ru/cat/aksessuary-muzhskie
    It is need to created a sector page url via create_sector_page_url
    (for example, https://5karmanov.ru/cat/aksessuary-muzhskie?&page=3)
    :return sector_pages_qt int
    """
    sector_page_html = get_html(sector_url)
    if sector_page_html:
        soup = BeautifulSoup(sector_page_html, "html.parser")
        try:
            last_page_url = soup.find("ul", class_="pagination").find_next("li", class_="more").find_next('a')["href"]
        except AttributeError:
            last_page_url = soup.find("ul", class_="pagination").find_all("a")
            last_page_url = last_page_url[-2]["href"]
        sector_pages_qt = last_page_url.partition("page=")[-1].strip('"')
        try:
            int(sector_pages_qt)
        except ValueError as e:
            logging.exception(f"Fail to get page_num at {sector_url}.Received data is not integer {e}")
            print("Не удалось загрузить секцию", sector_url)
        return int(sector_pages_qt)
    else:
        logging.exception(f"Failed to get {sector_url} html")
        print("Не удалось загрузить секцию", sector_url)


def create_sector_page_url(sector_url, page_number):
    """This func creates a url for single page in each sector.
    https://5karmanov.ru/cat/aksessuary-muzhskie?&page=5
    sector_url: str, url of a sector (presented in sectors_search_url in settings.py)
    page_number: int, serial number of page (received via get_total_num_pages)
    """
    sector_page_url = sector_url + "?&page=" + str(page_number)
    if url_validator(sector_page_url):
        return sector_page_url
    else:
        logging.exception("Ошибка формирования ссылки страницы галереи товаров секции")


def create_all_sector_pages(sector_pages_qt, sector_url):
    """This func creates all urls in sector.
    :return list of sector's page url (like https://5karmanov.ru/cat/aksessuary-muzhskie?&page=5)"""
    all_pages = [create_sector_page_url(sector_url, page_number) for page_number in range(1, sector_pages_qt + 1) if page_number is not None]
    return all_pages
