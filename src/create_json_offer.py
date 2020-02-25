"""This module parses html and create product's offer for each size.  """

import json

from bs4 import BeautifulSoup
from validators import url as url_validator

from helper_func import get_html
from settings import SHOP_INFO, base_url


class SectorPageInfo(object):
    """This class represents product's information that can be parsed from sector page."""
    def __init__(self, item_soup_object):
        self.product_name = self.get_product_name(item_soup_object)
        self.product_url = self.get_product_url(item_soup_object)
        self.product_price = self.get_product_price(item_soup_object)
        self.product_old_price = self.get_product_oldprice(item_soup_object)
        self.sizes = self.get_sizes(item_soup_object)
        self.is_product_new = self.is_product_new(item_soup_object)
        self.product_page_soup = self.get_product_page_soup()

    def get_product_name(self, item_soup_object):
        """This method gets a product name
        item_soup_object is a Beautiful Soup object related to 1 product
        returns str"""
        self.product_name = item_soup_object.find("meta", itemprop="name")["content"]
        return self.product_name

    def get_product_url(self, item_soup_object):
        """This method creates an absolute product url.
        item_soup_object is a Beautiful Soup object related to 1 product
        returns str"""
        search_result = item_soup_object.find("a", class_="title-link")["href"]
        self.product_url = base_url + str(search_result)
        # self.product_url = "https://5karmanov.ru" + str(search_result)
        if url_validator(self.product_url):
            return self.product_url

    def get_product_price(self, item_soup_object):
        """This method gets a product price.
        item_soup_object is a Beautiful Soup object related to 1 product
        returns str"""
        self.product_price = item_soup_object.find("span", class_="price").text.strip(" Р")
        return self.product_price

    def get_product_oldprice(self, item_soup_object):
        """This method gets a product old price if it is presented at page.
        item_soup_object is a Beautiful Soup object related to 1 product
        returns str or 0 in case there is no old price"""
        result = item_soup_object.find("span", class_="old-price")
        self.product_old_price = result.text.strip(" Р") if result is not None else 0
        return self.product_old_price

    def get_sizes(self, item_soup_object):
        """This method gets all sizes available for each product. If there is no size, "One Size" is returned.
        Size is available if it is possible to add it to basket (even if it is called "нетXS"). Each size is a str.
        item_soup_object is a Beautiful Soup object related to 1 product
        returns a list of sizes
        """
        result = item_soup_object.find_all("label")
        self.sizes_available = [size.text for size in result]
        self.sizes_available = ["One Size"] if not result else self.sizes_available
        return self.sizes_available

    def is_product_new(self, item_soup_object):
        """This method evaluates if there is a "new product" badge.
        For these purposes New product badge is a span text with class "info-text bg-blue" at sector page.
        item_soup_object is a Beautiful Soup object related to 1 product
        returns a bool
        """
        search_result = item_soup_object.find("span", class_="info-text bg-blue")
        self.is_product_new = True if search_result is not None else False
        return self.is_product_new

    def get_product_page_soup(self):
        """This method open product page url and returns a Beautiful soup object"""
        product_page_html = get_html(self.product_url)
        self.product_page_soup = BeautifulSoup(product_page_html, "html.parser")
        return self.product_page_soup


class ProductPageInfo(SectorPageInfo):
    """This class represents product's information that can be parsed from product page."""
    def __init__(self, item_soup_object):
        super().__init__(item_soup_object)
        self.available = self.is_product_available()
        self.pictures = self.get_product_picture()
        self.vendor_code = self.get_product_vendor_code()
        self.vendor = self.get_vendor_info()
        self.description = self.get_description()
        self.categories = self.get_product_categories()
        self.parameters = self.get_params()
        self.shop_info = SHOP_INFO

    def is_product_available(self):
        """This method checks if product is available to order online. If product is selling only in retail store it
        returns false.
        return str "true" or "false"
        """
        result = self.product_page_soup.find("div", class_="product-availability")
        is_available = "true" if result else "false"
        return is_available

    def get_product_picture(self):
        """This method fetched product pictures' uls presented on the product page.
        returns a list of str (urls)"""
        pic_found = self.product_page_soup.find_all('img', itemprop='image')
        picture_list = [img_link.get('src') for img_link in pic_found]
        return picture_list

    def get_product_vendor_code(self):
        """This method gets a product code
        returns a str """
        vendor_code = self.product_page_soup.find("meta", itemprop="sku")["content"]
        return vendor_code

    def get_vendor_info(self):
        """This method gets a vendor name. If it's misiing returns a shop name
        returns a str"""
        result = self.product_page_soup.find("a", itemprop="brand").text
        vendor = "5 карманов" if result == None else result
        return vendor

    def get_product_categories(self):
        """This method gets a bread crumbs of categories not including main page and product page.
         returns a list like ["Мужская коллекция", "Мужская одежда", "Мужские шорты"] """
        result = self.product_page_soup.find_all("a", class_="headerNavigation")
        product_categories = [item.text for item in result]
        return product_categories[1:-1]

    def get_description(self):
        """This method gets a product description if it is presented on page.
        returns a str or None if missing """
        result = self.product_page_soup.find("div", itemprop="description").find('div')
        self.description = result.text.strip() if result else None
        return self.description

    def get_params(self):
        """This method creates a python dictionary with parameters, presented on product page (like color, season,
        etc) and some mandatory params like "новинка", "Взрослый",  "Женский". """
        result = self.product_page_soup.find("div", itemprop="description").find_all('span', class_='name')
        keys = [param.text.strip() for param in result]
        values_result = self.product_page_soup.find('div', itemprop="description").find_all('span', class_='value')
        values = [value.text.strip() for value in values_result]
        self.parameters = dict(zip(keys, values))
        self.parameters["Новинка"] = 1 if self.is_product_new else 0
        # if self.is_product_new:
        #     self.parameters["Новинка"] = 1
        self.parameters["Возраст"] = "Взрослый"
        self.parameters["Пол"]="Женский" if self.categories[0].lower() == "женская коллекция" else "Мужской"
        return self.parameters

    def create_offers(self):
        """This method creates a product offer for every available size of product as json and print each offer to
        console.
        returns none """
        for size in self.sizes:
            offer = {}
            offer["available"] = self.available
            offer["picture"] = self.pictures
            offer["vendorCode"] = self.vendor_code
            offer["vendor"] = self.vendor
            offer["name"] = self.product_name
            offer["url"] = self.product_url
            offer["price"] = self.product_price
            if self.product_old_price:
                offer["oldprice"] = self.product_old_price
            if self.description:
                offer["description"] = self.description
            offer["param"] = self.parameters
            offer["param"]["Размер"] = size
            offer["currencyId"] = "RUR"
            offer["categories"] = self.categories
            offer_full = [self.shop_info, offer]
            offer_json = json.dumps(offer_full, ensure_ascii=False)
            print(offer_json)


def get_products_on_pages(url):
    """Gets a soup objects with all products on page"""
    page_html = get_html(url)
    if page_html:
        soup = BeautifulSoup(page_html, "html.parser")
        all_products = soup.find_all("div", itemprop="itemListElement")
    return all_products
