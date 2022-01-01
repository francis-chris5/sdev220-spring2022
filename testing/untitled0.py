#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 21:20:16 2021

@author: Christopher S. Francis
@version: Python 3.9.2
"""

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()

X = [[1, 2, 3], [11, 12, 13]]
y = [0, 1]

classifier.fit(X, y)

Z = [[14, 15, 16], [4, 5, 6]]
expected = classifier.predict(Z)

print(expected)

