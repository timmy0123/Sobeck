import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import os 
import cv2
import numpy as np
import glob

class output_file():
    def __init__(self,result_path,video_path,word_path,depth,area,time,mapdata):

        self.result_path = result_path
        self.video_path = video_path
        self.word_path = word_path
        self.depth = depth
        self.area = area
        self.time = time
        self.mapdata = mapdata
        self.csv_create()
        self.line_chart_depth()
        self.line_chart_area()
        self.map_create()
        
    def csv_create(self):
        data_save = np.vstack((self.time, self.depth)).T
        data_save2 = np.vstack((self.time, self.area)).T
        np.savetxt(self.result_path + 'IOT最大淹水深度.csv',data_save,delimiter=',',fmt='%s',header="Time,Flooding depth(m)")
        np.savetxt(self.result_path + '最大淹水面積.csv',data_save2,delimiter=',',fmt='%s',header="Time,Area(m*m)")


    def line_chart_depth(self):

        plt.figure(figsize=(50,30))

        zhfont_title = mpl.font_manager.FontProperties(fname=self.word_path, size=64)
        zhfont_label = mpl.font_manager.FontProperties(fname=self.word_path, size=40)


        xs = [datetime.strptime(d, '%Y-%m-%d-%H-%M') for d in self.time]
        plt.plot(xs, self.depth,linewidth=6,label = "0", color = "b")
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.gca().xaxis.set_major_locator(mdates.HourLocator())
        plt.legend(loc = "best", fontsize=50)

        plt.title(u"最大淹水深度", fontproperties=zhfont_title , y = 1.03)
        plt.xlabel(u"日期", fontproperties=zhfont_label)
        plt.ylabel(u"淹水深度(m)", fontproperties=zhfont_label)

        plt.gcf().autofmt_xdate()  
        plt.ylim(ymin=0)
        plt.xlim(xmin=datetime(2016, 9, 27, 0, 0),xmax=datetime(2016, 9, 30, 0, 0))
        plt.xticks(rotation='vertical',fontsize=24)
        plt.yticks(fontsize=30)
        ax = plt.gca()
        ax.yaxis.set_label_coords(-0.053, 0.5)
        ax.xaxis.set_label_coords(0.5, -0.162)
        plt.grid(True, ls='--')
        save_file_path = self.result_path + "IOT最大淹水深度.png"
        plt.savefig(save_file_path)
        plt.show()
        plt.close()
    
    def line_chart_area(self):
        plt.figure(figsize=(50,40))

        zhfont_title = mpl.font_manager.FontProperties(fname=self.word_path, size=64)
        zhfont_label = mpl.font_manager.FontProperties(fname=self.word_path, size=40)


        xs = [datetime.strptime(d, '%Y-%m-%d-%H-%M') for d in self.time]
        plt.plot(xs, self.area,linewidth=6)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.gca().xaxis.set_major_locator(mdates.HourLocator())


        plt.title(u"最大淹水面積", fontproperties=zhfont_title , y = 1.02)
        plt.xlabel(u"日期", fontproperties=zhfont_label)
        plt.ylabel(u"淹水面積(平方米)", fontproperties=zhfont_label)
        
        plt.ylim(ymin=0)
        plt.xlim(xmin=datetime(2016, 9, 27, 0, 0),xmax=datetime(2016, 9, 30, 0, 0))
        plt.xticks(rotation='vertical',fontsize=24)
        plt.yticks(fontsize=30)
        ax = plt.gca()
        ax.yaxis.set_label_coords(-0.053, 0.5)
        ax.xaxis.set_label_coords(0.5, -0.115)
        plt.grid(True, ls='--')
        save_file_path = self.result_path + "IOT淹水面積.png"
        plt.savefig(save_file_path)
        plt.show()
        plt.close()

    
    def map_create(self):
        zhfont_title = mpl.font_manager.FontProperties(fname=self.word_path, size=40)
        zhfont_label = mpl.font_manager.FontProperties(fname=self.word_path, size=16)
        zhfont_label_colorbar = mpl.font_manager.FontProperties(fname=self.word_path, size=20)

        filepath = []
        minute_start = 0
        hour_start = 0
        day_start = 27

        num = 0
        for i in self.mapdata:


            data = i
            plt.figure(figsize=(15,15))
            im = plt.imshow(data)

            plt.title(u"淹水影片", fontproperties=zhfont_title ,y = 1.02)
            plt.xlabel(u"格子 column", fontproperties=zhfont_label)
            plt.ylabel(u"格子 row", fontproperties=zhfont_label)
            plt.text(-2, -1.35, self.time[num] , fontsize= 20)


            ax = plt.gca()
            ax.yaxis.set_label_coords(-0.0353, 0.5)
            ax.xaxis.set_label_coords(0.5, -0.055)

            ax.yaxis.set_major_locator(MultipleLocator(1))
            ax.xaxis.set_major_locator(MultipleLocator(1))
            ax.xaxis.set_minor_locator(AutoMinorLocator(2))
            ax.yaxis.set_minor_locator(AutoMinorLocator(2))
            ax.grid(which='minor', ls='--',color = "red")
            

            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.25)
            plt.clim(35, 65)
            cbar = plt.colorbar(im,cax=cax)
            cbar.set_label('淹水深度(cm)', rotation=270, fontproperties=zhfont_label_colorbar , y = 0.5 , labelpad = 25)

            
            plt.savefig(self.video_path+str(num)+'.png')
            filepath.append(self.video_path+str(num)+'.png')
            plt.close()
            num+=1


        img_array = []
        for filename in filepath:
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
        
        out = cv2.VideoWriter(self.result_path+'map.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
