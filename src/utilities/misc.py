def N_str_sum(N_str,n):
        if len(N_str) == 1:
            if n >= 0:
                return N_str+"+"+str(n)
            else:
                return N_str+str(n)
        else:
            s = int(N_str[1:3])+n
            if s > 0:
                return N_str[0:2]+str(s)
            elif s < 0:
                return N_str[0]+str(s)
            elif s == 0:
                return N_str[0]
            
def prod_except(indices, comp):
        c = 1
        for i in range(len(comp)):
            if i not in indices:
                c *= int(comp[i][1:3])
        return c