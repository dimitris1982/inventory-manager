print("ΔΙΑΧΕΙΡΙΣΗ ΑΠΟΘΕΜΑΤΟΣ — ΚΑΦΕΣ")


stock = 20
choice = 0
total_received = 0
total_sold = 0

while choice != 4:
    print("1. Παραλαβή προϊόντος")
    print("2. Πώληση προϊόντος")
    print("3. Εμφάνιση αποθέματος")
    print("4. Έξοδος")

    choice = int(input("Δώσε επιλογή: "))

    if choice == 1:
        print("Επέλεξες παραλαβή")
        quantity = int(input("Δώσε ποσότητα παραλαβής: "))
        if quantity > 0:
            stock = stock + quantity
            total_received = total_received + quantity
            print(f'Το απόθεμα είναι: {stock}')
        else:
            print("Η ποσότητα πρέπει να είναι θετική")
    elif choice == 2:
        print("Επέλεξες πώληση")
        sale = int(input("Δώσε ποσότητα πώλησης: "))
        if sale <= 0:
            print("Η ποσότητα πρέπει να είναι θετική")
        elif sale > stock:
            print("Δεν υπάρχει αρκετό απόθεμα")
        else:
            stock = stock - sale
            total_sold = total_sold + sale
            print(f'Το απόθεμα είναι: {stock}')
    elif choice == 3:
        print(f'Το stock είναι: {stock}')
        print(f'Συνολικά τεμάχια παραλαβών: {total_received}')
        print(f'Συνολικά τεμάχια πωλήσεων: {total_sold}')
        if stock == 0:
            print("Το προϊόν εξαντλήθηκε!")
        elif stock <=5:
            print("Χαμηλό απόθεμα — χρειάζεται παραγγελία.")
        else:
            print("Το απόθεμα είναι επαρκές.")
    elif choice == 4:
        print("Έξοδος")
    else:
        print("Μη έγκυρη επιλογή")


