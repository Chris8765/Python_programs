# Tribonacci Sequence

#As the name may already reveal, it works basically like a Fibonacci, 
#but summing the last 3 (instead of 2) 
#numbers of the sequence to generate the next.



n = 10
signature = [1,1,1]

def tribonacci(signature, n):
    step = n - 3 
    
    counter = 0
    if n == 0:
        signature = []
    elif n == 1:
        signature = [signature[0]]
    elif n == 2:
        signature = [signature[0], signature[1]]
 
    else:
        while counter < step:
            entry = signature[(0+counter)] + signature[(1+counter)] + signature [(2+counter)]
            counter +=1
            signature.append(entry)
    
    result = signature
    return(result)

result = tribonacci(signature, n)

print(result)