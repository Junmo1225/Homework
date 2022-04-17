import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("C:\\Users\\Junmo\\Desktop\\Designer\\IDAndPassword.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.print_btn)
        self.apple.clicked.connect(self.radio_btn)
        self.amazon.clicked.connect(self.radio_btn)
        self.tesla.clicked.connect(self.radio_btn)
        self.comboBox.currentIndexChanged.connect(self.printComboBoxItem)
        self.listWidget.itemClicked.connect(self.chkItemClicked)
        
        sports = ['Golf','Soccer','Baseball']
        for i in sports:
            self.comboBox.addItem(i)
            
        sports = ['Golf','Soccer','Baseball']
        for i in sports:
            self.listWidget.addItem(i)
            
        for row in range(3):
            for col in range(4):
                self.tableWidget.setItem(row,col, 
                                         QTableWidgetItem(str(row)+','+str(col)))

    def radio_btn(self):
        companies = ['Apple','Amazon','Tesla']
        if self.apple.isChecked():
            self.lbCompany.setText(f'{companies[0]} selected')
        elif self.amazon.isChecked():
            self.lbCompany.setText(f'{companies[1]} selected')
        elif self.tesla.isChecked():
            self.lbCompany.setText(f'{companies[2]} selected')

    def print_btn(self):
        #print("Button Pressed")
        self.LBPrint.setText('Print Pressed')
        
    def printComboBoxItem(self):
        print(self.comboBox.currentText())
        
    def chkItemClicked(self):
        print(self.listWidget.currentItem().text())

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()