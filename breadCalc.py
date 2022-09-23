import string
from ingredients import *

def pizza_dough_cost(flour_name:string, flour_ammount:float, yeast_name:string, yeast_ammount:float,salt_name:string, salt_ammount:float):
    cost = (flour_ammount*(flour_name["price"]/flour_name["weight"]))+(yeast_ammount*(yeast_name["price"]/yeast_name["weight"]))
    cost += salt_ammount*(salt_name["price"]/salt_name["weight"])
    print(f"Dough cost {cost}")
    return cost

def toppings_cost(mozzarella_name:string, mozarella_ammount:float):
    cost = mozarella_ammount * (mozzarella_name["price"]/mozzarella_name["weight"])
    print(f"Toppings cost: {cost}")
    return cost

def tomatoe_sauce_cost(tomato_name:string, tomatoe_ammount:float, olive_oil_name:string, olive_oil_ammount:float, salt_name:string, salt_ammount:float):
    cost = tomatoe_ammount * (tomato_name["price"]/tomato_name["weight"])
    cost += (olive_oil_ammount * (olive_oil_name["price"]/olive_oil_name["weight"])) + (salt_ammount * (salt_name["price"]/salt_name["weight"]))
    print(f"Tomatoe sauce cost: {cost}")
    return cost
one_margaretha_ram = pizza_dough_cost(ramlösa_tipo,156,yeast,0.3,salt,4.6) + toppings_cost(mozzarella,100) + tomatoe_sauce_cost(tomatoe_sauce,100,olive_oil,3.75,salt,3.75)
one_margaretha_caputo = pizza_dough_cost(caputo_tipo,156,yeast,0.3,salt,4.6) + toppings_cost(mozzarella,100) + tomatoe_sauce_cost(tomatoe_sauce,100,olive_oil,3.75,salt,3.75)
print(f"Pizza made with caputo flour cost: {one_margaretha_caputo} and with ramlösa: {one_margaretha_ram}")


def make_bread(flour1_name:string, flour1_ammount:float, flour2_name:string, flour2_ammount:float, honey_name:string, honey_ammount:float, yeast_name:string, yeast_ammount:float, salt_name:string, salt_ammount:float, water_ammount:float = 0):
    
    print("****************************************************************************************************")
    flour1_cost = flour1_ammount * (flour1_name["price"]/flour1_name["weight"])
    flour2_cost = flour2_ammount * (flour2_name["price"]/flour2_name["weight"])
    honey_cost = honey_ammount * (honey_name["price"]/honey_name["weight"])
    yeast_cost = yeast_ammount * (yeast_name["price"]/yeast_name["weight"])
    salt_cost = salt_ammount * (salt_name["price"]/salt_name["weight"])
    total_cost = flour1_cost + flour2_cost + honey_cost + yeast_cost + salt_cost

    print(f"Individual cost {flour1_name}: {flour1_cost}, ölands: {flour2_cost}, honey: {honey_cost} yeast: {yeast_cost}, salt: {salt_cost}")
    print(f"Total cost: {total_cost}:-\n")
    print(f"Bread weight: {flour1_ammount+flour2_ammount+honey_ammount+yeast_ammount+salt_ammount+water_ammount}g")
    print(f"Hydration: {round(water_ammount/(flour1_ammount+flour2_ammount)*100)}%")
    print(f"Salt%: {round(salt_ammount/(flour1_ammount+flour2_ammount)*100)}%")
    print("****************************************************************************************************")
    return total_cost
make_bread(ölands_vete,200,ramlösa_tipo,400,honey,15,yeast,10,salt,15,500)