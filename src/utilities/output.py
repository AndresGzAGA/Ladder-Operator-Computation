def str_out(coeff, m):
    polynomial = ""
    
    for n in range(m,len(coeff)):
        if n == 0:
            polynomial += str(coeff[0])
        elif n == 1:
            if coeff[n] > 0 and polynomial != "":
                polynomial += "+"+str(coeff[n])+"N"
            else:
                polynomial += str(coeff[n])+"N"
        elif coeff[n] > 0 and polynomial != "":
                polynomial += "+"+str(coeff[n])+"N**"+str(n)
        else:
            polynomial += str(coeff[n])+"N**"+str(n)
        
    return polynomial