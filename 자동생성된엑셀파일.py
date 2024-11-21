#자동생성된엑셀파일.py
import openpyxl
import random
from openpyxl import Workbook

# 샘플 제품명 리스트
products = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "이어폰", 
    "블루투스 스피커", "공기청정기", "TV", "냉장고", "세탁기"
]

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active
ws.title = "제품 판매 데이터"

# 헤더 추가
headers = ["제품ID", "제품명", "수량", "가격"]
ws.append(headers)

# 100개의 데이터 생성 및 추가
for i in range(1, 101):
    product_id = f"P{str(i).zfill(3)}"  # P001, P002, ... 형식의 ID
    product_name = random.choice(products)
    quantity = random.randint(1, 100)
    price = random.randint(50000, 2000000)
    
    row = [product_id, product_name, quantity, price]
    ws.append(row)

# 열 너비 자동 조정
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

# 파일 저장
wb.save('products.xlsx')
print("products.xlsx 파일이 생성되었습니다.")