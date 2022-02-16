# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:18:57 2022

@author: c.s.francis

@version: Python 3.10.2

@summary: A collection of constants and functions to calculate payroll for a business
"""


from employees import *


FICA = 0.12
REGULAR_TIME = 40


def GrossPay(employee):
    """
    Calculats gross pay for a single employee
    
    Parameters
    ----------
    employeeName : str
        the name of the employee whose hours are currently being calculated.
    rateOfPay : float
        dollar amount this employee makes for each hour of work.

    Returns
    -------
    gross : float
        the total pre-tax pay for this employee during this pay period.

    """
    if isinstance(employee, Employee):
        if isinstance(employee, Manager):
            hours = REGULAR_TIME
        else:
            hours = float(input(f"Enter {employee.getName()}'s hours for this pay period: "))
        if hours <= REGULAR_TIME:
            gross = hours * employee.getRate()
        else:
            gross = REGULAR_TIME * employee.getRate() + 1.5 * (hours - REGULAR_TIME) * employee.getRate()
        return gross
    else:
        return 0




def Taxes(gross):
    """
    Calculates net pay after social secturity tax for an employee

    Parameters
    ----------
    gross : float
        the pay amount before taxes.

    Returns
    -------
    net : float
        the pay amount after taxes.

    """
    net = gross - gross * FICA
    return net













