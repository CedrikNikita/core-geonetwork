# -*- coding: utf-8 -*-
import time
import sys
import re
import progressbar
import wget
import os.path
from time import sleep
from time import strptime

import geonames
from XmlGenerator import Fields


'''class Object:
  pass
'''
class Editor:
  pass

class Public:
  pass

def parsePdfEng(string):
  sys.stdout.write("title/date/authors ...\n")
  sys.stdout.flush()



  #Title/date 

  edited = re.search(
    '\d+\s*\n*((?:.+\s*\n){0,6})\n*.*Edited\sby\s+\n+(.+?)\s*\n+((?:.+\s*\n){3,5})E-mail\s*:\s*([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})',
     string, re.IGNORECASE)

  pices_template = 0

  if edited:
    pices_template = 1
    #print(title)
    info = re.split("\n\n|\n", edited.group(3).strip())
    #print(info)
    tdate = info[0].strip().split(' ')
    #print (tdate)
    try:
      pub_date = str(tdate[1]) + '-' + str(strptime(tdate[0], len(tdate[0]) > 3 and '%B' or '%b').tm_mon) + '-' + '1T11:06:05'
      #print(date)
    except ValueError:
     #print("Debug: date parse error")
      sys.exit() 
  else:
    edited = re.search('(Edited\sby\s+\n+)(.+?)\s+\n', string, re.IGNORECASE)



  #Поиск координат

  sys.stdout.write("coordinates ...\n")
  sys.stdout.flush()

  #(57.5°N, 175°W)
  coordinates = re.findall('(\d{1,3}\.*\d{0,3})°([N|S])\W*\s*(\d{1,3}[\.,]*\d{0,3})°([W|E])', string)
  #(N57.5°, W175°)
  coordinates = coordinates + re.findall(
              '([N|S])(\d{1,3}\.*\d{0,3})°\W*\s*([W|E])(\d{1,3}[\.,]*\d{0,3})°', string)
  #(+42.0012, +31.0002)
  coordinates = coordinates + re.findall('([\+|\-]\d+\.*\d+)\s*[,|\.]\s*([\+|\-]\d+\.*\d+)', string)
  #55°45′21″ с. ш. 37°37′04″ в. д. 
  coordinates = coordinates + re.findall(
    '(\d{0,3}.?d*?°\d{0,2}[\'′]?\d{0,2}[\"″]?)\s*([с|ю])\.\s*ш\.\s*(\d{0,3}.?d*?°\d{0,2}[\'′]?\d{0,2}[\"″]?)\s*([в|з])\.\s*д\.',
    string)
 #print(coordinates)



  #Поиск географических названий

  #TODO: EntryThreshold
  EntryThreshold = 5

  sys.stdout.write("geonames/keywords ...\n")
  sys.stdout.flush()

  #if pices_template:
  priority_geo, geo, locations = [], [], []
  title = edited.group(1).strip()

  for obj in geonames.Objects:
    for key in obj.keys():
      title_re = re.search(key, title, re.IGNORECASE)
      rest_re = re.search(key, string[edited.end():], re.IGNORECASE)
      if title_re:
       #print(title.lower().count(key.lower()))
        priority_geo.append(key)
        locations.append(obj[key])
      if rest_re and string[edited.end():].lower().count(key.lower()) > EntryThreshold:
        geo.append(key)
        locations.append(obj[key])


 #print('title')
 #print(priority_geo)
 #print('geonames')
 #print(geo)

  if priority_geo and not priority_geo in geonames:
    geonames.extend(priority_geo)



  #Поиск ключевых слов

  keywords = []

  for key in geonames.Keywords:
    title_re = re.search(key, title, re.IGNORECASE)
    rest_re = re.search(key, string[edited.end():], re.IGNORECASE)
    if title_re:
     #print(title.lower().count(key.lower()))
      if not key in keywords:
        keywords.append(key)
  #TODO:5?
    if rest_re and string[edited.end():].lower().count(key.lower()) > EntryThreshold:
      if not key in keywords:
        keywords.append(key)

 #print('keywords')
 #print(keywords)



  #Поиск информации о авторах

  names = re.split(',|and|;', edited.group(2))
  for i in range(len(names)):
    names[i] = re.sub('^\s+', '', names[i])
    names[i] = re.sub('\s+$', '', names[i])

  #print (names)

  editors = [Editor() for i in range(len(names))]

 #print(editors)

  def getEditorInfo(classobj, name):
    classobj.name = name
    local_info = re.search(name + '\s*((?:.+\s*\n){0,8})E-mail\s*:\s*([a-z0-9_\.-]+@[a-z0-9_\.-]+\.[a-z\.]{2,6})',
     string[ : edited.start()] + string[edited.end() : ])
    if local_info:
     #print(local_info.group(0))
      classobj.email = local_info.group(2)

  for i in range(len(names)):
    getEditorInfo(editors[i], names[i])

 #print(editors[1].name)


  title = title.split('\n\n')[-1]

  '''with open('font.html', 'r') as f:
    font = f.read()

  search = re.search('<span[^>]*?>(' + title + '.+?)</span>', font)

 #print(title)
 #print(search.group(0))'''

  #Вывод
  
  extracted = Fields()

  extracted.title = title
  extracted.pub_date = pub_date
  extracted.editors = editors
  extracted.keywords = keywords
  extracted.priority_geo = priority_geo
  extracted.geo = geo
  extracted.locations = locations
  extracted.language = 'eng'

  return extracted