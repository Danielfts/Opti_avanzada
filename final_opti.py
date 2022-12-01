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




population = {} #población
for fila in range(2,111):
        upz = sheet.cell(fila,14).value
        population[upz]= sheet.cell(fila,7).value