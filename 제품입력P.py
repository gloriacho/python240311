import sqlite3

class ProductDatabase:
    def __init__(self, db_name="products.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL
            )
        """)
        self.conn.commit()

    def insert_product(self, product_id, product_name, price):
        self.cur.execute("""
            INSERT INTO products (product_id, product_name, price)
            VALUES (?, ?, ?)
        """, (product_id, product_name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        self.cur.execute("""
            UPDATE products
            SET price = ?
            WHERE product_id = ?
        """, (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cur.execute("""
            DELETE FROM products
            WHERE product_id = ?
        """, (product_id,))
        self.conn.commit()

    def select_all_products(self):
        self.cur.execute("SELECT * FROM products")
        return self.cur.fetchall()

# 샘플 데이터 추가
if __name__ == "__main__":
    db = ProductDatabase()
    sample_data = [
        (1, "Smartphone", 500),
        (2, "Laptop", 1000),
        (3, "Headphones", 50),
        (4, "Tablet", 300),
        (5, "Smartwatch", 150),
        (6, "Wireless Earbuds", 80),
        (7, "Digital Camera", 400),
        (8, "Gaming Console", 500),
        (9, "Fitness Tracker", 70),
        (10, "Portable Speaker", 50),
        # ... (더 많은 샘플 데이터 추가)
    ]
    for data in sample_data:
        db.insert_product(*data)

    # 전체 제품 목록 출력
    products = db.select_all_products()
    for product in products:
        print(f"Product ID: {product[0]}, Name: {product[1]}, Price: ${product[2]:.2f}")
