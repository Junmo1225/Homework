import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication
import sqlalchemy as sa
import pandas as pd

form_class = uic.loadUiType("customer.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn_show.clicked.connect(self.show_btn)
        self.btn_add.clicked.connect(self.add_btn)
        self.btn_edit.clicked.connect(self.edit_btn)
        self.btn_delete.clicked.connect(self.delete_btn)
        self.btn_search.clicked.connect(self.search_btn)
        
        engine = sa.create_engine('mysql://root:django@52.78.162.166:54643/Junmo')
        
        con = engine.connect()
        
        query='select * from customer'
        df = pd.read_sql(query,con)
        print(df.head())
        
        #for row in range(3):
            #for col in range(4):
                #self.tableWidget.setItem(row, col,
                                         #QTableWidgetItem(str(row)+','+str(col)))
    def show_btn(self):
        print('Show button clicked')
    
    def add_btn(self):
        if self.txt_name.text()=='':
            self.warning.setText('이름을 입력하세요')
        if self.txt_phone.text()=='':
            self.warning.setText('핸드폰 번호를 입력하세요')
        print(self.txt_name.text())
        print(self.txt_phone.text())
        print(self.txt_email.text())
    
    def edit_btn(self):
        print('Edit button clicked')
    
    def delete_btn(self):
        print('Delete button clicked')
    
    def search_btn(self):
        print('Search button clicked')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindow = WindowClass()
    
    myWindow.show()
    
    app.exec_()