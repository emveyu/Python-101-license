# -*- coding: utf-8 -*-
"""
Created on Aug 03 2022
@author: Yun-Hsuan Kuo
"""

import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter import filedialog as fd
import os

class load_tool:
    def txt_load(start_text='_start_', spacer=' ', wait=0, columnum=2):
        '''
        Input: GUI loading
        Output: column_1 [list], column_2 [list]
        '''
        output_directory = 'plots'
        start_flag = False
        # GUI load file
        Tk().withdraw()
        file = fd.askopenfilename()
        filename = os.path.split(file)[1]
        filefolder = os.path.split(file)[0]
        if (filename==''):
            print('No file is selected.')
            return 
        output_folder = os.path.join(filefolder, output_directory)
        if not os.path.isdir(output_folder):   
            os.mkdir(output_folder) 
        # Loading 
        x = []
        y = []
        with open(file) as f1:
            print('Loading '+filename+'...')
            for line in f1.readlines():
                if (start_text in line) or (start_text=='_start_'): 
                    start_flag = True
                if wait<=0: 
                    s = line.split(spacer)
                    if len(s)<columnum: 
                        break
                    x.append(float(s[0]))
                    y.append(float(s[1]))
                if start_flag:
                    wait=wait-1
            return x, y, filename
        
class plot_tool:    
    def curve(x,y,title='',xlabel='',ylable='', width=5, height=3, filenm='plot',linewidth=1,linecolor='#3b61b1', linestyle='-',tfontsize=14, xfontsize=12, yfontsize=12):
        fig, ax = plt.subplots(1, 1, figsize=(width, height), dpi=300) 
        plt.plot(x, y, lw=linewidth, c=linecolor, ls = linestyle, antialiased=True)
        ax.set_xlabel(xlabel, fontsize=xfontsize)
        ax.set_ylabel(ylable, fontsize=yfontsize)
        ax.set_title(f'{title}', fontsize=tfontsize)
        png = filenm + '.png'
        fig.savefig(png, bbox_inches = 'tight')
        print('Ouput png: '+png)
        plt.show()
        plt.close() 
        
        
    def heatmap(x,y,score, width=5, height=5, labelsize=10, barlabelsize=10):
        cmap = sns.color_palette('mako', as_cmap=True)
        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(111)
        c = ax.pcolormesh(score, cmap=cmap, edgecolors='w', linewidths=2)
        cbar = fig.colorbar(c, ax=ax)
   
        ax.set_xticks(np.arange(len(x)) + 0.5)
        ax.set_yticks(np.arange(len(y)) + 0.5)
        ax.set_xticklabels(x)
        ax.set_yticklabels(y)    
        ax.tick_params(axis='both', which='major', labelsize=labelsize) 
        cbar.ax.tick_params(labelsize=barlabelsize)
                