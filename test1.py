#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import genetico
from random import seed

class Testprueba (unittest.TestCase):
    
    def test_crossover(self):
        self.assertEqual(genetico.cruzamiento([0,0,0,0,0,0],[1,1,1,1,1,1]),[[0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0]])
        self.assertEqual(genetico.cruzamiento([0,0,0,0,0,0],[1,1,1,1,1,1]),[[0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0]])
        self.assertEqual(genetico.cruzamiento([0,0,0,0,0,0],[1,1,1,1,1,1]),[[0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0]])

    def test_mutacion(self):
        self.assertEqual(genetico.mutacion([0,0,0,0,0,0],20),[0, 1, 0, 0, 0, 0])
        self.assertEqual(genetico.mutacion([0,0,0,0,0,0],20),[0, 0, 0, 1, 0, 1])
        self.assertEqual(genetico.mutacion([0,0,0,0,0,0],20),[0, 0, 0, 0, 0, 1])

if __name__ == '__main__':
    seed(1)
    unittest.main()

