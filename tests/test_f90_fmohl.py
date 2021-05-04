#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for f90 module `ctef2py.fmohl`."""

import ctef2py

# create an alias for the binary extension cpp module
f90 = ctef2py.fmohl

import numpy as np


def test_f90_fmohl():
    a = 1.0
    b = 1.0
    q = 10.0
    np = 1e6
    assert (f90.fmohl(a,b,q,np) - 5.111281639134099e-07) < 1e-16


#def test_f90_add():
#    x = np.array([0,1,2,3,4],dtype=np.float)
#    shape = x.shape
#    y = np.ones (shape,dtype=np.float)
#    z = np.zeros(shape,dtype=np.float)
#    expected_z = x + y
#    f90.add(x,y,z)
#    assert (z == expected_z).all()

#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_f90_add

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
