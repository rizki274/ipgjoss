# -*- coding: utf-8 -*-
from xlpy import *

xl = XL('6287780855294')
r = xl.loginWithOTP('SER39K')
if(r != False):
    print(xl.purchasePackage('Service ID')['message'])
else:
    print("Login failed try again")
