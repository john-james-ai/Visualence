#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \canvas.py                                                            #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Wednesday January 1st 2020, 2:56:38 am                         #
# Last Modified: Wednesday January 1st 2020, 8:19:29 am                       #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2020 Decision Scients                                         #
# =========================================================================== #
""" Validator, ValidationFactory, and AttributeValidator classes.

Validation of the Canvas objects is directed by the Validator class. Once
a Validator class is invoked, it dispatches the ValidationFactory to create
the appropriate validation instance for the request. The ValidationFactory
produces:

    * CanvasValidator : Validates all attributes of the Canvas object. 
    * CanvasComponentValidator : Validates all attributes of a 
        CanvasComponent object.
    * CanvasAttributeValidator : Validates an individual attribute a
        CanvasComponent object.

There are five validation checks conducted on each parameter's value:

    * type : is the value the correct type  
    * allowed : is the value one of the allowed values, if appropriate
    * min : is the value greater or equal to the minimum  
    * max : is the value less than or equal to the maximum  
    * regex : does the value match one of the regex patterns

If a value is determined to be invalid, an appropriate error message is logged
and a ValueError is raised.
"""
import numpy as np
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import getpass
from uuid import uuid4

from utils import is_none, is_not_none, is_empty, is_not_empty, is_bool
from utils import is_integer, is_number, is_string, is_equal, is_not_equal
from utils import is_less, is_less_equal, is_greater, is_greater_equal
from utils import is_match
# =========================================================================== #
#                             BASECANVASVALIDATOR                             #
# =========================================================================== #
class BaseCanvasValidator(ABC):

    def __init__(self):
        # Designate unique/opaque userid and other metadata      
        self._id = str(uuid4())
        self._created = datetime.now()
        self._creator = getpass.getuser()
    
    def _validate_type(self, instance, attribute, parameter):
        """ Ensures the attribute has the correct type."""
        value = instance.get_parameter(attribute)
        type_expected = instance.get_type(attribute)
        type_observed = type(value).__name__
        if type_expected != type_observed:
            error_message = "Expected the attribute to be a {expected} type, \
                but observed a value of the {observed} type.".format(
                    expected=type_expected,
                    observed=type_observed
                )
            return error_message

    def _validate_allowed(self, instance, attribute, parameter):
        """ Ensures the attribute is one of the allowed values."""
        allowed =  instance.get_allowed_values(attribute)        
        if allowed:
            value = instance.get_parameter(attribute)
            if value is not None and value not in allowed:
                error_message = "{value} is invalid for {attr}. Allowed values include \
                    {allowed}.".format(
                        value=repr(value),
                        attr=attribute,
                        allowed=repr(allowed)
                    )
                return error_message

    def _validate_min(self, instance, attribute, parameter):
        """ Ensures the attribute is not less than a designated minimum value."""
        min_value =  instance.get_min_value(attribute)        
        if min_value:
            value = instance.get_parameter(attribute)
            if value is not None and value < min_value:
                error_message = "{value} must be greater than or equal to {min}".format(
                        value=repr(value),
                        min=min_value
                    )
                return error_message        

    def _validate_max(self, instance, attribute, parameter):
        """ Ensures the attribute is not greater than a designated maximum value."""
        max_value =  instance.get_max_value(attribute)        
        if max_value:
            value = instance.get_parameter(attribute)
            if value is not None and value > max_value:
                error_message = "{value} must be less than or equal to {max}".format(
                        value=repr(value),
                        max=max_value
                    )
                return error_message     

    def _validate_regex(self, instance, attribute, parameter):
        """ Ensures the attribute matches a specified regex pattern."""
                
        regex =  instance.get_regex(attribute)                
        if regex:            
            match = False
            value = instance.get_parameter(attribute)
            for pattern in regex:
                if is_match(value, pattern):
                    match=True
            if not match:
                error_message = "{value} doesn't match [any of] the designated \
                    regex pattern(s).".format(
                        value=repr(value)
                    )
                return error_message 

    def _validate_rule(self, instance, attribute, parameter):
        """ Evaluates the validation rule."""
        rule_validator = RuleValidator():
        if not rule_validator.validate.is_valid(instance, attribute, parameter):
            error_message = rule_validator.error_message
            return error_message

    def validate(self, instance, attribute, parameter):
        """ Validates a parameter object.

        There are five validation checks conducted on each parameter's value:

        * type : is the value the correct type  
        * allowed : is the value one of the allowed values, if appropriate
        * min : is the value greater or equal to the minimum  
        * max : is the value less than or equal to the maximum  
        * regex : does the value match one of the regex patterns

        There are methods for each type of validation and they are dispatched
        in turn.       

        Parameters
        ----------
        instance : Canvas or CanvasComponent object
            The instance of the class being evaluated.
        attribute : str
            The name of the attribute being evaluated
        parameter : dict
            A dictionary containing the validation rules and the parameter value.

        Raises
        ------
        ValueError : Raised if value is determined to be invalid.

        """
        error_messages = []
        error_messages.append(self._validate_type(instance, attribute, parameter))
        error_messages.append(self._validate_allowed(instance, attribute, parameter))
        error_messages.append(self._validate_min(instance, attribute, parameter))
        error_messages.append(self._validate_max(instance, attribute, parameter))
        error_messages.append(self._validate_regex(instance, attribute, parameter))
        error_messages.append(self._validate_rule(instance, attribute, parameter))

        if error_messages:
            raise Exception("An exception occurred. \
                \n      Class : {classname}, \
                \n  Attribute : {attrname}.".format(
                    classname = instance.__class__.__name__,
                    attrname = attribute
                ))

            for message in error_messages:
                print("\n     {message}".format(message=message))

# =========================================================================== #
#                           CANVAS RULE VALIDATOR                             #
# =========================================================================== #
class CanvasRuleValidator(BaseCanvasValidator):
    """Evaluates validation rules for the CanvasComponent classes.

    Canvas parameters are dictionaries containing various attributes of the 
    parameter, as well as a dictionary defining an additional validation or
    rules, perhaps, involving other attributes of the instance. These semantic
    validation rules  a validation rule.