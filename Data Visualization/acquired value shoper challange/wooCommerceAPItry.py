# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:49:27 2020

@author: outsi
"""

from woocommerce import API

wcapi = API(
    url="http://localhost/wordpress/",
    consumer_key="ck_2e3ee2d3e4deefebf0a93f489548dae9e7a66ede",
    consumer_secret="cs_898be151ada68820a78521f46b5aaf0f14f9a80e",
    wp_api=True,
    version="wc/v3"
)

print(wcapi.get("").json())
order=wcapi.get("oreder").json()