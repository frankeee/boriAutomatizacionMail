#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:14:51 2019

@author: franco
"""

#descomentarlineademodificadorbase.py
#instalar python
#ver que el path sea correcto
#ver que el nombre de las carpetas sea correcto
#agregar el pythonpath
#hacer lo del token de gmail

#Puerto 65022

from ftplib import FTP_TLS
import os
import sqlite3
from sqlite3 import Error
from mailPrueba import mailardo
from datetime import date
from datetime import datetime
#Diccionario de referencia, NO ES USADO POR EL PROGRAMA
dicprod =	{
  "00354": "ABAD_NICOLAS_GUILLERMO",
  "00299": "ACCINELLI_LUIS_ANGEL",
  "00329": "ALLEN_MIGUEL_EDUARDO",
  "05002": "ARNAIZ_GRACIELA_DEL_CARMEN",
  "00618": "ASSURLINE_S.R.L.",
  "00245": "BIONDI_OSVALDO_GUILLERMO",
  "00150": "CANNIZZO_JORGE_BENEDICTO",
  "00884": "CASTELLO_MERCURI_S.A.",
  "00296": "CDS_BROKERS_S.A.",
  "01143": "CENTRALIA_BROKERS_S.A.",
  "00266": "CIVRAN_VICTOR_PIO",
  "00011": "CRITERIO_S.A.",
  "00263": "CURA_JULIO_OSCAR",
  "00203": "DENNET_AYLING_S.A.HERRERIA_FERNANDO_ARIEL",
  "00488": "GARCIA_MARIA_SOLEDAD",
  "00036": "LOUSTAUNAU_MARCELO_JORGE",
  "03068": "MULHALL_GRANT_GRACIELA",
  "00656": "NATIONAL_BROKERS_S.A.",
  "00253": "NORDEN_BROKERS_S.A.",
  "00201": "OSES_S.R.L.",
  "00324": "PEREZ_FEIJO_JOSE_MARIA",
  "00098": "PHILIPP_CLAUDIA_SUSANA",
  "00108": "PIÑEIRO_JOSE_RODOLFO",
  "00649": "PRIETO_ROSA_MARIA",
  "00413": "PROD_ASES_DE_SEG_JCA_SRL",
  "00030": "SILBERT_ALEJANDROyJORGE",
  "00589": "TORTORELLI_VICTOR_SERGIO",
  "00659": "VANONI_JUAN_DANIEL",
  "00148": "VILLANUEVA_SANTIAGO_RAUL" 
  }


print(os.getcwd())
#cambia el working directry para estar en archivos filezilla
#os.chdir(os.path.join('/home','franco','Documents','archiveiros'))
print(os.getcwd())
#Conexion a base de datos
def sql_connection():
 
    try:
 
        con = sqlite3.connect('miBase.db')
 
        return con
 
    except Error:
 
        print(Error)
#Devuelve 1 si el codigo de productor existe en la base de datos        
def sql_existe(con,clave):
 
    cursorObj = con.cursor()
 
 
    
    cursorObj.execute("SELECT EXISTS(SELECT 1 FROM productores WHERE id='"+clave+"')") 
    
    a = cursorObj.fetchall()
    return a
#Dada una clave retorna el nombre asociado en la base de datos    
def sql_dameNombre(con,clave):
 
    cursorObj = con.cursor()
 
 
    
    cursorObj.execute("SELECT name FROM productores WHERE id='"+clave+"'")
    
    a = cursorObj.fetchall()
    return a
#Dada una clave retorna el mail asociado en la base de datos
def sql_dameMail(con,clave):
 
    cursorObj = con.cursor()
 
 
    
    cursorObj.execute("SELECT mail FROM productores WHERE id='"+clave+"'")
    
    a = cursorObj.fetchall()
    return a

con = sql_connection()

#objeto conexion a servidor
ftp= FTP_TLS() 
ftp.connect(host='144.217.157.48', port=65022, timeout=3000)
ftp.login(user ='Graieb@dominio.com',passwd='Agosto.2019', acct='')
#print(ftp.pwd())
#Lista los nombres de todos los archivos del servidor
juan =ftp.nlst()
print(juan)
#los recorre
for h in juan:
    #chequea si el codigo del archivo pertenece a algun productor de la base de datos
    n = (sql_existe(con,h[-23:-18]))
    r = n[0]
    z = r[0]
    esta = 0;
    #si esta lo manda a su carpeta correspondiente
    if(z == 1):
        cupa = (sql_dameNombre(con,h[-23:-18]))
        es = cupa[0]
        el = es[0]
        os.chdir(os.path.join('C:','\\Users','Franco','Documents','archivosproductores',str(el)))
    #si no esta lo manda a la carpeta noreconocios
    else:
        os.chdir(os.path.join('C:','\\Users','Franco','Documents','archivosproductores','noreconocidos'))

    john = os.listdir(os.getcwd())
#se fija si ya  estan(hay que agregar que vaya a la carpeta de cada socio)
    for files in john:
        if(h == files):
            esta = 1
#si el archvio no esta lo agrega
    if(esta == 0 and (h[-3:]=="pdf" or h[-3:]=="docx" or h[-3:]=="doc" or h[-3:]=="txt")):        
        cmd ='RETR '+h
        f = open(h,'+wb');
            
        def callback(data):
            f.write(data)
        ftp.retrbinary(cmd, callback, blocksize=8192, rest=None)
        f.close()
        if(z==1):
            #manda mail
            mandador = mailardo()
            #retorna mail asociado en la base de datos
            cora = (sql_dameMail(con,h[-23:-18]))
            de = cora[0]
            deus = de[0]
            mandador.mandaMail(h,str(deus))
            #escribe  en el resgistro correspondiente que mando el archivo
            today = str(date.today())
            now = str(datetime.now())
            ei = now[-15:-7]
            os.chdir(os.path.join('C:','\\Users','Franco','Documents','archivosproductores','registros'))
            if(os.path.isfile(today+'.txt')== False):
                archivoFile =  open(today+'.txt','+w')
                archivoFile.write("Archivo "+h+" enviado a "+str(el)+" a las "+ei+" horas.\n")
                archivoFile.close()
            else:
                archivoFile =  open(today+'.txt','a')
                archivoFile.write("Archivo "+h+" enviado a "+str(el)+" a las "+ei+" horas.\n")
                archivoFile.close()
ftp.quit()
con.close()
