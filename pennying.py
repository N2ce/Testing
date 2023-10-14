import samplebot


class stockpennying:
    def __init__(self,symbol) -> None:
        self.bid_price
        self.ask_price
        self.bidvol
        self.askvol
        self.Borderid = []
        self.Sorderid = []
        self.symbol = symbol
    def pennying(self,message):
        if message["type"] == "book" and message["Symbol"] == self.symbol:
            def bestvalue(side):
                if message[side]:
                    return message[side][0][0]

            self.bid_price = bestvalue("buy")
            self.ask_price = bestvalue("sell")
            self.bidvol = sum(sublist[1] for sublist in message["buy"])
            self.askvol = sum(sublist[1] for sublist in message["sell"])
            
    def ordering(self,exchange):
        global B,S
        exchange.send_cancel_message(self.Borderid[0])
        exchange.send_cancel_message(self.Sorderid[0])
        del self.Borderid[0]
        del self.Sorderid[0]
        exchange.send_add_message(order_id=S, symbol=self.symbol, dir="SELL", price=self.bid_price+1, size=self.askvol)
        exchange.send_add_message(order_id=B, symbol=self.symbol, dir="BUY", price=self.ask_price-1, size=self.bidvol)
        self.Sorderid.append(S)
        self.Borderid.append(B)
        S += 1
        B += 1
        