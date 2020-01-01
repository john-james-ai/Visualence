#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \rule.py                                                              #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Wednesday January 1st 2020, 6:02:36 am                         #
# Last Modified: Wednesday January 1st 2020, 9:40:35 am                       #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2020 Decision Scients                                         #
# =========================================================================== #
#                          VALIDATION RULES                                   #
# =========================================================================== #
""" Validation RuleSet and validation Rule classes.

Validation Rule
---------------
A validation Rule is comprised of two operands, a and b,  and an operator.
The 'a' operand is an attribute on the instance being evaluated. The 'b'
operand is optional and may contain the name of an attribute on the 
instance being evaluated or it may be a literal value. There are two types
of operators: syntactic and semantic.

The syntactic operators involve only the 'a' operand and is one of:
    * is_none
    * is not_none
    * is_empty
    * is_not_empty
    * is_bool
    * is_integer
    * is_number
    * is_string.

The purpose of the rule is to evaluate the syntax of operand 'a'.

Semantic operators compare two (or more) values, hence, the 'b' value
is required. Semantic operators include:
    * is_less
    * is_less_equal
    * is_greater
    * is_greater_equal
    * is_match (regex)

Validation RuleSet
------------------
A validation RuleSet is a collection of RuleSet or Rule objects along 
with a logical variable which determines how the Rule objects are 
to be evaluated together. The logical may be:
    * 'all' : when all rules must pass 
    * 'any' : when any one rule must pass
    * None  : when none of the rules must pass

These classes are defined in accordance with the composite pattern,
including the following classes:

    * BaseRule : Abstract base rule that defines the Rule interface.
    * RuleSet : Composite class containing Rule and RuleSet objects.
    * Rule : Leaf class that contains indidual rules.

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

SYNTACTIC_OPERATORS = [is_none.__name__, 
                       is_not_none.__name__,
                       is_empty.__name__,
                       is_not_empty.__name__,
                       is_bool.__name__,
                       is_integer.__name__,
                       is_number.__name__,
                       is_string.__name__]

SEMANTIC_OPERATORS = [is_less.__name__,
                      is_less_equal.__name__,
                      is_greater.__name__,
                      is_greater_equal.__name__,
                      is_match.__name__]                       
# =========================================================================== #
#                               BASE RULE                                     #
# =========================================================================== #
class BaseRule(ABC):
    """ Abstract base class defining the interface for Rule and RuleSet classes."""

    def __init__(self, instance, attribute, parameters):
        # Designate unique/opaque userid and other metadata      
        self._id = str(uuid4())
        self._created = datetime.now()
        self._creator = getpass.getuser()        

        self._instance = instance        
        self._attribute = attribute
        self._parameters = parameters

    @property
    def is_composite(self):
        return False

    @abstractmethod
    def get_component(self, name):
        pass

    @abstractmethod
    def get_components(self):
        pass    

    @abstractmethod
    def add_component(self, component):
        pass

    @abstractmethod
    def del_component(self, component):
        pass

    @abstractmethod
    def print(self, name=None):
        pass

    @abstractmethod
    def validate(self):
        pass

# =========================================================================== #
#                               RULE SET                                      #
# =========================================================================== #
""" Composite class containing Rule and RuleSet objects."""

class RuleSet(BaseRule):

    ID = 0

    def __init__(self, instance, attribute, parameters):
        super(RuleSet, self).__init__(instance=instance,
                                      attribute=attribute,
                                      parameters=parameters)
        self._reset_rule_set()

    def _reset_rule_set(self):
        """Resets the RuleSet object to 'factory' state."""        
        
        self._rule_set = {
            'id': self._id,
            'name': self._instance.__class__.__name__ + "_" + self._attribute + \
                "_rule_set_#_" + str(self.__class__.ID),
            'creator': self._creator,
            'created': self._created,            
            'classname' : self._instance.__class__.__name__,
            'attribute': self._attribute,
            'logical': None,
            'components':[]            
        }
        self.__class__.ID += 1

    def reset_rule_set(self):
        """Public method for resetting the RuleSet object with confirmation."""

        confirmation = input("Resetting the RuleSet object will permanently\
                    delete associated Rule objects. Are you sure you would like\
                    to proceed? (y/n) ")
        if confirmation in ["y", "Y", "yes", "YES"]:
            self._reset_rule_set()
        else:
            return self

    @property
    def is_composite(self):        
        return True

    @property
    def name(self):
        return self._rule_set['name']

    @property
    def logical(self):
        return self._rule_set['logical']

    @logical.setter
    def logical(self, value):
        if value in ['all', 'any', None]:
            self._rule_set['logical'] = value
        else:
            raise ValueError("{value} is an invalid logical operand. Valid \
                values are ['all', 'any', None].".format(value=value))

    def get_rule_set(self):
        """Returns the current RuleSet object.""" 
        return self._rule_set        

    def get_component(self, name):
        """Returns the named Rule or RuleSet component object.""" 
        component_found = False        
        for component in self._rule_set['components']:
            if component.name == name:
                component_found = True
                return component
        if not component_found:
            raise ValueError("The component Rule or RuleSet {name} was not found.".format(name=name))
        return self

    def get_components(self):
        return self._rule_set['components']
            
    def add_component(self, component):
        """ Add component Rule or RuleSet object to the components list."""
        self._rule_set['components'].append(component)
        return self

    def del_component(self, name):
        """ Delete named Rule or RuleSet object from the rules list."""
        component_found = False
        for component in self._rule_set['components']:
            if name == component.name:
                component_found = True
                self._rule_set['components'].remove(component)

        if not component_found:
            raise ValueError("The component Rule or RuleSet {name} was not found.".format(name=name))
        
        return self

    def _raise_exception(self):
        print("Validation rule set: {name} failed.".format(name=self._rule_set['name']))
        components = self._rule_set['components']
        for component in components:
            if component.error_message:
                print("\n{message}".format(component.error_message))

    def validate(self):
        """Performs validation via delegation to component objects."""

        is_valid=[]
        for component in self._rule_set['components']:
            if isinstance(component, RuleSet):
                component.validate()
            else:
                is_valid.append(component.validate().is_valid)

        if self._rule_set['logical'] == 'all':
            self._rule_set['is_valid'] = all(is_valid)
        elif self._rule_set['logical'] == 'any':
            self._rule_set['is_valid'] =  any(is_valid)
        else:
            self._rule_set['is_valid'] = not any(is_valid)

        if not self._rule_set['is_valid']:
            self._raise_exception()


# =========================================================================== #
#                                  RULE                                       #
# =========================================================================== #
class Rule(BaseRule):
    """ Class specifying a single validation rule for a single attribute."""

    ID = 0

    def __init__(self, instance, attribute, parameters):
        super(Rule, self).__init__(instance=instance,
                                   attribute=attribute,
                                   parameters=parameters)

        self.a = None
        self.b = None
        self.operator = None        
        self._rule = {}
        self._reset_rule()

    def _reset_rule(self):
        """Resets a rule to 'factory' condition."""
        self._rule = {
            'id': self._id,
            'name': self._instance.__class__.__name__ + "_" + self._attribute + \
                "_rule_#_" + str(self.__class__.ID),
            'creator': self._creator,
            'created': self._created,            
            'classname' : self._instance.__class__.__name__,
            'attribute': self._attribute,
            'a': None,
            'b': None,
            'operator': None,
            'is_valid': True,
            'error_message' : None
        }
        self.__class__.ID += 1
        return self

    def reset_rule(self):
        """Public method for resetting the Rule object with confirmation."""

        confirmation = input("Resetting the Rule object will permanently\
                    remove its contents. Are you sure you would like\
                    to proceed? (y/n) ")
        if confirmation in ["y", "Y", "yes", "YES"]:
            self._reset_rule()
        else:
            return self

    def _reset_validation_results(self):
        self._rule['is_valid'] = True
        self._rule['error_message'] = None

    @property
    def is_composite(self):
        return False

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        try:
            self._a = getattr(self._instance, value)
        except(AttributeError):
            self._a = value
        return self

    @property
    def b(self):
        return self._b
        
    @b.setter
    def b(self, value):
        try:
            self._b = getattr(self._instance, value)
        except(AttributeError):
            self._b = value
        return self

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        operator_name = value.__name__
        if operator_name in SYNTACTIC_OPERATORS or \
            operator_name in SEMANTIC_OPERATORS:
            self._operator = value
        else:
            raise ValueError("{oper} is not a valid operator function. Valid\
                operators include:\n\
                    Syntactic Operators : {syntactic}\n\
                    Semantic Operators : {semantic}".format(
                        oper=value,
                        syntactic=SYNTACTIC_OPERATORS,
                        semantic=SEMANTIC_OPERATORS
                    ))        
        return self

    @property
    def error_message(self):
        return self._rule['error_message']

    @error_message.setter
    def error_message(self, value):
        self._rule['error_message'] = value
        return self

    def get_component(self, name):
        pass

    def get_components(self):
        pass

    def add_component(self, component):
        pass

    def del_component(self, component):
        pass

    def print(self):
        print("\nname : {name}, created by: {creator} at {created}\
            \n          Class : {classname}\
            \n      Attribute : {attribute}\
            \n              a : {a}\
            \n              b : {b}\
            \n       Operator : {operator}\
            \n       is_valid : {isvalid}\
            \n  Error Message : {error}".format(
                name=self._rule['name'],
                creator=self._rule['creator'],
                created=self._rule['created'],
                classname=self._rule['classname'],
                attribute=self._rule['attribute'],
                a=self._rule['a'],
                b=self._rule['b'],
                operator=self._rule['operator'],
                isvalid=self._rule['is_valid']
            ))

    def _obtain_values(self):
        # If 'a' is an attribute name, obtain its value from the instance
        try:
            self._a = getattr(self._instance, self._a)
        except(AttributeError):
            pass

        # Confirm 'b' is provided for semantic rules:
        if self._rule['operator'] in SEMANTIC_OPERATORS:
            if self._b:
                try:
                    self._b = getattr(self._instance, self._b)
                except(AttributeError):
                    pass
            else:
                raise ValueError("Parameter 'b' is required {operator}.".format(
            operator=self._rule['operator'].__name__
            ))

        return self

    def _is_ready(self):
        if self._rule['a'] is None:
            return False
        if self._rule['operator'] is None:
            return False
        if self._rule['operator'] in SEMANTIC_OPERATORS:
            if self._b is None:
                return False
        return True
        

    def _validate_syntactic_rule(self):
        if self._rule['operator'](self._a):
            self._rule['is_valid'] = True
        else:
            self._rule['is_valid'] = False
            self._rule['error_message'] = "Validation rule {name}, specifying \
                that {a} is {oper}, failed.".format(
                    name=self._rule['name'],
                    a=self._a,
                    oper=self._rule['operator']
                )

        return self

    def _validate_semantic_rule(self):
        if self._rule['operator'](self._a, self._b):
            self._rule['is_valid'] = True
        else:
            self._rule['is_valid'] = False
            self._rule['error_message'] = "Validation rule {name}, specifying \
                that {a} is {oper} than {b}, failed.".format(
                    name=self._rule['name'],
                    a=self._a,
                    oper=self._rule['operator'],
                    b=self._b
                )
        return self
    
    def validate(self):
        if self._is_ready():
            self._reset_validation_results()
            self._obtain_values()
            if self._rule['operator'].__name__ in SYNTACTIC_OPERATORS:
                self._validate_syntactic_rule()
            else:
                self._validate_semantic_rule()
            return self
        else:
            raise Exception("This rule is not ready for validation. The 'operator'\
                'a', and if evaluating semantic rule, the 'b' parameters must\
                    be initialized. Current values are:\
                \n       'a' : {a}\
                \n       'b' : {b}\
                \n'operator' : {operator}".format(
                    a=self._a,
                    b=self._b,
                    operator=self._operator
                ))
