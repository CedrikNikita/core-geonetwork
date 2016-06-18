# -*- coding: utf-8 -*-
import time
import sys
import re
import wget
import os.path
from time import sleep
from time import strptime


import pdf2txt
from XmlGenerator import generateXml, Fields
from FieldsExtractorEng import parsePdfEng

#TODO: parse title
#TODO: cut ending (bibliography) while searching for keywords
#TODO: language checker
#TODO: Don't use wget. Use either urllib2 or urlgrabber instead.
#http://stackoverflow.com/questions/2467609/using-wget-via-python
#TODO: Database?
#TODO: Russian search
#TODO: period of time
#TODO: geonetwork
#TODO: else variant

#fields
#TODO: denominator


#TODO:
#[16.04.2016 22:28:31] Денис Давидюк: Вот ссылки на проект по распознаванию публикаций, с которым мне предлагали работать:
#https://github.com/CeON/CERMINE
#http://cermine.ceon.pl/index.html -- здесь можно прямо загрузить pdf и посмотреть результат распознавания
#[16.04.2016 22:29:23] Денис Давидюк: Вот ещё есть презентация:
#http://cermine.ceon.pl/static/docs/slides.pdf




#Проверка аргументов/Загрузка файла/Проверка сущестование файла

if len(sys.argv) < 2:
  print('Error: No input files')
  sys.exit()

pdf = sys.argv[1]

url = re.search('^(https?:\/\/)([\w\.]+)\.([a-z]{2,6}\.?)(\/[\w\.]*)*\/?$', pdf)
if not url is None:
  #urllib2?
  filename = wget.download(pdf)
  pdf = url.group(4)[1 :]
  print('\n' + pdf + ' is downloaded')
  
elif not os.path.isfile(pdf):
  print('Error: ' + pdf +' : No such file in directory')
  sys.exit()



#Конвертирование pdf

#string = pdf2txt.main(['',  pdf])
"""if __debug__:  
  fi = open('1.txt', 'r')
  string = fi.read()
  fi.close()
else:"""
string = pdf2txt.main(['',  pdf])

fields = parsePdfEng(string)

fields.url = url
fields.filename = pdf[:-4]

generateXml(fields)