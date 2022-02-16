def mathCompoundInterest(principle,rate,time):
    
    totalAmount = principle*(1+(rate/100))**time

    print("Compound Interest: "+ str(round(totalAmount - principle,2)))


def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you
# I really should loop this...
    
    client_principal = float(input("Principle (amount): "))
    client_time =      float(input("Time:               "))
    client_rate =      float(input("Rate:               "))
    mathCompoundInterest(client_principal,client_rate,client_time)
    print("---")
    client_principal = float(input("Principle (amount): "))
    client_time =      float(input("Time:               "))
    client_rate =      float(input("Rate:               "))
    mathCompoundInterest(client_principal,client_rate,client_time)
    print("---")
    client_principal = float(input("Principle (amount): "))
    client_time =      float(input("Time:               "))
    client_rate =      float(input("Rate:               "))
    mathCompoundInterest(client_principal,client_rate,client_time)



 #print("Compound Interest: "+str(intrest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
if __name__ == "__main__":
    calculateCompoundInterest()
