dict = {1:1}

def shi():
    x = int(input())
    x = get_pet(ID=x)
    
    print(x)

def get_pet(ID):   
    while ID not in dict.keys():
        if ID not in dict.keys():
            print("такого числа нет, введите заново")
            ID = int(input())
    return ID
    
shi()


