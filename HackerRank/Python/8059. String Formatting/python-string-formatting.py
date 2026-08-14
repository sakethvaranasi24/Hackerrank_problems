def print_formatted(number):
    # your code goes here
    w=len(bin(number)[2:])
    
    for i in range(1,number+1):
        dec = str(i).rjust(w)
        octal = oct(i)[2:].rjust(w)
        hexa = hex(i)[2:].upper().rjust(w)
        binary = bin(i)[2:].rjust(w)
        
        print(f"{dec} {octal} {hexa} {binary}")
    

