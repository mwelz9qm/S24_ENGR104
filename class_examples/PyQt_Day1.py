# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:25:42 2024

@author: mwelz
"""

import sys
from PyQt5.QtWidgets import (QDialog, QLabel, QGridLayout, QDoubleSpinBox,QApplication)


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


 
    #creates a grid for dialog box
        grid = QGridLayout()
        
        #adds stuff to the grid
        grid.addWidget(angleLabel,0,0)
        grid.addWidget(self.angleBox,0,1)
        grid.addWidget(veloLabel,1,0)
        grid.addWidget(self.veloBox,1,1)
        grid.addWidget(heightLabel,2,0)
        grid.addWidget(self.heightBox,2,1)
        
        
    #finalizes the dialog box/form
        self.setLayout(grid)
        self.setWindowTitle("Projectile Motion Fun")
        


# code we need to run the app

app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())



