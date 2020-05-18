def nba_extrap(ppg, mpg):
    
    extrap = (ppg / mpg) * 48
    return round(extrap, 1) if mpg > 0 else 0;