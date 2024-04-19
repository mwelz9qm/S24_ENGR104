# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:25:42 2024

@author: mwelz
"""

import sys
from PyQt5.QtWidgets import (QDialog, QLabel, QGridLayout, QDoubleSpinBox,QApplication)
import numpy as np

#dialog for projectile motion data
class Form(QDialog):
    
    def __init__(self):   #constructor
        super().__init__() #calls the QDialog constructor
        
        #inputs
        
        #add launch angle double spinbox and label
        
        self.angleBox = QDoubleSpinBox()
        self.angleBox.setRange(0,90)
        self.angleBox.setValue(45)
        self.angleBox.setDecimals(2)
        self.angleBox.setSuffix(" degrees")     
 
        angleLabel = QLabel("Initial Launch Angle")    
        
        
        #add initial velocity spinboxx and label

        self.veloBox = QDoubleSpinBox()
        self.veloBox.setRange(0,200)
        self.veloBox.setValue(0)
        self.veloBox.setDecimals(2)
        self.veloBox.setSuffix(" m/s")     
 
        veloLabel = QLabel("Initial Velocity") 

        #add initial height spinboxx and label

        self.heightBox = QDoubleSpinBox()
        self.heightBox.setRange(0,200)
        self.heightBox.setValue(0)
        self.heightBox.setDecimals(2)
        self.heightBox.setSuffix(" m")     
 
        heightLabel = QLabel("Initial Height") 


    #outputs

        self.impactTime = QLabel() #display of the time label
        timeLabel = QLabel("Time of Impact")
        self.maxHeight = QLabel() #tracking the max height attained
        maxHeightLabel = QLabel("Max Height Attained")
        self.distance = QLabel() #tracking the distance travelled
        distanceLabel = QLabel("Horizontal Distance Traveled")
        


 
    #creates a grid for dialog box
        grid = QGridLayout()
        
        #adds inputs to the grid
        grid.addWidget(angleLabel,0,0)
        grid.addWidget(self.angleBox,0,1)
        grid.addWidget(veloLabel,1,0)
        grid.addWidget(self.veloBox,1,1)
        grid.addWidget(heightLabel,2,0)
        grid.addWidget(self.heightBox,2,1)
        
        #add outputs to the grid
        
        grid.addWidget(timeLabel,0,2)
        grid.addWidget(self.impactTime,0,3)
        grid.addWidget(maxHeightLabel,1,2)
        grid.addWidget(self.maxHeight,1,3)
        grid.addWidget(distanceLabel,2,2)
        grid.addWidget(self.distance,2,3)
        
        
        self.heightBox.valueChanged.connect(self.updateUi)
        self.angleBox.valueChanged.connect(self.updateUi)
        self.veloBox.valueChanged.connect(self.updateUi)
        
        
    #finalizes the dialog box/form
        self.setLayout(grid)
        self.setWindowTitle("Projectile Motion Fun")
        

    def updateUi(self):
        v_x = self.veloBox.value() * np.cos(self.angleBox.value() * np.pi/180) #calculates horizontal velo
        v_y = self.veloBox.value() * np.sin(self.angleBox.value() * np.pi/180) # calculates vertical velo
        g = 9.81 #gravity in m/s^2
        impact = (-v_y - np.sqrt(v_y**2 + 2 * g * self.heightBox.value()))/(-g) #impact time
        hDistance = v_x * impact #horizontal distance traveled
        high_time = v_y/g #time of the high point
        maxH = -g*(high_time**2)/2 + v_y*high_time + self.heightBox.value() #high point
        
        
        #setting the display values
        self.impactTime.setText("{0:03f} s".format(impact)) 
        self.maxHeight.setText("{0:03f} m".format(maxH))
        self.distance.setText("{0:03f} m".format(hDistance))
        

# code we need to run the app

app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())



