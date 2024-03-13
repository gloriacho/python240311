import sqlite3

class ProductDatabase:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                price REAL NOT NULL
                            )''')
        self.conn.commit()

    def insert_product(self, product_id, name, price):
        self.cursor.execute('''INSERT INTO products (id, name, price)
                               VALUES (?, ?, ?)''', (product_id, name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        self.cursor.execute('''UPDATE products
                               SET price = ?
                               WHERE id = ?''', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''DELETE FROM products
                               WHERE id = ?''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''SELECT * FROM products
                               WHERE id = ?''', (product_id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()

# 데이터베이스 초기화 및 샘플 데이터 추가
def initialize_database():
    db = ProductDatabase()
    sample_data = [
        (1, 'Laptop', 999.99),
        (2, 'Smartphone', 599.99),
        (3, 'Tablet', 299.99),
        (4, 'Headphones', 149.99),
        (5, 'Monitor', 199.99),
        (6, 'Keyboard', 49.99),
        (7, 'Mouse', 29.99),
        (8, 'Printer', 299.99),
        (9, 'Smartwatch', 199.99),
        (10, 'Camera', 499.99)
    ]
    for data in sample_data:
        db.insert_product(*data)
    db.close_connection()

# 테스트를 위해 데이터베이스 초기화
initialize_database()

# 테스트
db = ProductDatabase()
print("전체 제품 목록:")
for product_id in range(1, 11):
    product = db.select_product(product_id)
    print(f"제품 ID: {product[0]}, 이름: {product[1]}, 가격: {product[2]}")
db.close_connection()
