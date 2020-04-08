# Medium: three hotels
# First, create a list of hotel dictionaries. They should contain at least 3 identical dictionaries (like the one in the example above).
# Create a while True loop to show the following menu:
# 1. Print hotel room status
# 2. Check in customer
# 3. Check out customer
# 4. Quit
# - When printing, show all rooms for all hotels and the name of the occupant, if there is one.
# - When checking a customer in, make sure to choose a hotel as well as a room.
# - Do not let a customer check into an occupied room.
# - If the room is unoccupied, prompt for each piece of information (name, cell, etc.)
# - upon check out, print out whether or not the customer has paid
# Medium: add/remove hotels
# Add more options to your main menu.
# Provide options to open a new hotel or close an existing hotel.
# guest_info = {
#     "occupant name": "1",
#     "phone number" : "2",
#     "has prepaid" : "Y/N",
# }
# import pprint
# pp = pprint.PrettyPrinter()

hotel1= {
    "101" : "Jim1",
    "102" : "Jose1",
    "103" : "Jack1",
    "104" : "Jonnie1",
    "105" : "",
}
hotel2 = {
    "201" : "Jim2",
    "202" : "Jose2",
    "203" : "Jack2",
    "204" : "Jonnie2",
    "205" : "",
}
hotel3 = {
    "301" : "Jim3",
    "302" : "Jose3",
    "303" : "Jack3",
    "304" : "Jonnie3",
    "305" : "",
}
#allhotels
hotels = []
hotels.append(hotel1)
hotels.append(hotel2)
hotels.append(hotel3)
#------------------------customer check-in------------------------#
                ######-----Name------#######
nameLast=str(input("Customer last name."))
nameFirst=str(input("Customer first name."))
customer_name= (nameLast+nameFirst)
            ######-----Phone number------#######
phonenumber = int(input("Phone number"))
            ######-----PrePaid------#######
prepaid= (input("Has customer paid? If has not paid type 0" ))
if prepaid == True:
    print("ok to assign to room")
if prepaid == False:
    print("Do not assign to room until payment is recieved.")

guest_info{
    "name" : customer_name
    "phone number" : phonenumber
    "prepaid": prepaid
}
#------------------------------------------------------------------#
# assign to room

#menu
main_menu = '''
1. Print hotel room status
2. Check in customer
3. Check out customer
4. Quit
'''
while True:
    menu_sel = int(input(main_menu))
    if menu_sel == 1:
       print(hotels)
        #hotel selec
    if menu_sel == 2:
        selected_hotel =int (input ("Hotel 1,2,or 3 "))
        if selected_hotel ==1:

            print(hotel1)
        if selected_hotel ==2:
            print(hotel2)
        if selected_hotel ==3:
            print(hotel3)
        if selected_hotel == "all":
            print(hotels)
   

    if menu_sel == 4:   
        print("Thank you, Come again")
        break
   
