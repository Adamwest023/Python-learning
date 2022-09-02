year = int(input("What year would you like to check: "))

def is_leap_year(year):     
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Its a leap year")
            else:
                print("Not a leap year")
        else:
            print('Leap year')
    else:
        print("Not a leap year")
    
        
is_leap_year(year)