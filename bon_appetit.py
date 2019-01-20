def bon_appetit(bill, k, b):
    without_anna_item = (sum(bill) - bill[k]) / 2
    print(without_anna_item)
    if b != without_anna_item:
        print(b - without_anna_item)
    else:
        print('Bon Appetit')


bill = [3, 10, 2, 9]
k1 = 1
b1 = 12
b2 = 7

bon_appetit(bill, k1, b2)