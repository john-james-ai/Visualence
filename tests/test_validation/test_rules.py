#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# =========================================================================== #
# Project: Visualence                                                         #
# Version: 0.1.0                                                              #
# File: \test_rules.py                                                        #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Wednesday January 1st 2020, 9:46:26 am                         #
# Last Modified: Wednesday January 1st 2020, 2:26:55 pm                       #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2020 Decision Scients                                         #
# =========================================================================== #
import numpy as np
import pytest
from pytest import mark

from visualence.validation.rules import Rule, RuleSet
from visualence.validation.utils import is_number, is_greater, is_in
# =========================================================================== #
#                            TEST RULE                                        #
# =========================================================================== #
class RuleTests:

    @mark.validation
    @mark.validation_rules
    @mark.validation_rules_syntactic_instantiation
    def test_validation_rules_syntactic_instantiation(self, create_canvas_component):
        component = create_canvas_component
        attribute = 'title_x'
        rule = Rule(instance=component, attribute=attribute)
        assert 'CanvasTitle' in rule.name, "Rule name not valid"
        assert rule.classname == 'CanvasTitle', "Class name is invalid"
        assert rule.attribute == 'title_x', "Attribute is invalid"
        assert rule.a is None, "a is invalid"
        assert rule.b is None, "b is invalid"
        assert rule.operator is None, "operator is invalid"
        assert rule.is_valid is True, "is_valid not initialized"
        assert rule.error_message is None, "error message not valid"
        assert rule.is_composite == False, "error message not valid"

    @mark.validation
    @mark.validation_rules
    @mark.validation_rules_syntactic_setters
    def test_validation_rules_syntactic_setters(self, create_canvas_component):
        component = create_canvas_component
        attribute = 'title_x'
        rule = Rule(instance=component, attribute=attribute)
        rule.name = "No Whiners"
        rule.a = "max"
        rule.operator = is_number
        rule.error_message = "Should be a number"
        assert rule.name == "No Whiners", "Name not updated"
        assert rule.a == 1, "a not updated"        
        assert rule.operator == is_number, "operator not updated"
        assert rule.error_message == "Should be a number", "Error message not updated"
        # Error handling
        with pytest.raises(ValueError):
            rule.operator = 'x'     
               
    @mark.validation
    @mark.validation_rules
    @mark.validation_rules_syntactic
    @mark.validation_rules_syntactic_validate
    def test_validation_rules_syntactic_validate(self, create_canvas_component):
        component = create_canvas_component
        attribute = 'title_x'
        rule = Rule(instance=component, attribute=attribute)
        with pytest.raises(Exception):
            rule.validate().is_valid
        rule.a = 'max'
        rule.operator = is_number
        assert rule.validate().is_valid == True, "Invalid evaluation of syntactic rule"
        rule.a = 'description'
        rule.operator = is_number
        assert rule.validate().is_valid == False, "Validation didn't fail as expected."
        assert rule.error_message is not None, "Error message on fail not rendered."
        print(rule.error_message)
               
    @mark.validation
    @mark.validation_rules
    @mark.validation_rules_semantic
    @mark.validation_rules_semantic_validate
    def test_validation_rules_semantic_validate(self, create_canvas_component):
        component = create_canvas_component
        attribute = 'title_x'
        rule = Rule(instance=component, attribute=attribute)
        with pytest.raises(Exception):
            rule.validate().is_valid
        rule.a = 'max'
        rule.operator = is_greater
        rule.b = 'min'
        assert rule.validate().is_valid == True, "Invalid evaluation of semantic rule"
        rule.a = 'description'        
        with pytest.raises(TypeError):
            assert rule.validate().is_valid == False, "Validation didn't fail as expected."        
        rule.b = 5
        with pytest.raises(TypeError):
            assert rule.validate().is_valid == False, "Validation didn't fail as expected."
        rule.a = 'max'
        assert rule.validate().is_valid == False, "Validation didn't fail as expected."
        print(rule.error_message)

    @mark.validation
    @mark.validation_rules
    @mark.validation_rules_semantic
    @mark.validation_rules_semantic_error_handling
    def validation_rules_semantic_error_handling(self, create_canvas_component):
        component = create_canvas_component
        attribute = 'x'
        with pytest.raises(ValueError):        
            Rule(component, attribute)
               
# =========================================================================== #
#                            TEST RULE SETS                                   #
# =========================================================================== #
class RuleSetTests:

    @mark.validation
    @mark.validation_rule
    @mark.validation_rule_sets
    @mark.validation_rule_sets_instantiation
    def test_validation_rules_sets_instantiation(self, create_canvas_component):  
        component = create_canvas_component
        attribute = 'title_xanchor'
        rule_set = RuleSet(component, attribute) 
        assert rule_set.is_composite == True, "is composite not initialized"
        assert "CanvasTitle" in rule_set.name, "name not initialized"
        assert "CanvasTitle" == rule_set.classname, "classname not initialized"
        assert "title_xanchor" == rule_set.attribute, "attribute not initialized"
        assert "all" == rule_set.logical, "logical not initialized"
        assert "all" == rule_set.logical, "logical not initialized"        
        assert rule_set.get_components() == [], "components not initialized."

    @mark.validation
    @mark.validation_rule
    @mark.validation_rule_sets
    @mark.validation_rule_sets_child_management
    def test_validation_rule_sets_child_management(self, create_canvas_component):  
        component = create_canvas_component
        attribute = 'title_xanchor'
        ruleset1_name = "Grabbin' the Pope"
        ruleset1 = RuleSet(component, attribute)
        ruleset1.get_components()
        # Error handling
        with pytest.raises(ValueError):
            ruleset1.get_component(ruleset1_name)
        with pytest.raises(ValueError):
            ruleset1.add_component(ruleset1_name)                
        with pytest.raises(ValueError):
            ruleset1.del_component(ruleset1_name)
        rule1 = Rule(component, attribute)
        rule1.a = 'max'
        rule1.b = 'min'
        rule1.operator = is_greater
        rule2 = Rule(component, attribute)
        rule2.a = 'description'
        rule2.operator = is_number
        # Add rules
        ruleset1.add_component(rule1)
        ruleset1.print
        assert rule1 in ruleset1.get_component(rule1) 
        ruleset1.add_component(rule2)
        # Create another ruleset
        ruleset2 = RuleSet(component, attribute)
        rule3=Rule(component, attribute)
        ruleset2.add_component(rule3)
        ruleset1.add_component(ruleset2)
        print(ruleset1)

        

