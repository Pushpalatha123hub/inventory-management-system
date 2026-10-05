from database import get_connection


def add_product():
    name = input("Enter product name: ")
    category_id = int(input("Enter category ID: "))
    supplier_id = int(input("Enter supplier ID: "))
    price = float(input("Enter price: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO products
        (product_name, category_id, supplier_id, price)
        VALUES (%s, %s, %s, %s)
        RETURNING product_id
    """

    cursor.execute(
        query,
        (name, category_id, supplier_id, price)
    )

    product_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    print(f"Product added successfully! ID: {product_id}")


def view_products():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            p.product_id,
            p.product_name,
            c.category_name,
            s.supplier_name,
            p.price
        FROM products p
        JOIN categories c
            ON p.category_id = c.category_id
        JOIN suppliers s
            ON p.supplier_id = s.supplier_id
        ORDER BY p.product_id
    """

    cursor.execute(query)

    products = cursor.fetchall()

    print("\nPRODUCT LIST")
    print("-" * 70)

    if not products:
        print("No products found.")
    else:
        for product in products:
            print(
            f"ID: {product[0]} | "
            f"Name: {product[1]} | "
            f"Category: {product[2]} | "
            f"Supplier: {product[3]} | "
            f"Price: ₹{product[4]}"
        )

    cursor.close()
    connection.close()


def update_product():
    product_id = int(input("Enter product ID: "))
    new_price = float(input("Enter new price: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE products
        SET price = %s
        WHERE product_id = %s
    """

    cursor.execute(query, (new_price, product_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Product updated successfully!")
    else:
        print("Product not found.")

    cursor.close()
    connection.close()


def delete_product():
    product_id = int(input("Enter product ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM products
        WHERE product_id = %s
    """

    cursor.execute(query, (product_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Product deleted successfully!")
    else:
        print("Product not found.")

    cursor.close()
    connection.close()