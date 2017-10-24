#!/usr/bin/env python3
import dbModules
import datetime


def error_day_percentage(data):
    """ Print all the days that have more than 1% of fail
    requests """
    for row in data:
        print('* {0:%B %d, %Y} - {1:.2f}% error'.format(row[0], row[1]))


def popular_three_articles(data):
    """ Print the three articles with more views """
    for row in data:
        print("*", row[0], "-", row[1], "views")


def popular_authors(data):
    """ Print all the authors and their views"""
    for row in (data):
        print("*", row[0], "-", row[1], "views")

if __name__ == '__main__':
    print("What are the most popular three articles of all time?")
    print()
    data = dbModules.get_articles_views()
    popular_three_articles(data)
    print()
    print("Who are the most popular article authors of all time?")
    print()
    data = dbModules.get_authors_views()
    popular_authors(data)
    print()
    print("On which days did more than 1% of requests lead to errors?")
    print()
    data = dbModules.get_error_count()
    error_day_percentage(data)
