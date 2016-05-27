#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016-5-26

@author: hustcc
'''

from datetime import datetime
from timeago.setting import SECONDS, MINUTE_SECONDS, HOUR_SECONDS, DAY_SECONDS, MONTH_SECONDS, YEAR_SECONDS
from timeago.locales import timeago_template
from timeago.excepts import ParameterUnvalid

__version__ = '1.0.2'
__license__ = 'MIT'
__ALL__ = ['format']


def format(date, now=None, locale='en'):
    '''
    the entry method
    '''
    if now is None:
        now = datetime.now()

    if type(date) != datetime or type(now) != datetime:
        raise ParameterUnvalid('the 1st, 2st parameter show be type of datetime.')

    # the gap sec
    diff_seconds = (now - date).total_seconds()

    # is ago or in
    ago_in = 0
    if diff_seconds < 0:
        ago_in = 1  # date is later then now, is the time in future
        diff_seconds *= -1  # chango to positive

    # less then SECONDS
    if(diff_seconds < SECONDS):
        return timeago_template('JUST_NOW', locale, ago_in)

    # seconds ago
    if(diff_seconds < MINUTE_SECONDS):
        return timeago_template('SECOND_AGO', locale, ago_in) % (int(diff_seconds))

    # a minute ago
    if(diff_seconds < MINUTE_SECONDS * 2):
        return timeago_template('A_MINUTE_AGO', locale, ago_in)

    # minutes ago
    if(diff_seconds < HOUR_SECONDS):
        return timeago_template('MINUTES_AGO', locale, ago_in) % (int(diff_seconds / MINUTE_SECONDS))

    # an hour ago
    if(diff_seconds < HOUR_SECONDS * 2):
        return timeago_template('AN_HOUR_AGO', locale, ago_in)

    # hours ago
    if(diff_seconds < HOUR_SECONDS * 24):
        return timeago_template('HOURS_AGO', locale, ago_in) % (int(diff_seconds / HOUR_SECONDS))

    # a day ago
    if(diff_seconds < DAY_SECONDS * 2):
        return timeago_template('A_DAY_AGO', locale, ago_in)

    # days ago
    if(diff_seconds < DAY_SECONDS * 30):
        return timeago_template('DAYS_AGO', locale, ago_in) % (int(diff_seconds / DAY_SECONDS))

    # a month ago
    if(diff_seconds < MONTH_SECONDS * 2):
        return timeago_template('A_MONTH_AGO', locale, ago_in)

    # months ago
    if(diff_seconds < MONTH_SECONDS * 12):
        return timeago_template('MONTHS_AGO', locale, ago_in) % (int(diff_seconds / MONTH_SECONDS))

    # a year ago
    if(diff_seconds < YEAR_SECONDS * 2):
        return timeago_template('A_YEAR_AGO', locale, ago_in)

    # years ago
    return timeago_template('YEARS_AGO', locale, ago_in) % (int(diff_seconds / YEAR_SECONDS))
