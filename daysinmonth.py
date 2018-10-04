def day_amount(month, year):
    from calendar import monthrange
    x = monthrange(year, month)
    y = list(x)
    return y[1]
    
