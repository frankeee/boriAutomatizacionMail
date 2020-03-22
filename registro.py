# -*- coding: utf-8 -*-
from datetime import date
from datetime import datetime
import os


today = str(date.today())
print(today)

now = str(datetime.now())
ei = now[-15:-7]
print(ei)
os.chdir(os.path.join('C:','\\Users','Franco','Documents','archivosproductores','registros'))

print(os.path.isfile(today+'.txt'))    
#print(os.path.isdir('dist'))

