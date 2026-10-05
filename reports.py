from database import get_connection


def inventory_report():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            p.product_name,
            p.price,
            i.quantity,
            p.price * i.quantity AS inventory_value
        FROM products p
        JOIN inventory i
            ON p.product_id = i.product_id
        ORDER BY inventory_value DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\nINVENTORY VALUE REPORT")
    print("-" * 70)

    for row in rows:
        print(
            f"Product: {row[0]} | "
            f"Price: ₹{row[1]} | "
            f"Quantity: {row[2]} | "
            f"Value: ₹{row[3]}"
        )

    cursor.close()
    connection.close()


def low_stock_report():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            p.product_name,
            i.quantity
        FROM products p
        JOIN inventory i
            ON p.product_id = i.product_id
        WHERE i.quantity < 10
        ORDER BY i.quantity
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\nLOW STOCK REPORT")
    print("-" * 50)

    if not rows:
        print("No low-stock products.")
    else:
        for row in rows:
            print(
                f"Product: {row[0]} | "
                f"Stock: {row[1]}"
            )

    cursor.close()
    connection.close()


def total_inventory_value():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            SUM(p.price * i.quantity)
        FROM products p
        JOIN inventory i
            ON p.product_id = i.product_id
    """

    cursor.execute(query)

    result = cursor.fetchone()[0]

    print("\nTOTAL INVENTORY VALUE")
    print("-" * 40)
    print(f"₹{result}")

    cursor.close()
    connection.close()