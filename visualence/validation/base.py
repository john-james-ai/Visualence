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
# Create Date: Wednesday January 1st 2020, 5:41:15 am                         #
# Last Modified: Wednesday January 1st 2020, 5:45:32 am                       #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2020 Decision Scients                                         #
# =========================================================================== #
#                              BASE VALIDATOR                                 #
# =========================================================================== #
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
class BaseValidator(ABC):
    """The abstract base class for all Validator objects."""

    def __init__(self):
    # Designate unique/opaque userid and other metadata      
        self._id = str(uuid4())
        self._created = datetime.now()
        self._creator = getpass.getuser()        
        self._error_message = None
        self._is_valid = False

    @property
    def error_message(self):
        return self._error_message

    @property
    def is_valid(self):
        return self._is_valid

    @abstractmethod
    def validate(self, instance, attribute, parameter):
        pass
    