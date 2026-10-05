from products import (
    add_product,
    view_products,
    update_product,
    delete_product
)

from inventory import (
    add_stock,
    remove_stock,
    view_inventory
)

from reports import (
    inventory_report,
    low_stock_report,
    total_inventory_value
)

from sales import create_sale


def show_menu():
    print("\n")
    print("=" * 50)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1.  Add Product")
    print("2.  View Products")
    print("3.  Update Product")
    print("4.  Delete Product")

    print("5.  Add Stock")
    print("6.  Remove Stock")
    print("7.  View Inventory")

    print("8.  Inventory Value Report")
    print("9.  Low Stock Report")
    print("10. Total Inventory Value")

    print("11. Create Sale")

    print("12. Exit")

    print("=" * 50)


def main():

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                add_product()

            elif choice == "2":
                view_products()

            elif choice == "3":
                update_product()

            elif choice == "4":
                delete_product()

            elif choice == "5":
                add_stock()

            elif choice == "6":
                remove_stock()

            elif choice == "7":
                view_inventory()

            elif choice == "8":
                inventory_report()

            elif choice == "9":
                low_stock_report()

            elif choice == "10":
                total_inventory_value()

            elif choice == "11":
                create_sale()

            elif choice == "12":
                print("\nThank you for using Inventory Management System!")
                break

            else:
                print("\nInvalid choice. Please enter a number from 1 to 12.")

        except ValueError:
            print("\nInvalid input. Please enter the correct value.")

        except Exception as error:
            print(f"\nAn error occurred: {error}")


if __name__ == "__main__":
    main()