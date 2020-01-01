#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \base.py                                                              #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Tuesday December 31st 2019, 3:07:42 pm                         #
# Last Modified: Tuesday December 31st 2019, 7:05:21 pm                       #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2019 Decision Scients                                         #
# =========================================================================== #
"""
Plotly plots are comprised primarily of two constituents: a data constituent
and a layout constituent. The data constituent specifies 'what' will be 
plotted; whereas, the layout constituent defines 'how' the data will be 
plotted. 

Plotly layouts consist of over 140 parameters, which we have organized
into 18 groups of parameters. Each group is managed by a specific 
CanvasComponent class. It exposes methods for setting and getting the
parameters within its class.

The Canvas class is a container of CanvasComponent classes, representing
the client's Plotly layout parameter settings for plotting purposes.

This module defines the Canvas class as well as the CanvasComponent 
interface.
"""
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import getpass
from uuid import uuid4

class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Canvas(Borg):
    """Class that contains the plotting parameters and defaults.
    
    Plotly plots are comprised of data and layout components. The data 
    component specifies 'what' is being plotted.  The layout component
    defines 'how' the data is being plotted.

    This class contains the Plotly layout parameters to be applied to 
    any plot.  The parameters are organized into 18 CanvasComponent
    classes. As such, the Canvas class is composed of the following
    component classes:

    * CanvasTitle : Title text, font and font family
    * CanvasLegend : Background color, border, font, font size and location.
    * CanvasMargins : Padding and margins for left, top, and bottom. 
    * CanvasSize : The height and width of the canvas or layout.
    * CanvasFont : Font family, size, and color.
    * CanvasColorBackground : The background for Plotly plot and paper.
    * CanvasColorScale : The colorscale, either diverging or sequential.
    * CanvasColorAxisDomain : Defines the color domain vis-a-vis data.
    * CanvasColorAxisScales : The color axis colorscale.
    * CanvasColorAxisBarStyle : The thickness, length, and color.
    * CanvasColorAxisBarPosition : The location of the colorbar.
    * CanvasColorAxisBarBoundary : The outline and color of the boundary.
    * CanvasColorAxisBarTicks : The colorbar ticks.
    * CanvasColorAxisBarTickStyle : Color angle, prefix and suffix of ticks.
    * CanvasColorAxisBarTickFont : Family size and color of tick fonts.
    * CanvasColorAxisBarTickFormatStops : Tick format stops
    * CanvasColorAxisBarNumbers : Format of numbers on the coloraxis bar.
    * CanvasColorAxisBarTitle : Text, font, and color of coloraxis bar. 
    
    The Canvas class obtains the parameters from the above CanvasComponent
    classes and stores them in a single canvas dictionary.

    """   
    def __init__(self):
        # Designate unique/opaque userid and other metadata      
        super(Canvas, self).__init__()  
        self._id = str(uuid4())
        self._created = datetime.now()
        self._creator = getpass.getuser()

        # Component objects                
        self._components = {}

    def add_component(self, component):        
        """Adds a CanvasComponent object.
        
        Parameters
        ----------
        component : CanvasComponent
            Adds a CanvasComponent object to the component dictionary
        """
        component_name = component.__class__.__name__            
        self._components[component_name] = component

        return self

    def del_component(self, component):
        """Removes a CanvasComponent object.
        
        Parameters
        ----------
        component : str or CanvasComponent 
            Either the name of a CanvasComponent object or the object itself.

        Raises
        ------
        ValueError : If component is not found.

        """
        try:
            component_name = component.__class__.__name__            
            del self._components[component_name]
        except(Exception):
            try:
                del self._components[component]
            except(Exception):
                print("{component} is not found.".format(component=repr(component)))

        return self

    def print_components(self, component=None):
        """Prints components.

        Parameters
        ----------
        component : str or CanvasComponent object
            component to print
        """
        if component is not None:
            try:
                component_name = component.__class__.__name__            
                print(str(self._components[component_name]))
            except(Exception):
                try:
                    print(str(self._components[component]))
                except(Exception):
                    print("{component} is not found.".format(component=repr(component)))
        else:
            for _, component in self._components.items():
                print(str(component))

        return self


    def get_parameters(self):
        """Extracts all parameters and returns as key/value pairs."""
        parameters = {}
        for _, component in self._components.items():
            parameters.update(component.get_parameters())
        return parameters

