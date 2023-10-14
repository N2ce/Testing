import samplebot
import time
S = 5000000
B = 1000000
lst = []
def estimation(message,temp = []):
    if message["type"] == "book":
        buy_total = sum(sublist[1] for sublist in message["buy"])
        buy_sum_value = sum(sublist[0] for sublist in message["buy"])
        sell_total = sum(sublist[1] for sublist in message["sell"])
        sell_sum_value = sum(sublist[0] for sublist in message["sell"])
        if message["symbol"] == "GS":
            temp[0] = ((buy_sum_value*buy_total)+(sell_total*sell_sum_value))/(buy_total+sell_total)
        elif message["symbol"] == "MS":
            temp[1] = ((buy_sum_value*buy_total)+(sell_total*sell_sum_value))/(buy_total+sell_total)
        elif message["symbol"] == "WFC":
            temp[2] = ((buy_sum_value*buy_total)+(sell_total*sell_sum_value))/(buy_total+sell_total)
        elif message["symbol"] == "XLF":
            temp[3] = ((buy_sum_value*buy_total)+(sell_total*sell_sum_value))//(buy_total+sell_total)

def weighting(temp,exchange,lst):
    global S,B
    weight = (2*temp[0] + 3*temp[1] + 2*temp[2] + 3*1000)//10
    if weight > temp[3]:
        exchange.send_add_message(order_id=B, symbol="XLF", dir="BUY", price=temp[3], size=50)
        B += 1
        lst.append(B)
        
    elif temp[3] > weight:
        exchange.send_add_message(order_id=S, symbol="XLF", dir="SELL", price=weight, size=50)
        S += 1
        lst.append(S)


def cancelorder(lst,exchange):
    if len(lst) != 0:
        exchange.send_cancel_message(lst[0])
        del lst[0]


def stratesETF(message,exchange,lst,temp=[]):
    estimation(message,temp)
    estimation(message,temp)
    estimation(message,temp)
    estimation(message,temp)
    weighting(temp,exchange,lst)
    time.sleep(3)
    cancelorder(lst,exchange)