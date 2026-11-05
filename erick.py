print('======= SIMPLE FOOD ORDERING SYSTEM ========')
meal_code = ("M01", "M02", "M03")
meal = ['Chicken','Burger meal','Pasta']
print("\n\n Available meals: ")
print("M01 - chicken Meal - 120₱")
print("M02 - Burger Meal - 150₱")
print("M03 - Pasta Meal - 180₱")
price = ["120","150","180"]

'''index = ('0','1','2')'''

codes = (input("Enter meal code: "))
quantity_meal = int(input("Enter quantity: "))

if codes == "M01":
    print("you selected", meal[0])
    print("price: ₱", price[0])
    price = 120
elif codes == "M02":
    print("You selected: ", meal[1])
    print("price: ₱", price[1])
    price = 15-
elif codes == "M03":
    print("You selected: ", meal[2])
    print("price: ₱", price[2])
else:
    print('invalid')

total = price * quantity_meal
print("total: ", total)




