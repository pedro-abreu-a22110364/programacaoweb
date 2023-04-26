def positivo(n):
    if n > 0:
        return True
    return False

def par(n):
    if n % 2 == 0:
        return True
    return False

def primo(n):
    if n > 1:
 
        for i in range(2, n):
   
            if (n % i) == 0:
                return False
        else:
            return True
 
    else:
        return False