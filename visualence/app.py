#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \app.py                                                               #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Friday January 3rd 2020, 1:55:36 am                            #
# Last Modified: Saturday January 4th 2020, 8:22:06 am                        #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2020 Decision Scients                                         #
# =========================================================================== #
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go
import dash_daq as daq

import pandas as pd

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H1("Visualence Data Science Studio"),
                    html.H4("Visual Platform for Analysis and Inference.")
                ],
            ),
        ]
    )

def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab1",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Projects-tab",
                        label="Projects",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Data-tab",
                        label="Data",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Analysis-tab",
                        label="Exploratory Data Analysis",
                        value="tab3",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Feature-selection-tab",
                        label="Feature Selection",
                        value="tab4",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),             
                    dcc.Tab(
                        id="Feature-engineering-tab",
                        label="Feature Engineering",
                        value="tab5",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),             
                    dcc.Tab(
                        id="Model-selection-tab",
                        label="Model Selection",
                        value="tab6",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),             
                    dcc.Tab(
                        id="Model-diagnosis-tab",
                        label="Model Diagnosis",
                        value="tab7",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),                                                                    dcc.Tab(
                        id="Model-evaluation-tab",
                        label="Model Evaluation",
                        value="tab8",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),                                       
                ],
            )
        ],
    )

app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                html.Div(id="app-content")
            ]
        )        
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
