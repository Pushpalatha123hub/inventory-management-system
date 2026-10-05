from database import get_connection


def add_stock():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity to add: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE inventory
        SET quantity = quantity + %s
        WHERE product_id = %s
    """

    cursor.execute(query, (quantity, product_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Stock added successfully!")
    else:
        print("Product not found.")

    cursor.close()
    connection.close()


def remove_stock():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity to remove: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE inventory
        SET quantity = quantity - %s
        WHERE product_id = %s
        AND quantity >= %s
    """

    cursor.execute(
        query,
        (quantity, product_id, quantity)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Stock removed successfully!")
    else:
        print("Not enough stock or product not found.")

    cursor.close()
    connection.close()


def view_inventory():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            p.product_id,
            p.product_name,
            i.quantity
        FROM products p
        JOIN inventory i
            ON p.product_id = i.product_id
        ORDER BY p.product_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\nINVENTORY")
    print("-" * 50)

    for row in rows:
        print(
            f"ID: {row[0]} | "
            f"Product: {row[1]} | "
            f"Stock: {row[2]}"
        )

    cursor.close()
    connection.close()