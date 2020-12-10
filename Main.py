import Item,Data,QR
def main():
    running = True
    while running:
        print("1 - Scan QR")
        print("2 - Create xlsx data")
        print("3 - Get item by id")
        print("4 - Create QR from id")
        print("5 - Create next QR")
        print("6 - Get item id")
        uin = int(input("Choose an option:"))
        if uin == 1:
            running = False
            print("Starting")
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
        elif uin == 4:
            running = False
            idno = int(input("Id no:"))
            QR.create_qr_from_id(idno)
            running = True
        elif uin == 5:
            running = False
            QR.create_next_qr()
            running = True
        elif uin == 6:
            running = False
            item = str(input("Item:"))
            Item.get_item_id(item)
            running = True
        elif uin == 7:
            running = False
            sz = int(input("How big should the qr codes be? (1 is best):"))
            fr = int(input("From what value?:"))
            to= int(input("To what value?:"))
            Data.create_qr_docx(sz,fr,to)
            running = True
        else:
            running = False
            print("Input not recognised, please try again.")
            running = True
if __name__ == "__main__":
    main()
