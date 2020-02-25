"""This module describes shop's info parser.
Parcer fetches information about shops, forms it into csv format and prints it into console.
";" is used as separator at csv.
 Urls for parsing are provided in setting (shops_urls)."""

from bs4 import BeautifulSoup

from helper_func import get_html
from settings import base_shops_url, shops_urls


class ShopInfo(object):
    """This class defines information that should be fetched about every shop.
    shop_soup is a Beautiful Soup object of shop's info page html.
    my_dict is a Python dictionary, contains pairs mall_name: outlet_id. It is received as a result of get_shop_codes
     function execution. Key is a mall_name and value is a outlet_id.
    Method .print_result() prints csv row in console.
    """

    def __init__(self, shop_soup, my_dict):
        self.shop_soup = shop_soup
        self.mall_name = self.get_mall_name()
        self.outlet_id = self.get_outlet_id(my_dict)
        self.store_name = "5 карманов"
        self.store_phone = self.get_store_phone()
        self.store_adress = self.get_store_adress()

    def get_mall_name(self):
        """This method fetches a shop name, return a str"""
        self.mall_name = self.shop_soup.find("meta", itemprop="name")["content"]
        return self.mall_name

    def get_outlet_id(self, my_dict):
        """This method fetches outlet_id.
        my_dict is a Python dictionary, contains pairs mall_name: outlet_id.
        It is received as a result of get_shop_codes function execution. Key is a mall_name and value is a outlet_id."""
        self.outlet_id = ""
        for key in my_dict.keys():
            if key == self.mall_name:
                self.outlet_id = my_dict[key]
                break
        return self.outlet_id

    def get_store_phone(self):
        """This method fetches a store_phone, return a str"""
        self.store_phone = self.shop_soup.find("meta", itemprop="telephone")["content"]
        return self.store_phone

    def get_store_adress(self):
        """This method fetches a store_adress, return a str"""
        self.store_adress = self.shop_soup.find("meta", itemprop="location")["content"]
        return self.store_adress

    def print_result(self):
        """This method prints information about shop in console as a csv row. ";" is used as a separator."""
        message = f" ;{self.mall_name};{self.outlet_id};{self.store_name};{self.store_phone};{self.store_adress}"
        print(message)


def get_shop_codes(base_url):
    """This function fetches information about outlet_id and shop_name presented at base_url.
    It returns a Python dictionary, contains pairs "store_name":"outlet_id". """
    htms = get_html(base_url)
    shop_soup = BeautifulSoup(htms, "html.parser")
    result = shop_soup.find_all("li", class_="shops-list__item j-info-shop-list-item")
    my_dict = {}
    for i in result:
        id_code = i["data-id"].strip()
        name = i.find("span", class_="name").text.strip()
        my_dict[name] = id_code
    return my_dict


def start_shop_info_parsing(my_dict, shop_urls):
    """This function fetches information about each shop and prints it in console"""
    for url in shops_urls:
        html = get_html(url)
        shop_soup = BeautifulSoup(html, "html.parser")
        shop_info = ShopInfo(shop_soup, my_dict)
        shop_info.print_result()


if __name__ == "__main__":
    outlet_codes = get_shop_codes(base_shops_url)
    start_shop_info_parsing(outlet_codes, shops_urls)
