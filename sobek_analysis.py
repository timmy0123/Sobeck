# -*- coding: utf-8 -*-
import os
import numpy as np
import time_bar_create
import export_file

input_folder = input("請輸入資料夾位置")
year = input("請輸入開始年分")
month = input("請輸入開始月分")
day = input("請輸入日期")
hour = input("請輸入幾點開始")
minute = input("請輸入幾分開始")

year,month,day,hour,minute = int(year),int(month),int(day),int(hour),int(minute)

result_path = os.getcwd() + "/Result/"
video_path = result_path + "out/"
word_path = os.getcwd() + "/SimHei.ttf"
if not os.path.isdir(result_path):
  os.mkdir(result_path)
if not os.path.isdir(video_path):
  os.mkdir(video_path)

print("開始讀檔")

max_index = [0]
area_index = [0]
mapdata = []
os.chdir(input_folder)
for i in range(1,434):

  index = []
  if i < 10 :filename = "dm1d000"+str(i)+".asc"
  elif 10 <= i < 100 :filename = "dm1d00"+str(i)+".asc"
  elif 100 <= i :filename = "dm1d0"+str(i)+".asc"
  ascii_grid = np.loadtxt(filename ,skiprows = 6,dtype= float)
  arraytemp = ascii_grid[461:474,568:580]
  for row in range(arraytemp.shape[0]) :
      for column in range(arraytemp.shape[1]) :
          if arraytemp[row,column] > 0: 
              index.append([row,column,arraytemp[row,column]])
              arraytemp[row,column] = arraytemp[row,column]*100
  mapdata.append(arraytemp)
  if len(index) != 0:
      area_index.append(len(index))
      max_val = 0
      for time in range(len(index)):
          arraytemp2 = np.copy(index)
          if arraytemp2[time,2] > max_val:
              max_val = arraytemp2[time,2]
      max_index.append(max_val*100)
  else : 
    max_index.append(0)
    area_index.append(0)

  print("讀取%s"%filename)

time = time_bar_create.time_bar(year,month,day,hour,minute)

out = export_file.output_file(result_path,video_path,word_path,max_index,area_index,time.real_time,mapdata)
