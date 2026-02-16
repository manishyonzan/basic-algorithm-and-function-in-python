def findCelebrity(n):
    candidate = 0
    
    for i in range(1,n):
        # if(not knows(candidate,i)):
        #     candidate = i
        pass
    for j in range(0,n):
        if(i==candidate):
            continue
        # if(not knows(candidate,i) or knows(candidate,j)):
            # if j doesnot know candidate
            # or candidate knows j, return -1
            return -1
        
    return candidate
        