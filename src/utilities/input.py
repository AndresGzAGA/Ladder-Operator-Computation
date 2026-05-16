def input_validation(O):
    if any(o not in ["a","b"] for o in O):
        raise ValueError("O must be a list of ladder operators represented by strings a and b")
        
    if len(O) % 2 != 0:
        raise ValueError("O must be an even list with an equal number of creation and annihilation operators")
        
    if sum(o == "a" for o in O) != sum(o == "b" for o in O):
        raise ValueError("O must be a list with an equal number of creation and annihilation operators")
    