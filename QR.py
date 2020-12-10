import qrcode
import Item
import cv2
def create_next_qr():
    with open("qrdata.txt","r") as f:
        lines = f.readlines()
    if lines == []:
        no = int(1)
    else:
        no, desc = lines[len(lines)-1].split(",")
        no = int(no) + 1
    x=str(no)
    img = qrcode.make(x)
    img.save(f"{x}.png")
    print(f"QR ID: {x}")
    dsc=str(input("Description: "))
    Item.create_item()

def create_qr_from_id(x):
    img = qrcode.make(x)
    img.save(f"{x}.png")

def scan_qr():
    # initalize the cam
    cap = cv2.VideoCapture(0)

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()

        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)

        # check if there is a QRCode in the image
        if bbox is not None:
           

            if data:
                break

        # display the result
        cv2.imshow("img", img)
        
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    with open("qrdata.txt","r") as f:
        lines = f.readlines()
    for line in lines:
        l1,l2 = line.split(",")
        if l1 == data:
            return l1,l2
    return data
