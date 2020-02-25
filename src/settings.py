"""This module contains information about urls needed to be parsed, logging configurations and shop information that is
add to each json offer. """

import logging

# urls to parse to get offers (json parser)
base_url = "https://5karmanov.ru"
URL_MAN = "https://5karmanov.ru/cat/odezhda-muzhskaya"
URL_MAN_ACCESSORIES = "https://5karmanov.ru/cat/aksessuary-muzhskie"
URL_WOMAN = "https://5karmanov.ru/cat/zhenskaya-kollektsiya"
URL_WOMAN_ACCESSORIES = "https://5karmanov.ru/cat/aksessuary-zhenskie"

sectors_search_url = [URL_WOMAN_ACCESSORIES, URL_WOMAN, URL_MAN_ACCESSORIES, URL_MAN]

# urls to parse to get shop info (cvs parser)
base_shops_url = "https://5karmanov.ru/shops/all"
shops_urls = ["https://5karmanov.ru/shops/all/tula--maksi-",
              "https://5karmanov.ru/shops/all/-moskva--mega--himki",
              "https://5karmanov.ru/shops/all/moskva--iyun-",
              "https://5karmanov.ru/shops/all/volgograd--akvarel-",
              "https://5karmanov.ru/shops/all/krasnodar--mega-",
              "https://5karmanov.ru/shops/all/n-novgorod--fantastika-",
              "https://5karmanov.ru/shops/all/tolyatti--rus-",
              "https://5karmanov.ru/shops/all/staryj-oskol--boshe-",
              "https://5karmanov.ru/shops/all/moskva--oblaka-",
              "https://5karmanov.ru/shops/all/moskva--rio--dmitrovskoe-shosse",
              "https://5karmanov.ru/shops/all/armavir--krasnaya-ploshhad-",
              "https://5karmanov.ru/shops/all/tyumen--kristall-",
              "https://5karmanov.ru/shops/all/yaroslavl--aura-",
              "https://5karmanov.ru/shops/all/tambov--akvarel-",
              "https://5karmanov.ru/shops/all/moskva--kolumbus-",
              "https://5karmanov.ru/shops/all/moskva--vesna-",
              "https://5karmanov.ru/shops/all/taganrog--marmelad-",
              "https://5karmanov.ru/shops/all/moskva--vegas--kashirskoe-sh-",
              "https://5karmanov.ru/shops/all/moskva--vegas--krokus-siti",
              "https://5karmanov.ru/shops/all/n-novgorod--mega-",
              "https://5karmanov.ru/shops/all/rostov-na-donu--vavilon-",
              "https://5karmanov.ru/shops/all/moskva--avenyu--yugo-zapad",
              "https://5karmanov.ru/shops/all/moskva--fashion-house--chernaya-",
              "https://5karmanov.ru/shops/all/yaroslavl--altair-",
              "https://5karmanov.ru/shops/all/rostov-na-donu--mega-",
              "https://5karmanov.ru/shops/all/samara--avrora-",
              "https://5karmanov.ru/shops/all/tyumen--solnechnyj-",
              "https://5karmanov.ru/shops/all/moskva--vegas--kuntsevo",
              "https://5karmanov.ru/shops/all/moskva--xl-1---dmit-shos-",
              "https://5karmanov.ru/shops/all/moskva--xl-3---yaroslav-sh-",
              "https://5karmanov.ru/shops/all/moskva--bum-",
              "https://5karmanov.ru/shops/all/moskva--ladya-",
              "https://5karmanov.ru/shops/all/moskva--krasnyj-kit--mytishhi",
              "https://5karmanov.ru/shops/all/moskva--shhuka-",
              "https://5karmanov.ru/shops/all/volgograd--park-haus-",
              "https://5karmanov.ru/shops/all/ekaterinburg--park-haus-",
              "https://5karmanov.ru/shops/all/ekaterinburg--grinvich-",
              "https://5karmanov.ru/shops/all/kazan--mega-",
              "https://5karmanov.ru/shops/all/kazan--park-haus-",
              "https://5karmanov.ru/shops/all/n-novgorod--respublika-",
              "https://5karmanov.ru/shops/all/tolyatti--aeroholl-",
              "https://5karmanov.ru/shops/all/tolyatti--park-haus-",
              "https://5karmanov.ru/shops/all/tyumen--gudvin-",
              "https://5karmanov.ru/shops/all/chelyabinsk--fokus-",
              "https://5karmanov.ru/shops/all/yaroslavl--vernisazh-",
              "https://5karmanov.ru/shops/all/ivanovo--serebryanyj-gorod-",
              "https://5karmanov.ru/shops/all/kaluga--xxi-vek-",
              "https://5karmanov.ru/shops/all/cheboksary--megamoll-",
              "https://5karmanov.ru/shops/all/moskva--mega--belaya-dacha",
              "https://5karmanov.ru/shops/all/moskva--aviapark-",
              "https://5karmanov.ru/shops/all/moskva--vodnyj-",
              "https://5karmanov.ru/shops/all/volgograd--voroshilovskij-",
              "https://5karmanov.ru/shops/all/moskva--zolotoj-vavilon--rostoki",
              "https://5karmanov.ru/shops/all/sankt-peterburg--mega-parnas-",
              "https://5karmanov.ru/shops/all/rostov-na-donu--gorizont-",
              "https://5karmanov.ru/shops/all/ulyanovsk--akvamoll-",
              "https://5karmanov.ru/shops/all/samara--mega-",
              "https://5karmanov.ru/shops/all/kursk--manezh-",
              "https://5karmanov.ru/shops/all/moskva--horosho-",
              "https://5karmanov.ru/shops/all/sankt-peterburg--mega-dybenko-",
              "https://5karmanov.ru/shops/all/ekaterinburg--mega-",
              "https://5karmanov.ru/shops/all/moskva--zolotoj-vavilon--rostoki",
              "https://5karmanov.ru/shops/all/kaluga--torgovyj-kvartal-",
              "https://5karmanov.ru/shops/all/ivanovo--evrolend-",
              "https://5karmanov.ru/shops/all/moskva--domodedovskij-",
              "https://5karmanov.ru/shops/all/ryazan--premer-",
              "https://5karmanov.ru/shops/all/kazan--koltso-",
              "https://5karmanov.ru/shops/all/volgograd--komsomoll-",
              "https://5karmanov.ru/shops/all/tyumen--sitimoll-",
              "https://5karmanov.ru/shops/all/moskva--ordzhonikidze-",
              "https://5karmanov.ru/shops/all/moskva--kashirskaya-plaza-",
              "https://5karmanov.ru/shops/all/sochi--moremoll-",
              "https://5karmanov.ru/shops/all/moskva--mega--teplyj-stan",
              "https://5karmanov.ru/shops/all/saratov-triumf-moll",
              "https://5karmanov.ru/shops/all/moskva--salaris--",
              "https://5karmanov.ru/shops/all/moskva--autlet-belaya-dacha-",
              "https://5karmanov.ru/shops/all/voronezh--siti-park-grad-",
              "https://5karmanov.ru/shops/all/samara--elrio-",
              "https://5karmanov.ru/shops/all/kazan--tandem-"]

# shop info added to each json offer
SHOP_INFO = {"shop_info": {"url": "https://5karmanov.ru", "company": "5karmanov", "currencies": [["RUR", "1"]],
                           "name": "5karmanov"}}

# formatting logging message
FORMAT = "%(asctime)-8s %(message)s"
logging.basicConfig(level=logging.ERROR, format=FORMAT,
                    filename="errors_logs.log", filemode="w", datefmt="%m/%d/%Y %I:%M:%S %p")
