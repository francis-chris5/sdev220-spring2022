# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:18:57 2022

@author: c.s.francis

@version: Python 3.10.2

@summary: A collection of constants and functions to calculate payroll for a business
"""


FICA = 0.12
REGULAR_TIME = 40


def GrossPay(employeeName, rateOfPay):
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
    hours = float(input(f"Enter {employeeName}'s hours for this pay period: "))
    if hours <= REGULAR_TIME:
        gross = hours * rateOfPay
    else:
        gross = REGULAR_TIME * rateOfPay + 1.5 * (hours - REGULAR_TIME) * rateOfPay
    return gross




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













