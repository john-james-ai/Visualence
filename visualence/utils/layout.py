#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \layout.py                                                            #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Friday January 3rd 2020, 1:55:52 pm                            #
# Last Modified: Friday January 3rd 2020, 2:09:04 pm                          #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2020 Decision Scients                                         #
# =========================================================================== #
#                           LAYOUT DEFAULTS                                   #
# =========================================================================== #
PALETTES = {
        'blue_orange' : 
        {
            'page_background': "#010038",
            'div_background': "#151965",
            'medium_background': "#293a80",
            "plot_background": "#000000",
            'text': "#537ec5",
            'border_color': "#f39422"

        }
    }

FONTS = {
    'header': {
        'family': 'Open Sans',
        'size': 18,
        'color': PALETTES['blue_orange']['text']
    },
    'sub_header': {
        'family': 'Open Sans',
        'size': 14,
        'color': PALETTES['blue_orange']['text']
    },
    'normal': {
        'family': 'Open Sans',
        'color': PALETTES['blue_orange']['text']
    }
}