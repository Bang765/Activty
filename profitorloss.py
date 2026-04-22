AP = int(input("Enter the price you bought the item"))
SP = int(input("Enter the price you sold the item"))
if AP > SP :
    print("you have occurred a loss of", AP - SP)
elif AP < SP:
    print("you have made a profit of", SP - AP)
    