from datetime import datetime

# Hint:  use Google to find python function

def difference_in_days(date1, date2):

    months = 'jan feb mar apr may jun jul aug sep oct nov dec'.split()
    month_to_number = {month:x for month, x in zip(months, range(1,13))}

    # Check Format    
    if '-' in date1:
        if date1[3:4].isalpha():
            d1 = datetime(int(date1[-4:]), month_to_number[date1[3:6].lower()], int(date1[:2]))
            d2 = datetime(int(date2[-4:]), month_to_number[date2[3:6].lower()], int(date2[:2]))
        else:
            d1 = datetime(int(date1[-4:]), int(date1[:2]), int(date1[3:5]))
            d2 = datetime(int(date2[-4:]), int(date2[:2]), int(date2[3:5]))
    else:
        d1 = datetime(int(date1[-4:]), int(date1[:2]), int(date1[2:4]))
        d2 = datetime(int(date2[-4:]), int(date2[:2]), int(date2[2:4]))

    return (d2 - d1).days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
print("There are {0} days between {1} and {2}".format(difference_in_days(date_start, date_stop), date_start, date_stop))

# >> There are 937 days between 01-02-2013 and 07-28-2015

####b)  
date_start = '12312013'  
date_stop = '05282015'
print("There are {0} days between {1} and {2}".format(difference_in_days(date_start, date_stop), date_start, date_stop))  

# >> There are 513 days between 12312013 and 05282015

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 
print("There are {0} days between {1} and {2}".format(difference_in_days(date_start, date_stop), date_start, date_stop)) 

# >> There are 7850 days between 15-Jan-1994 and 14-Jul-2015