class CanvasComponent(ABC):
    """Abstact base class for all CanvasComponent subclasses.
    
    CanvasComponents store parameters in nested dictionaries in which there
    is an outer dictionary and an inner dictionary. The outer dictionary 
    key is the name of the parameter and the value is a dictionary containing:

    * the Plotly name of the variable
    * the Plotly parent name of the variable
    * the type of the variable  
    * allowed values if applicable
    * a minimum value if applicable
    * a maximum value if applicable
    * the default value 
    * the current value

    outer dictionary is the parameter name and 
    
    """

    @abstractmethod
    def __init__(self):
        # Designate unique/opaque userid and other metadata      
        self._id = str(uuid4())
        self._created = datetime.now()
        self._creator = getpass.getuser()        

        self._parameters = {}

    def __getattr__(self, name):
        """Returns the value of the named attribute."""
        try:
            definition = self._parameters[name]
        except(Exception) as e:
            print(e)
        else:
            parameter = {}
            parameter[name] = definition['value']
        return parameter

    def __setattr__(self,name, value):
        """Sets the value of the named attribute."""
        try:
            definition = self._parameters[name]
        except(Exception) as e:
            print(e)
        else:
            definition['value'] = value
            self._parameters[name] = definition
        return self

    def get_parameters(self):
        """Returns all parameters as key/value pairs."""
        parameters = {}
        for name, parameter in self._parameters.items():
            d = {}
            d[name] = parameter['value']
            parameters.update(d)
        return parameters    

    def _get_attribute(self, name, attribute):
        try:
            definition = self._parameters[name]
        except(Exception) as e:
            print(e)

        try:
            value = definition[attribute]
        except(Exception) as e:
            print(e)
        return value

    def _set_attribute(self, name, value):
        try:
            definition = self._parameters[name]
        except(Exception) as e:
            print(e)
        definition['value'] = value
        self._parameters[name] = definition
        return self
    
    
    def get_plotly_name(self, name):
        """Returns the Plotly name for the named attribute."""
        return self._get_attribute(name, 'plotly_name')

    def get_plotly_parent(self, name):
        """Returns the Plotly name for the named attribute."""
        return self._get_attribute(name, 'plotly_parent')
    
    def get_type(self, name):
        """Returns the Plotly name for the named attribute."""
        return self._get_attribute(name, 'type')

    def get_allowed_values(self, name):
        """Returns the Plotly name for the named attribute."""
        return self._get_attribute(name, 'allowed_values')

    def get_min_value(self, name):
        """Returns the Plotly name for the named attribute."""
        return self._get_attribute(name, 'min_value')

    def get_max_value(self, name):
        """Returns the Plotly name for the named attribute."""
        return self._get_attribute(name, 'max_value')

    def get_parameter(self, name):
        """Returns the value of the named parameter."""
        return self._get_attribute(name, 'value')

    def set_parameter(self, name, value):
        self._set_attribute(name, value)
        return self

    def get_default_value(self, name):
        """Returns the value of the named attribute."""
        return self._get_attribute(name, 'default')

    def print_parameters(self, name=None):
        """Prints all parameters or the named parameter if so designated."""
        if name is None:
            for name, parameter in self._parameters.items():
                print("\nParameter : {name}".format(name=name))
                for k,v in parameter.items():
                    print("     {k}: {v}".format(k=k, v=v))
        else:
            try:
                definition = self._parameters[name]
            except(Exception) as e:
                print(e)
            else:
                print("\nParameter : {name}".format(name=name))
                for k,v in definition.items():
                    print("     {k}: {v}".format(k=k, v=v))

        return self
