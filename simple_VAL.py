import samplebot
VALE = []
VALBZ = []

def data(value, operation, type):
    if operation == "buy":
        if type == "VALE":
            VALE.append(value)
        else:
            VALBZ.append(value)
    else:
        if type == "VALE":
            VALE.append(value)
        else:
            VALBZ.append(value)

def simple_val(bestbuy, bestsell):
    
