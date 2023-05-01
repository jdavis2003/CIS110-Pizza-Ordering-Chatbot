print("Hello, my name is Gizmo your virtual assistant.  I will help you order your pizza!")
print("I am going to ask you a few questions.  After typing an answer, press Enter.")
userName = input("\nEnter your name:  ")
if userName.lower() == "jennifer":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")

size = input("\nWhat size do you want? Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat type of crust do you want:  ")
quantity = input("\nHow many of these do you want to order? Enter a nurmeric value:  ")
quantity = int(quantity)
method = input ("\nIs this carry out or delivery:  ")

if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
    
salesTax = 1.0825

if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99

total = (pizzaCost * quantity) * salesTax + deliveryFee

print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")

if total >= 50:
    print ("\nCongrats! You've been awarded a $10 off coupon for your next order.")
else:
    print("\nOrders over $50 will receive a free $10 off coupon!")

print("-" * 10)