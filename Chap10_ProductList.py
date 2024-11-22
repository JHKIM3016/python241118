import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3

# 데이터베이스 연결 및 테이블 생성
con = sqlite3.connect("ProductList.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Price INTEGER NOT NULL
    );
""")

# 디자인 파일 로드
form_class = uic.loadUiType("ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 초기값 셋팅
        self.id = 0
        self.name = ""
        self.price = 0

        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 엔터 키로 다음 필드 이동
        self.prodID.returnPressed.connect(self.focusNextChild)
        self.prodName.returnPressed.connect(self.focusNextChild)
        self.prodPrice.returnPressed.connect(self.focusNextChild)

        # 초기 데이터 로드
        self.getProduct()

    def addProduct(self):
        self.name = self.prodName.text().strip()
        self.price = self.prodPrice.text().strip()

        if not self.name or not self.price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품명과 가격을 올바르게 입력하세요.")
            return

        cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", 
                    (self.name, int(self.price)))
        con.commit()
        self.getProduct()
        QMessageBox.information(self, "완료", "제품이 추가되었습니다.")

    def updateProduct(self):
        self.id = self.prodID.text().strip()
        self.name = self.prodName.text().strip()
        self.price = self.prodPrice.text().strip()

        if not self.id.isdigit() or not self.name or not self.price.isdigit():
            QMessageBox.warning(self, "입력 오류", "올바른 ID, 제품명, 가격을 입력하세요.")
            return

        cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", 
                    (self.name, int(self.price), int(self.id)))
        con.commit()
        self.getProduct()
        QMessageBox.information(self, "완료", "제품이 수정되었습니다.")

    def removeProduct(self):
        self.id = self.prodID.text().strip()

        if not self.id.isdigit():
            QMessageBox.warning(self, "입력 오류", "올바른 ID를 입력하세요.")
            return

        cur.execute("DELETE FROM Products WHERE id = ?;", (int(self.id),))
        con.commit()
        self.getProduct()
        QMessageBox.information(self, "완료", "제품이 삭제되었습니다.")

    def getProduct(self):
        self.tableWidget.setRowCount(0)  # 기존 행 초기화

        cur.execute("SELECT * FROM Products;")
        rows = cur.fetchall()
        for row_idx, row in enumerate(rows):
            self.tableWidget.insertRow(row_idx)
            self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(str(row[2])))

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
