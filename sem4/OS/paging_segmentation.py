def decimalToBinary(n): 
    return bin(n).replace("0b","") 

def binaryToDecimal(n): 
    return int(n,2) 

str = input("Enter 16 bit memory address:")
if (len(str) == 16):
    print("1.Paging 2.Segmentation")
    ch = int(input("enter your choice:"))
    if (ch == 1):
        pg = {'000000':'000100','101010':'011000','001010':'010100','000111':'101010'}

        ans = pg[str[:6]]+str[6:]

        print("Physical Address :",ans)

    elif (ch ==2):
        sg = {'0000':'1010100110010101','0010':'0001110001010110','0111':'1100010111010000',
        '1000':'0010000000100100','0101':'0011110010101000','1010':'0011111100110001','1111':'1000111011000101'}
        f4 = sg[str[:4]]
        b1 = binaryToDecimal(str[4:])
        b2 = binaryToDecimal(f4)
        d = b1 + b2 
        ans = decimalToBinary(d)
        print("Physical address :",ans)
        
    else:
        print("choice incorrect")

else:
    print("length not 16-bit")