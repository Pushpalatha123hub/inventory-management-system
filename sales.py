from database import get_connection


def create_sale():
    customer_name = input("Enter customer name: ")
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))

    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Check product and stock
        cursor.execute(
            """
            SELECT price, quantity
            FROM products
            JOIN inventory
                ON products.product_id = inventory.product_id
            WHERE products.product_id = %s
            FOR UPDATE
            """,
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:
            print("Product not found.")
            connection.rollback()
            return

        price, stock = product

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            connection.rollback()
            return

        if stock < quantity:
            print("Not enough stock.")
            connection.rollback()
            return

        total_amount = price * quantity

        # Create sale
        cursor.execute(
            """
            INSERT INTO sales
            (customer_name, total_amount)
            VALUES (%s, %s)
            RETURNING sale_id
            """,
            (customer_name, total_amount)
        )

        sale_id = cursor.fetchone()[0]

        # Create sale item
        cursor.execute(
            """
            INSERT INTO sale_items
            (sale_id, product_id, quantity, unit_price)
            VALUES (%s, %s, %s, %s)
            """,
            (sale_id, product_id, quantity, price)
        )

        # Reduce inventory
        cursor.execute(
            """
            UPDATE inventory
            SET quantity = quantity - %s
            WHERE product_id = %s
            """,
            (quantity, product_id)
        )

        # Commit everything
        connection.commit()

        print("Sale completed successfully!")
        print(f"Sale ID: {sale_id}")
        print(f"Total amount: ₹{total_amount}")

    except Exception as error:
        connection.rollback()
        print("Sale failed.")
        print(f"Error: {error}")

    finally:
        cursor.close()
        connection.close()