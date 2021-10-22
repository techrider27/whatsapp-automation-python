# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 16:58:20 2021

@author: Gaurav
"""
import pywhatkit as kit
#take mobile_number
mobileNo=input("enter mobile number with country code\n")
#take message
message=input("enter message\n")
#take hours in 24hr format
hours=int(input("enter time in 24 hrs format\n"))
#take minutes
minutes=int(input("enter minutes in 24 hrs format\n"))
kit.sendwhatmsg(mobileNo, message,hours,minutes)
 