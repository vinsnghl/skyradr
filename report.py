from datetime import datetime
import pandas as pd
import math
import json
from time import sleep
import os
import sys

from datetime import date

#df = pd.read_json('/home/veeru/inthebox.json', lines=True,orient='records')
#df = pd.read_json('/home/veeru/inthebox.json')
#print(df)

######### REPORT INIT ###########

todayoutputdir = sys.argv[1]
print(todayoutputdir)
output_aircraftinbox_json = open(sys.argv[1], 'r')
output_aircraftinbox_html = open(sys.argv[2], 'r')

output_aircraftinbox_html_final = open

reporthtml = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<style>
table, th, td {
  border: 2px solid black;
  border-collapse: collapse;
}
</style>
</head>
<body>

<h1 align = "center" >Report of airplanes flying over head</h1>
<p align = "center">This is a paragraph.</p>

<table style="width:70% ; margin-left: auto; margin-right: auto;">
""" 
output_aircraftinbox_html.writelines(reporthtml + '\n')
output_aircraftinbox_html.flush() 



"""
today = date.today()
todaysdate = today.strftime("%m%d%Y")
print(todaysdate)

recentplanes = {}
now1 = datetime.now()
recentplanes['abc123'] = now1
sleep(3)
now2 = datetime.now()
recentplanes['abc124'] = now2

print((now2 - now1).seconds)
print(recentplanes)

recentplanes2 = {}
for planes in recentplanes:
    print( (datetime.now() - recentplanes[planes]).seconds )
    recentplanes2[planes] = recentplanes[planes] 

print(recentplanes2)
recentplanes = recentplanes2
print(recentplanes)
"""



