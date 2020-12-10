
def get_item_by_id(idcode):
    with open("qrdata.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            l1,l2 = line.split(",")
            if l1 == str(idcode):
                return l2
#checks the item id by the description
def get_item_id(desc):
    with open("qrdata.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            l1,l2 = line.split(",")
            if str(desc.lower()) in str(l2.lower()):
                return int(l1)

def create_item(idcode,desc):
    with open("qrdata.txt","a") as f:
        f.write(idcode+","+desc+"\n")
