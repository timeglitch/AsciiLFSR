from operator import mod
import binascii

from numpy import integer
pm = "PM"
cipherText = "111010101100100111100101101011000010001001011010001100111000100110101001010110101000111011000011100100110110000011011000010011101110011000000111011111110110000000000011"
lfsrlength = 5

#simulates a binary lfsr with lists state and cof of equal length, returns the output 
def lfsr(state, cof) -> list[int]:
    out = 0
    for(i, j) in zip(state, cof):
        out = out + i * j
    out = out % 2
    return state[1:] + [out]

def revlfsr(state, cof) -> list[int]:
    pass

def intToList (input: int) -> list[int]:
    remaining = input
    output = []
    for i in [2 ** x for x in range(lfsrlength-1, -1, -1)]:
        if remaining >= i:
            output.append(1)
            remaining = remaining - i
        else:
            output.append(0)
    return output


state = [1,1,1,0,1]
co = [1,0,0,1,0]

output = lfsr(state,co)
stringlist = {}

for statesvalues in range(32):
    
    orstate = intToList(statesvalues)
    for coefvalues in range(32):
        co = intToList(coefvalues)
        state = orstate
        outstr = ""
        for i in range(len(cipherText)):
            outstr = outstr + str(state[0])
            state = lfsr(state,co)
        #print(outstr)
        stringlist[outstr] = (orstate, co)

for lsfrbits in stringlist:
    new = [(ord(a) ^ ord(b)) for a,b in zip(cipherText, lsfrbits)]
    out = ""
    for i in new:
        out = out + str(i)
    #print(out)
    try:
        n = int(out, 2)
        print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
        print(stringlist[lsfrbits])
    except:
        pass

    
    """for (ciphertext, keybits) in zip(cipherText, lsfrbits):
        #two strings to xor
        new = [(ord(a) ^ ord(b)) for a,b in zip(cipherText, lsfrbits)]
        
        print(type(new))
        n = int(new, 2)
        print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())"""

    
    


