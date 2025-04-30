#You can perform if...else statements inside the placeholders:

#Return "Expensive" if the price is over 50, otherwise return "Cheap" ?

price = 49

txt = f"it is very {'Expensive' if price>50 else 'cheap'}"
print(txt)