sales = []
choice = ""

while choice != "4":
    print("\n-SCHOOL CANTEEN SALES LOG-")
    print("(1) - Add Sale")
    print("(2) - View Sales Summary")
    print("(3) - Edit Sale")
    print("(4) - Exit")
    print("-" * 30)
    choice = input("Enter your choice: ")

    if choice == "1":
        another_Entry = "y"
        while another_Entry == "y":
            product = input("Enter product name: ").strip().capitalize()
            qty = int(input("Enter quantity sold: "))
            price = float(input("Enter price per item: "))
            total = qty * price
            record = {"product": product, 
                      "qty": qty, 
                      "price": price, 
                      "total": total}
            sales.append(record)
            print(f"\n{product} recorded successfully!\n")
            another_Entry = input("Add another sale? (y/n): ").lower()
        else:
            print("-" * 30)
            print("-SALES SUMMARY")
            for i, sale in enumerate(sales):
                    print(f"{i+1} - {sale['product']} ({sale['qty']} pcs)")

    elif choice == "2":
        print("\n-SALES SUMMARY-")
        if len(sales) == 0:
            print("No sales recorded yet.")
        else:
            total_sales = 0
            print(f"{'No.':<4}{'Product':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
            print("-" * 50)
            for i, sale in enumerate(sales):
                print(f"{i+1:<4}{sale['product']:<15}{sale['qty']:<5}{sale['price']:<10.2f}{sale['total']:<10.2f}")

                total_sales += sale['total']
            print("-" * 50)
            print(f"Total Daily Sales: ₱{total_sales:.2f}")

    elif choice == "3":
        print("\n-EDIT SALE-")
        if len(sales) == 0:
            print("No sales to edit.")
        else:
            for i, sale in enumerate(sales): 
                print(f"{i+1} - {sale['product']} ({sale['qty']} pcs)")
            edit_no = int(input("Enter the number of the sale to edit: ")) - 1
            if 0 <= edit_no < len(sales):
                product = input("Enter new product name: ").strip().capitalize()
                qty = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                total = qty * price
                sales[edit_no] = {"product": product, "qty": qty, "price": price, "total": total}
                print("\nSale updated successfully!")
                
                for i, sale in enumerate(sales):
                    print(f"{i+1} - {sale['product']} ({sale['qty']} pcs)")
                
            else:
                print("Invalid number entered.")

    elif choice == "4":
        print("Thank you for using the system!")
    else:
        print("Invalid choice, please try again.")