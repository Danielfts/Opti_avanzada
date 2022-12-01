import pandas as pd
import gurobipy as gp 
from gurobipy import GRB
import pandas as pd
import numpy as np 
import pyflakes
from openpyxl import*






book = load_workbook("/Users/spheal/Desktop/a.xlsx")
sheet = book.active 
datos = book.active




demanda = {} #demanda
for fila in range(6,12):
        indice = sheet.cell(fila,14).value
        vector[upz]= sheet.cell(fila,7).value
