from datetime import datetime

name=input("Enter your name:")
# list of items
lists='''
rice    Rs 30/kg
sugar   Rs 20/kg
salt    Rs 10/kg
boost   Rs 80/kg
yippee  Rs 50/kg
oil     Rs 90/kg
milk    Rs 30/lt
besan   Rs 50/kg
'''
# Declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':30,'sugar':20,'salt':10,'boost':80,'yippee':50,'oil':90,'milk':30,'besan':50}
option=int(input("for list of items press1 :"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*4)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(30*"=","Python Supermarket",30*"=")
            print(32*" ","Anakapalli")
            print("Name:",name,28*" ","Date:",datetime.now())
            print(75*"-")
            print(" sno",6*" ",'items', 6*" ",'quantity',6*" ",'price')
            for i in range(len(pricelist)):
                print(i,6*' ',3*' ',ilist[i],6*' ',qlist[i],6*" ",plist[i])
            print(80*" ")
            print(60*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount:",50*" ",'Rs',gst)
            print(80*"-")
            print(60*" ",'finalamount:','Rs',finalamount)
            print(80*"-")
            print(60*" ","Thanks for visting")
            print(80*"-")

