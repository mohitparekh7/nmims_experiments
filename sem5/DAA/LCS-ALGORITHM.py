def createZeroMatrix(m,n):
    l1 = []
    for i in range(m+1):
        l = []
        for j in range(n+1):
            x = 0
            l.append(0)
        l1.append(l)
    return l1

def lcsAlgorithm(seq1,seq2):
    m = len(seq1)
    n = len(seq2)
    c = createZeroMatrix(m,n)
    b = createZeroMatrix(m,n)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if seq1[i-1] == seq2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    
    index = c[m][n]
    LCS = [""] * (index+1)
    LCS[index] = ""
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            LCS[index-1] = seq1[i-1]
            i = i - 1
            j = j - 1
            index = index - 1
        elif c[i-1][j] > c[i][j-1]:
            i = i - 1
        else:
            j = j - 1
    
    print("LCS TABLE: ")
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                print(" " , end=" ")
            elif i == 0:
                print(seq2[j-1], end=" ")
            elif j == 0:
                print(seq1[i-1], end=" ")
            else:
                print(c[i][j],end= " ")
        print()

    print("Longest Common Subsequence between ", seq1, " and ", seq2, ": ", "".join(LCS))
    print("Length of Longest Common Subsequence: ", c[m][n])
        



sequence1 = input("Enter DNA sequence 1: ")
sequence1 =  sequence1.upper()
sequence2 = input("Enter DNA sequence 2: ")
sequence2 = sequence2.upper()

check = set("ACGT")

if set(sequence1).issubset(check) and set(sequence2).issubset(check):
    lcsAlgorithm(sequence1,sequence2)
else:
    print("Invalid DNA Sequence Entered!")


