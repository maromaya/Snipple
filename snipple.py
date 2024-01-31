# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap, QFont, QPainter, QColor
from PyQt5.QtCore import Qt
import sys
import modelAlpha
import modelH
import Image_create
  
# creating a class
# that inherits the QDialog class

class window2(QDialog):
    def __init__(self,h,alpha):
        super().__init__()
        self.setWindowTitle("Snipple Results")
        self.setGeometry(700,700,700,700)
        screenSize = app.desktop().availableGeometry()
        self.move(screenSize.width()//2 - self.width()//2, screenSize.height()//2 - self.height()//2)

        font = QFont()
        font.setPointSize(20)
        font.setFamily("Tahoma")
        font.setBold
        st1 = "Alpha="+str(alpha)+"  , Height="+str(h)
        label1=QLabel(st1,self)
        label1.setFont(font)
        Image_create.plot_results(alpha,h)

        layout=QVBoxLayout()
        label2 = QLabel()
        pixmap=QPixmap('plot.jpg')
        label2.setPixmap(pixmap)
        layout.addWidget(label2)
        layout.addWidget(label1)
        self.setLayout(layout)
        

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
  
        # setting window title
        self.setWindowTitle("Snipple")
  
        # setting geometry to the window
        self.setGeometry(600, 600, 600, 600)
        screenSize = app.desktop().availableGeometry()
        self.move(screenSize.width()//2 - self.width()//2, screenSize.height()//2 - self.height()//2)

        layout=QVBoxLayout()
        label2 = QLabel()
        pixmap=QPixmap('Snipple.png')
        label2.setPixmap(pixmap)
        label2.setFixedSize(600,600)
        label2.setScaledContents(True)
        label2.setWordWrap(True)
        layout.addWidget(label2)
        layout.setSpacing(10)
        layout.setContentsMargins(10,10,10,10)
        self.setLayout(layout)

        # creating a dialog button for ok and cancel
        self.buttonBox = QPushButton("Let's Snipple!")
        # self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        # self.buttonBox.setVisible(True)
        # self.buttonBox.show()
        self.buttonBox.clicked.connect(self.create_form_window)
        # self.buttonBox.accepted.connect(self.create_form_window)
  
        # adding action when form is rejected
        # self.buttonBox.rejected.connect(self.reject)
        layout.addWidget(self.buttonBox)

    def create_form_window(self):
        self.w=Window()
        self.w.show()
        self.hide()
  




class Window(QDialog):
  
    # constructor
    def __init__(self):
        super().__init__()
  
        # setting window title
        self.setWindowTitle("Snipple")
  
        # setting geometry to the window
        self.setGeometry(600, 600, 600, 600)
        screenSize = app.desktop().availableGeometry()
        self.move(screenSize.width()//2 - self.width()//2, screenSize.height()//2 - self.height()//2)
        
  
        # creating a group box
        self.formGroupBox = QGroupBox("New patient")
  
        # creating spin box to select volume
        self.BreastOriginalVolumeSpinBar = QSpinBox()
        self.BreastOriginalVolumeSpinBar.setRange(500,3000)   
        self.BreastFinalVolDoubleSpinBar = QDoubleSpinBox()
        self.BreastFinalVolDoubleSpinBar.setRange(240,700)    
        self.SkinElasticSpinBar = QSpinBox()
        self.SkinElasticSpinBar.setRange(100,200)
        self.weight = QSpinBox()
        self.weight.setRange(50,150)
        self.Height = QSpinBox()
        self.Height.setRange(150,200)
        self.RightbreastWidth = QSpinBox()
        self.RightbreastWidth.setRange(15,35)
        self.LeftbreastWidth = QSpinBox()
        self.LeftbreastWidth.setRange(15,35)
        self.RBreastHeight = QSpinBox()
        self.RBreastHeight.setRange(13,35)
        self.LBreastHeight = QSpinBox()
        self.LBreastHeight.setRange(13,35)
        self.NiptoClav = QSpinBox()
        self.NiptoClav.setRange(20,32)
        self.Niptost = QSpinBox()
        self.Niptost.setRange(23,50)
        self.Niptoimf = QSpinBox()
        self.Niptoimf.setRange(6,10)
        self.betweennips = QSpinBox()
        self.betweennips.setRange(7,15)
        self.fibro = QSpinBox()
        self.fibro.setRange(1,4)
        self.age = QSpinBox()
        self.age.setRange(25,70)
  
        # # creating combo box to select degree
        # self.degreeComboBox = QComboBox()
  
        # # adding items to the combo box
        # self.degreeComboBox.addItems(["BTech", "MTech", "PhD"])
  
        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.acceptBtn)
  
        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)
  
        # creating a vertical layout
        mainLayout = QVBoxLayout()
  
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
  
        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)
  
        # setting lay out
        self.setLayout(mainLayout)

    def window2(self,h,alpha):
        self.w=window2(h,alpha)
        self.w.show()
        
        self.hide()






    


  
    # get info method called when form is accepted
    def getInfo(self):
        x_vec= []
        x_vec.append(int(self.age.text()))
        x_vec.append(int(self.BreastOriginalVolumeSpinBar.text()))
        x_vec.append(float(self.BreastFinalVolDoubleSpinBar.text()))
        x_vec.append(int(self.SkinElasticSpinBar.text()))
        x_vec.append(int(self.weight.text()))
        x_vec.append(int(self.Height.text()))
        x_vec.append(int(self.RightbreastWidth.text()))
        # x_vec.append(self.LeftbreastWidth.text())
        x_vec.append(int(self.RBreastHeight.text()))
        # x_vec.append(self.LBreastHeight.text())
        x_vec.append(int(self.NiptoClav.text()))
        x_vec.append(int(self.Niptost.text()))
        x_vec.append(int(self.Niptoimf.text()))
        x_vec.append(int(self.betweennips.text()))
        x_vec.append(int(self.fibro.text()))
        return x_vec


    def acceptBtn(self):
        x_vec=self.getInfo()
        print(x_vec)
        alpha = modelAlpha.getPrediction(x_vec)
        h = modelH.getPrediction(x_vec)/10
        # print("alpha is:",alpha,"h is:",h)
        self.hide()
        self.window2(h,alpha)
        # closing the window
        self.close()



  
    # creat form method
    def createForm(self):
  
        # creating a form layout
        layout = QFormLayout()
  
        # adding rows
        # for name and adding input text
  
        # for degree and adding combo box
        # layout.addRow(QLabel("Degree"), self.degreeComboBox)
  
        # for age and adding spin box
        layout.addRow(QLabel("Age"), self.age)
        layout.addRow(QLabel("Breast Original Volume (in CC)"), self.BreastOriginalVolumeSpinBar)
        layout.addRow(QLabel("Breast Final Volume (in CC)"), self.BreastFinalVolDoubleSpinBar)
        layout.addRow(QLabel("Skin Elasticity"), self.SkinElasticSpinBar)
        layout.addRow(QLabel("Weight (in KG)"), self.weight)
        layout.addRow(QLabel("Height (in CM)"), self.Height)
        layout.addRow(QLabel("Right Breast Width (in CM)"), self.RightbreastWidth)
        layout.addRow(QLabel("Left Breast Width (in CM)"), self.LeftbreastWidth)
        layout.addRow(QLabel("Right Breast Height (in CM)"), self.RBreastHeight)
        layout.addRow(QLabel("Left Breast Height (in CM)"), self.LBreastHeight)
        layout.addRow(QLabel("Nipple to Clavicle (in CM)"), self.NiptoClav)
        layout.addRow(QLabel("Nipple to Sternal Notch (in CM)"), self.Niptost)
        layout.addRow(QLabel("Nipple to IMF (in CM)"), self.Niptoimf)
        layout.addRow(QLabel("Distance Between Nipples (in CM)"), self.betweennips)
        layout.addRow(QLabel("Fibrogranular tissue (1-4)"), self.fibro)

        # layout.addRow(QLabel("Breast Final Volume"), self.BreastFinalVolumeSpinBar)
  
        # setting layout
        self.formGroupBox.setLayout(layout)
  



# main method
if __name__ == '__main__':
  
    # create pyqt5 app
    app = QApplication(sys.argv)
  
    # create the instance of our Window
    window = MainWindow()
  
    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())