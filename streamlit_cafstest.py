# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:37:31 2022

@author: user
"""

import os
import subprocess 
from subprocess import Popen, PIPE
import geemap
import geopandas
import streamlit as st
from subprocess import check_output as qx
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import plotly.express as px
import requests

# read and check the file
p = subprocess.Popen(r'C:\Users\user\Desktop\New folder\model.exe',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output, errors = p.communicate()

dat_file = r"C:\Users\user\Desktop\New folder\res.dat"   

with open(dat_file, 'r') as file:
    text = file.read()
    print(text)
    
# conversion .dat file to csv file
with open(dat_file) as dat_file, open('file.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    for line in dat_file:
        row = [field.strip() for field in line.split('|')]
        if len(row) == 3 and row[6] and row[4]:
            csv_writer.writerow(row)    
        
print(csv_writer)  

# Add a title and intro text
st.title('CAFS Model')
st.text('This is a web app to allow the user to run the crop model') 

# Display the model results 
data = pd.read_csv("file.csv") #path folder of the data file
st.write(data) 
         