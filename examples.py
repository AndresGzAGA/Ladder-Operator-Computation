from main import ladder_to_number

print(ladder_to_number(["a","b"])) # Outputs a string with value "1+1N".

print(ladder_to_number(["b","a"])) # Outputs a string with value "N".

print(ladder_to_number(["a","a","b","b"])) # Outputs a string with value "2+3N+1N**2". This is the example given in the README.txt file.

print(ladder_to_number(["a","b","a","b","b","a"])) # Outputs a string with value "1N+2N**2+1N**3".

print(ladder_to_number(["a","b","a","b","b","a","a","a","b","b"])) # Outputs a string with value "2N+7N**2+9N**3+5N**4+1N**5".

print(ladder_to_number(["a"]*5+["b"]*10+["a"]*5)) # Outputs a string with value "2880N+576N**2-4100N**3-820N**4+1365N**5+273N**6-150N**7-30N**8+5N**9+1N**10".