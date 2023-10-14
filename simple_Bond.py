import samplebot
def buy_bond_strate(exchange, size,B):
    

    exchange.send_add_message(order_id=B, symbol="BOND", dir="BUY", price=999, size=size)




        
def sell_bond_strate(exchange, size,S):


    exchange.send_add_message(order_id=S, symbol="BOND", dir="SELL", price=1001, size=size)



