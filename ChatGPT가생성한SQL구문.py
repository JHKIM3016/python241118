import sqlite3
import random

class ElectronicsDatabase:
    """
    SQLite를 사용하여 전자제품 데이터를 관리하는 클래스.
    제품 정보는 제품 ID, 제품명, 가격을 포함하며 데이터 삽입, 수정, 삭제, 조회 기능을 제공합니다.
    """

    def __init__(self, db_name="electronics.db"):
        """
        데이터베이스 초기화 메서드.
        :param db_name: 데이터베이스 파일 이름 (기본값: electronics.db)
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)  # 데이터베이스 연결 생성
        self.create_table()  # 테이블 생성

    def create_table(self):
        """
        제품 정보를 저장하기 위한 테이블 생성 메서드.
        테이블이 이미 존재하면 생성하지 않습니다.
        """
        with self.connection:  # 자동 커밋 모드로 실행
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 제품 고유 ID (자동 증가)
                    product_name TEXT NOT NULL,                    -- 제품 이름
                    price REAL NOT NULL                            -- 제품 가격
                )
            """)

    def insert_product(self, product_name, price):
        """
        제품 데이터를 테이블에 삽입하는 메서드.
        :param product_name: 제품 이름 (문자열)
        :param price: 제품 가격 (실수)
        """
        with self.connection:
            self.connection.execute(
                "INSERT INTO products (product_name, price) VALUES (?, ?)",
                (product_name, price)
            )

    def update_product(self, product_id, product_name=None, price=None):
        """
        기존 제품 데이터를 수정하는 메서드.
        제품 이름, 가격 중 하나 또는 둘 다 수정 가능.
        :param product_id: 수정할 제품의 ID
        :param product_name: 새로운 제품 이름 (기본값: None)
        :param price: 새로운 제품 가격 (기본값: None)
        """
        with self.connection:
            if product_name and price:
                # 제품 이름과 가격을 모두 수정
                self.connection.execute(
                    "UPDATE products SET product_name = ?, price = ? WHERE product_id = ?",
                    (product_name, price, product_id)
                )
            elif product_name:
                # 제품 이름만 수정
                self.connection.execute(
                    "UPDATE products SET product_name = ? WHERE product_id = ?",
                    (product_name, product_id)
                )
            elif price:
                # 제품 가격만 수정
                self.connection.execute(
                    "UPDATE products SET price = ? WHERE product_id = ?",
                    (price, product_id)
                )

    def delete_product(self, product_id):
        """
        특정 제품 데이터를 삭제하는 메서드.
        :param product_id: 삭제할 제품의 ID
        """
        with self.connection:
            self.connection.execute(
                "DELETE FROM products WHERE product_id = ?",
                (product_id,)
            )

    def select_products(self):
        """
        테이블의 모든 제품 데이터를 조회하는 메서드.
        :return: 모든 제품 데이터를 포함하는 리스트 (각 행은 튜플 형태)
        """
        with self.connection:
            cursor = self.connection.execute("SELECT * FROM products")  # 모든 데이터 조회
            return cursor.fetchall()  # 결과를 리스트 형태로 반환

    def close(self):
        """
        데이터베이스 연결을 종료하는 메서드.
        """
        self.connection.close()


# 샘플 데이터 생성 함수
def generate_sample_data(db):
    """
    무작위로 생성된 샘플 데이터를 데이터베이스에 삽입하는 함수.
    :param db: ElectronicsDatabase 클래스 인스턴스
    """
    product_names = [
        "Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard",
        "Mouse", "Printer", "Camera", "Smartwatch", "Headphones"
    ]
    for _ in range(100):
        # 무작위 제품 이름과 가격 생성
        name = random.choice(product_names)
        price = round(random.uniform(50, 2000), 2)  # 랜덤 가격 (50 ~ 2000 사이, 소수점 둘째 자리)
        db.insert_product(name, price)


# 데이터베이스 사용 예제
db = ElectronicsDatabase()  # 데이터베이스 초기화

# 샘플 데이터 삽입
generate_sample_data(db)

# 데이터 조회 (전체 제품 중 상위 10개만 출력)
products = db.select_products()
print(f"Total Products: {len(products)}")
for product in products[:10]:  # 상위 10개만 출력
    print(product)

# 데이터 업데이트 예제
db.update_product(1, product_name="Gaming Laptop", price=1500.99)

# 데이터 삭제 예제
db.delete_product(2)

# 업데이트 후 데이터 조회 (상위 10개 출력)
updated_products = db.select_products()
print("\nUpdated Products:")
for product in updated_products[:10]:
    print(product)

# 연결 닫기
db.close()  # 데이터베이스 연결 종료
