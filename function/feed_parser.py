#!/usr/bin/python
#-*- coding: utf-8 -*-

import feedparser


def get_news_from_bankir(feed):
    parse_bankir = feedparser.parse(feed)
    result = []
    for i in range(4):
        message = parse_bankir.entries[i].link
        result.append(message)
    return result