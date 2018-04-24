# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:45:27 2018

@author: jon_c
"""

import numpy as np

import numpy as np

def angular_wave_func(m,l,theta,phi):
    y = 0
    if l == 0 and m ==0:
        y = np.sqrt(1/(4*np.pi)) + 0j
        y = round(y,5)
    
    if l == 1 and m ==1:
        y = -np.sqrt(3/(8*np.pi)) * np.sin(theta) * np.exp((1j*phi))
        y = round(y,5)
    
    if l == 1 and m == 0:
        y = np.sqrt(3/ (4*np.pi)) * np.cos(theta) + 0j
        y = round(y,5)
    
    if l == 1 and m == -1:
        y = np.sqrt(3/(8*np.pi)) * np.sin(theta) * np.exp(((-1j)*phi))
        y = round(y,5)
    
    if l == 2 and m == 2:
        y = np.sqrt(15/(32*np.pi)) * np.sin(theta)**2 * np.exp(1j * (2 * phi))
        y = round(y,5)
    
    if l == 2 and m == 1:
        y = -np.sqrt(15/(8*np.pi)) * np.cos(theta) * np.sin(theta) * np.exp(1j * phi)
        y = round (y,5)
    
    if l == 2 and m == 0:
        y = np.sqrt(5/(16*np.pi)) * ((3 * (np.cos(theta)**2)) - 1 ) + 0j
        y = round(y,5)
    
    if l == 2 and m == -1:
        y = np.sqrt(15/(8*np.pi)) * np.cos(theta) * np.sin(theta) * np.exp(-1j * phi)
        y = round(y,5)
    
    if l == 2 and m == -2:
        y = np.sqrt(15/(32*np.pi)) * (np.sin(theta)**2) * np.exp(-1j * (2*phi))
        y = round(y,5)
    
    if l == 3 and m == 3:
        y = - np.sqrt(35/(64*np.pi)) * (np.sin(theta)**3) * np.exp(1j * (3*phi))
        y = round(y,5)
    
    if l == 3 and m == 2:
        y = np.sqrt(105/(32*np.pi)) * np.cos(theta) * (np.sin(theta)**2) * np.exp(1j * (2*phi))
        y = round(y,5)
    
    if l == 3 and m == 1:
        y = -np.sqrt(21/(64*np.pi)) * np.sin(theta) * (5*(np.cos(theta)**2)-1) * (np.exp(1j * phi))
        y = round(y,5)
    
    if l == 3 and m == 0:
        y = np.sqrt(7/(16*np.pi)) * (5*(np.cos(theta)**3) - 3 * np.cos(theta)) +0j
        y = round(y,5)
    
    if l == 3 and m == -1:
        y = np.sqrt(21/(64*np.pi)) * np.sin(theta) * (5*(np.cos(theta)**2)-1) * (np.exp(-1j * phi))
        y = round(y,5)
    
    if l == 3 and m == -2:
       y = np.sqrt(105/(32*np.pi)) * np.cos(theta) * (np.sin(theta)**2) * np.exp(-1j * (2 * phi))
       y = round(y,5)
    
    if l == 3 and m == -3:
        y = np.sqrt(35/(64*np.pi)) * (np.sin(theta)**3) * np.exp(-1j * (3*phi))
        y = round(y,5)
    return y


import numpy as np

def angular_wave_func(m,l,theta,phi):
    y = 0
    if l == 0 and m ==0:
        y = np.sqrt(1/(4*np.pi)) + 0j
        y = round(y,5)
    
    if l == 1 and m ==1:
        y = -np.sqrt(3/(8*np.pi)) * np.sin(theta) * np.exp((1j*phi))
        y = round(y,5)
    
    if l == 1 and m == 0:
        y = np.sqrt(3/ (4*np.pi)) * np.cos(theta) + 0j
        y = round(y,5)
    
    if l == 1 and m == -1:
        y = np.sqrt(3/(8*np.pi)) * np.sin(theta) * np.exp(((-1j)*phi))
        y = round(y,5)
    
    if l == 2 and m == 2:
        y = np.sqrt(15/(32*np.pi)) * np.sin(theta)**2 * np.exp(1j * (2 * phi))
        y = round(y,5)
    
    if l == 2 and m == 1:
        y = -np.sqrt(15/(8*np.pi)) * np.cos(theta) * np.sin(theta) * np.exp(1j * phi)
        y = round (y,5)
    
    if l == 2 and m == 0:
        y = np.sqrt(5/(16*np.pi)) * ((3 * (np.cos(theta)**2)) - 1 ) + 0j
        y = round(y,5)
    
    if l == 2 and m == -1:
        y = np.sqrt(15/(8*np.pi)) * np.cos(theta) * np.sin(theta) * np.exp(-1j * phi)
        y = round(y,5)
    
    if l == 2 and m == -2:
        y = np.sqrt(15/(32*np.pi)) * (np.sin(theta)**2) * np.exp(-1j * (2*phi))
        y = round(y,5)
    
    if l == 3 and m == 3:
        y = - np.sqrt(35/(64*np.pi)) * (np.sin(theta)**3) * np.exp(1j * (3*phi))
        y = round(y,5)
    
    if l == 3 and m == 2:
        y = np.sqrt(105/(32*np.pi)) * np.cos(theta) * (np.sin(theta)**2) * np.exp(1j * (2*phi))
        y = round(y,5)
    
    if l == 3 and m == 1:
        y = -np.sqrt(21/(64*np.pi)) * np.sin(theta) * (5*(np.cos(theta)**2)-1) * (np.exp(1j * phi))
        y = round(y,5)
    
    if l == 3 and m == 0:
        y = np.sqrt(7/(16*np.pi)) * (5*(np.cos(theta)**3) - 3 * np.cos(theta)) +0j
        y = round(y,5)
    
    if l == 3 and m == -1:
        y = np.sqrt(21/(64*np.pi)) * np.sin(theta) * (5*(np.cos(theta)**2)-1) * (np.exp(-1j * phi))
        y = round(y,5)
    
    if l == 3 and m == -2:
       y = np.sqrt(105/(32*np.pi)) * np.cos(theta) * (np.sin(theta)**2) * np.exp(-1j * (2 * phi))
       y = round(y,5)
    
    if l == 3 and m == -3:
        y = np.sqrt(35/(64*np.pi)) * (np.sin(theta)**3) * np.exp(-1j * (3*phi))
        y = round(y,5)
    return y



















