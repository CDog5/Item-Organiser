import Item,Data,QR
def main():
    running = True
    while running:
        print("1 - Scan QR")
        print("2 - Create xlsx data")
        print("3 - Get item by id")
        uin = int(input("Choose an option:"))
        if uin == 1:
            running = False
            result = QR.scan_qr()
            print(f"Scanned: {result}")
            running = True
        elif uin == 2:
            running = False
            Data.create_xlsx_data()
            print("Created data.")
            running = True
        elif uin == 3:
            running = False
            idno = int(input("Id no:"))
            print(Item.get_item_by_id(idno))
            running = True
        else:
            running = False
            print("Input not recognised, please try again.")
            running = True
if __name__ == "__main__":
    main()
