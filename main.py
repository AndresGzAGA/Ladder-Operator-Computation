from src.utilities.misc import N_str_sum, prod_except
from src.utilities.input import input_validation
from src.utilities.output import str_out

def ladder_to_number(O):

    input_validation(O)
    
    while sum(o == "a" for o in O) + sum(o == "b" for o in O) > 0:    
    
        #Substitute identifiable number operators
        i = 0
        while i+1 < len(O):
            if O[i] == "b" and O[i+1] == "a":
                O[i] = "N"
                del O[i+1]
            if O[i] == "a" and O[i+1] == "b":
                O[i] = "N+1"
                del O[i+1]
            i += 1
        
        #Move all initial number operators to the right
        i = 0
        n = 0
        while n + 1 < len(O):
            if O[i] != "a" and O[i] != "b":
                for j in range(i+1,len(O)):
                    if O[j] == "a":
                        #Commutator [N,a] = -a, Na = a(N-1)
                        O[j] = N_str_sum(O[j-1],-1)
                        O[j-1] = "a"
                    elif O[j] == "b":
                        #Commutator [N,b] = b, Nb = b(N+1)
                        O[j] = N_str_sum(O[j-1],+1)
                        O[j-1] = "b"
                    else:
                        #Linear operators in N which commute
                        O[j-1], O[j] = O[j], O[j-1]
                        
                i -= 1 #In order to not miss the commuted element
            i += 1
            n += 1 #Counter for covering all elements
        
    coeff = [0]*(len(O)+1)
    coeff[-1] = 1
    
    m = sum([o == "N" for o in O]) #Single powers of N
    comp = [o for o in O if o != "N"] #Composite terms of N+a
    N = len(comp)-1
    
    if m == len(O) and m != 1:
        return "N**"+str(m)
    elif m == len(O) and m == 1:
        return "N"
    
    coeff[m] = prod_except([], comp)
    
    for n in range(m+1,len(coeff)-1): #Coefficient a_n of N**n
        
        indices = [i for i in range(n-m)]
        coeff[n] = prod_except(indices, comp)
        
        while indices[0] != N-(n-m)+1:
            i = len(indices)-1 #last element
    
            while indices[i] < N+i-(len(indices)-1):
                indices[i] += 1
                coeff[n] += prod_except(indices, comp)
                
            if len(indices) == 1:
                break
    
            for j in range(1,len(indices)+1):
                if indices[i-j]+1 != indices[i-j+1]:
                    indices[i-j] +=1
                    for k in range(i-j+1,len(indices)):
                        indices[k] = indices[k-1]+1
                    coeff[n] += prod_except(indices, comp)
                    break
    
    return str_out(coeff, m)