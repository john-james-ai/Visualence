#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \title.py                                                             #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Tuesday December 31st 2019, 3:06:33 pm                         #
# Last Modified: Wednesday January 1st 2020, 5:53:21 am                       #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2019 Decision Scients                                         #
# =========================================================================== #
#                           TITLE CLASS                                       #
# =========================================================================== #
from datetime import datetime
import getpass
from uuid import uuid4
from .base import CanvasComponent
from visualence import COLORS
class CanvasTitle(CanvasComponent):
    """Defines the title properties for the Plotly layout."""

    def __init__(self):
        super(CanvasTitle, self).__init__()
        self.reset()

    def reset(self):
        """Initializes and resets the parameters to their defaults."""
        self._reset_title_text()
        self._reset_title_font_family()
        self._reset_title_font_size()
        self._reset_title_font_color()
        self._reset_title_x()
        self._reset_title_y()
        self._reset_title_xref()
        self._reset_title_yref()
        self._reset_title_xanchor()
        self._reset_title_yanchor()
        self._reset_title_pad_top()
        self._reset_title_pad_bottom()
        self._reset_title_pad_left()

    def _reset_title_text(self):
        self._parameters['title_text'] = {
            'plotly_name' : 'text',
            'plotly_parent' : 'layout.title',
            'description' : "Sets the plot's title.",
            'type' : str,
            'allowed' : [],
            'min' : None,
            'max' : None,
            'regex' : None,
            'default' : "",
            'value':"",
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }
    def _reset_title_font_family(self):
        self._parameters['title_font_family'] = {
            'plotly_name' : 'family',
            'plotly_parent' : 'layout.title.font',
            'description' : """HTML font family - the typeface that will be applied by the web browser. The web browser will only be able to apply a font if it is available on the system which it operates. Provide multiple font families, separated by commas, to indicate the preference in which to apply fonts if they aren't available on the system. The plotly service (at https://plot.ly or on-premise) generates images on a server, where only a select number of fonts are installed and supported. These include 'Arial', 'Balto', 'Courier New', 'Droid Sans',, 'Droid Serif', 'Droid Sans Mono', 'Gravitas One', 'Old Standard TT', 'Open Sans', 'Overpass', 'PT Sans Narrow', 'Raleway', 'Times New Roman'.""",
            'type' : str,
            'allowed' : [],
            'min' : None,
            'max' : None,
            'regex' : None,
            'default' : "Open Sans",
            'value':['Open Sans', 'Balto'],
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }

    def _reset_title_font_size(self):
        self._parameters['title_font_size'] = {
            'plotly_name' : 'size',
            'plotly_parent' : 'layout.title.font',
            'description' : "Sets font size.",
            'type' : int,
            'allowed' : [],
            'min' : 1,
            'max' : None,
            'regex' : None,
            'default' : None,
            'value': None,
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }        
    def _reset_title_font_color(self):
        self._parameters['title_font_color'] = {
            'plotly_name' : 'color',
            'plotly_parent' : 'layout.title.font',
            'description' : "Sets font color.",
            'type' : str, 
            'allowed' : COLORS,
            'min' : None,
            'max' : None,
            'regex' : ['re.compile(r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})")', 
                       're.compile(r"(rgb|hsl|hsv)a?\\([\\d.]+%?(,[\\d.]+%?){2,3}\\)")',
                       're.compile(r"var\\(\\-\\-.*\\)")'],
            'default' : None,
            'value': None,
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }        

    def _reset_title_xref(self):
        self._parameters['title_xref'] = {
            'plotly_name' : 'xref',
            'plotly_parent' : 'layout.title',
            'description' : """Sets the container `x` refers to. "container" spans the entire `width` of the plot. "paper" refers to the width of the plotting area only.""",
            'type' : str,
            'allowed' : ['container', 'paper'],
            'min' : None,
            'max' : None,
            'regex' : None,
            'default' : 'container',
            'value': 'container',
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }                
 
    def _reset_title_yref(self):
        self._parameters['title_yref'] = {
            'plotly_name' : 'yref',
            'plotly_parent' : 'layout.title',
            'description' : """Sets the container `y` refers to. "container" spans the entire `height` of the plot. "paper" refers to the height of the plotting area only.""",
            'type' : str,
            'allowed' : ['container', 'paper'],
            'min' : None,
            'max' : None,
            'regex' : None,
            'default' : 'container',
            'value': 'container',
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }                        

    def _reset_title_x(self):
        self._parameters['title_x'] = {
            'plotly_name' : 'x',
            'plotly_parent' : 'layout.title',
            'description' : """Sets the x position with respect to `xref` in normalized coordinates from "0" (left) to "1" (right).""",
            'type' : float,
            'allowed' : [],
            'min' : 0,
            'max' : 1,
            'regex' : None,
            'default' : 0.5,
            'value': 0.5,
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }        

    def _reset_title_y(self):
        self._parameters['title_y'] = {
            'plotly_name' : 'y',
            'plotly_parent' : 'layout.title',
            'description' : """Sets the y position with respect to `yref` in normalized coordinates from "0" (bottom) to "1" (top). "auto" places the baseline of the title onto the vertical center of the top margin.""",
            'type' : float,
            'allowed' : [],
            'min' : 0,
            'max' : 1,
            'regex' : None,
            'default' : 0.5,
            'value': 0.5,
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }         

    def _reset_title_xanchor(self):
        self._parameters['title_xanchor'] = {
            'plotly_name' : 'xanchor',
            'plotly_parent' : 'layout.title',
            'description' : """Sets the title's horizontal alignment with respect to its x position. "left" means that the title starts at x, "right" means that the title ends at x and "center" means that the title's center is at x. "auto" divides `xref` by three and calculates the `xanchor` value automatically based on the value of `x`.""",
            'type' : str,
            'allowed' : ["auto", "left", "center", "right"],
            'min' : None,
            'max' : None,
            'regex' : None,
            'default' : "auto",
            'value': "auto",
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }              

    def _reset_title_yanchor(self):
        self._parameters['title_yanchor'] = {
            'plotly_name' : 'yanchor',
            'plotly_parent' : 'layout.title',
            'description' : """Sets the title's vertical alignment with respect to its y position. "top" means that the title's cap line is at y, "bottom" means that the title's baseline is at y and "middle" means that the title's midline is at y. "auto" divides `yref` by three and calculates the `yanchor` value automatically based on the value of `y`.""",
            'type' : str,
            'allowed' : ["auto", "top", "middle", "bottom"],
            'min' : None,
            'max' : None,
            'regex' : None,
            'default' : "auto",
            'value': "auto",
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }   

    def _reset_title_pad_top(self):
        self._parameters['title_pad_top'] = {
            'plotly_name' : 't',
            'plotly_parent' : 'layout.title.pad',
            'description' : """The amount of padding (in px) along the top of the component.""",
            'type' : int,
            'allowed' : [],
            'min' : 0,
            'max' : None,
            'regex' : None,
            'default' : 0,
            'value': 0,
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }   

    def _reset_title_pad_bottom(self):
        self._parameters['title_pad_bottom'] = {
            'plotly_name' : 'b',
            'plotly_parent' : 'layout.title.pad',
            'description' : """The amount of padding (in px) along the bottom of the component.""",
            'type' : int,
            'allowed' : [],
            'min' : 0,
            'max' : None,
            'regex' : None,
            'default' : 0,
            'value': 0,
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }           

    def _reset_title_pad_left(self):
        self._parameters['title_pad_left'] = {
            'plotly_name' : 'l',
            'plotly_parent' : 'layout.title.pad',
            'description' : """The amount of padding (in px) along the left of the component.""",
            'type' : int,
            'allowed' : [],
            'min' : 0,
            'max' : None,
            'regex' : None,
            'default' : 0,
            'value': 0,
            'validation' : {
                'logical' : 'all',
                'rules' : [
                    {
                        'a' : None,
                        'b' : None,
                        'operator' : None
                    }
                ]
        }