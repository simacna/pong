def assortments(listy):
    run = listy
    first_half = run[0:len(listy)/2]
    second = listy[len(listy)/2:]

    run = listy
    for idx in range(len(first_half)):
        if first_half[idx] > first_half[idx+1]:
            first_half[idx] = first_half[idx+1]
            
    return run
    
