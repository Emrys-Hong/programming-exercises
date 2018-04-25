# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 21:57:39 2018

@author: jon_c
"""

#question1
import scipy.constants as c

def deg_to_rad(deg):
    rad = (deg * c.pi) / 180
    return round(rad, 5)
 
def rad_to_deg(rad):
    deg = (rad * 180) / c.pi
    return round(deg, 5)

#question2
import numpy as np 
def spherical_to_cartesian(r,theta,phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return round(x, 5), round(y,5), round(z, 5)
def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/(np.sqrt(x**2 + y**2 + z**2)))
    phi = np.arctan(y/x)
    return round(r, 5), round(theta, 5), round (phi, 5)

#question3
#import numpy as np

def absolute(cnumber):
    cnumber = complex(cnumber.real, cnumber.imag) 
    mag = np.sqrt(cnumber.real**2 + cnumber.imag**2)
    return mag