# Programmers:  Liv Oakes, Hazel Osborne
# Course:  CS151
# Due Date: Oct. 9th 2024
# Lab Assignment: Lab 04
# Problem Statement: Determine price based on data used and package type
# Data In: Data used(GB) and Package type
# Data Out:  Data used(GB) and Price

#Prompt user to enter package type
package_type  = str(input("Enter your package type: "))
package_type = package_type.lower()

#Make sure Package type is valid
while (package_type != "purple") and (package_type != "blue") and (package_type != "green"):
    package_type = str(input("Enter a valid package type: "))
    package_type = package_type.lower()

#Prompt user to Enter Data used
gb = float(input("Enter Data used in GB"))

#Check if Package type is green
if package_type == "green":
    price = 49.99

    #Calculate price if above monthly data
    if gb > 2:
        gb_new = gb - 2
        price = price + (gb_new * 15)
    #Check if user used coupon
    coupon =  str(input("Did you use a coupon? Enter Yes or No"))
    coupon = coupon.lower()

    #Case correct coupon input
    while (coupon != "yes") and (coupon != "no"):
        coupon = str(input("Invalid Statement. Enter Yes or No"))
        coupon = coupon.lower()


        if coupon == "yes" and price > 75:
            price = price - 20

#Check if package type is blue
elif package_type == "blue":
    price = 70
    #Calculate blue price
    if gb > 4:
        gb_new = gb - 4
        price = price + (gb_new * 10)

#Price for package type purple
else:
    price = 99.99

#Output price to user
print("Your total price is:", f"{price:.2f}")
print("You used", gb, "gigabytes of data.")

