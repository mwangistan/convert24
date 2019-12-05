def convert24(date): 
    '''Convert am/pm date to 24hr format
    '''
    # Checking if last two elements of time 
    # is AM and first two elements are 12 

    if date[-2:] == "AM" and date[:2] == "12": 
        return "00" + date[2:-2] 
        
    # remove the AM     
    elif date[-2:] == "AM": 
        return date[:-2] 
    
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif date[-2:] == "PM" and date[:2] == "12": 
        return date[:-2] 
        
    else:             
        # add 12 to hours and remove PM 
        return str(int(date[:2]) + 12) + date[2:5]