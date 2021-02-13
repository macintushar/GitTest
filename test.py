import matplotlib.pyplot as plot
from dataframe import orderDF
import pandas as pd

orderDF()

orders = pd.read_csv("/home/tushar/Code/12th IP Project/Restaurant Menu/order.csv")
print(orders)

val = orders.loc[1:,['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']]
print(val)

value = pd.DataFrame(val)
value = value.to_csv('/home/tushar/Code/12th IP Project/Restaurant Menu/graph.csv')
value = pd.read_csv("/home/tushar/Code/12th IP Project/Restaurant Menu/graph.csv")
x = value.sum(axis=0, skipna=True)
x = list(x)
x.pop(0)
print(x)

dishes = ['CRISPY CHILLI POTATO','PANEER TIKKA','CHICKEN WINGS','FRENCH FRIES','PANEER TIKKA PIZZA','BBQ CHICKEN PIZZA','MARGHERITA PIZZA','CHICKEN KEEMA BURGER','VEG PLATTER' ,'NON VEG PLATTER' ,'BLUEBERRY CHEESECAKE' ,'SOFTY' ,'OREO MOUSSE','SPRITE' ,'COKE']

dish = dict(zip(dishes,x))

print(dish)
print()


'''
grph = plot.barh(dishes,x)

plot.xlabel('Frequency of Dishes ordered')
plot.ylabel('Dishes')

plot.grid(True)

plot.tight_layout()
plot.savefig("/home/tushar/Code/12th IP Project/Restaurant Menu/static/images/graph2.jpeg")
plot.show()
'''