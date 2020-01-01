#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \test_title.py                                                        #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Tuesday December 31st 2019, 7:10:30 pm                         #
# Last Modified: Wednesday January 1st 2020, 2:39:34 am                       #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2019 Decision Scients                                         #
# =========================================================================== #
#                        TEST CANVAS TITLE                                    #
# =========================================================================== #
import pytest
from pytest import mark

from visualence.canvas.title import CanvasTitle

class CanvasTitleTests:

    @mark.canvas
    @mark.canvas_title
    @mark.canvas_title_text
    @mark.canvas_title_text_reset_getters_setters
    def test_canvas_title_text_reset_getters_setters(self):
        canvas = CanvasTitle()
        assert canvas.get_parameter('title_text') == '', "Title text not working."
        assert canvas.get_plotly_name('title_text') == 'text', "Plotly parent get/set not working."
        assert canvas.get_plotly_parent('title_text') == 'layout.title', "Plotly parent get/set not working."
        assert canvas.get_type('title_text') == str, "Type not returned."
        assert canvas.get_description('title_text') is not None, "Description not returned."
        assert canvas.get_allowed_values('title_text') == [], "Allowed values not returned."
        assert canvas.get_min_value('title_text') is None, "Min value not returned."
        assert canvas.get_max_value('title_text') is None, "Max not returned."
        assert canvas.get_default_value('title_text') == "", "Default value not returned."
        canvas.set_parameter('title_text', "Another title")
        assert canvas.get_parameter('title_text') == "Another title", "set_parameter is not working"




