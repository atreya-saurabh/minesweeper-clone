import random as r

F = 'X'

def InputDimensions():
    X=int(input("Enter X: "))
    Y=int(input("Enter Y: "))
    return X,Y

def InputCoeff():
    Z=float(input("Enter %age of mines: "))
    print("")
    return (Z/100)

def generateList(S,P):
    A=[]
    for i in range(int(S*P)):
        A.append(1)
    for j in range(int(S*(1-P))):
        A.append(0)
    while len(A) < S:
        A.append(r.choice([0,1]))
    A=A[:S]
    r.shuffle(A)
    return A

def generateMines(X,Y,P):
    G=generateList(X*Y,P)
    I=0
    k=[]
    for i in range(Y):
        h=[]
        for j in range(X):
            h.append(G[I])
            I+=1
        k.append(h)
    return k

def generateBlank(X,Y):
    k=[]
    for i in range(Y):
        h=[]
        for j in range(X):
            h.append(0)
        k.append(h)
    return k

def generateFull(X,Y):
    k=[]
    for i in range(Y):
        h=[]
        for j in range(X):
            h.append(1)
        k.append(h)
    return k

def ComputeNumbers(M,X,Y):
    T=generateBlank(X,Y)
    for i in range(Y):
        for j in range(X):
            if M[i][j]==1:
                t=(i>=1)
                b=(i<(Y-1))
                l=(j>=1)
                r=(j<(X-1))
                if t:
                    T[i-1][j]+=1
                    if l:
                        T[i-1][j-1]+=1
                    if r:
                        T[i-1][j+1]+=1
                if l:
                    T[i][j-1]+=1
                if r:
                    T[i][j+1]+=1
                if b:
                    T[i+1][j]+=1
                    if l:
                        T[i+1][j-1]+=1
                    if r:
                        T[i+1][j+1]+=1
    for i in range(Y):
        for j in range(X):
            if (M[i][j]==1):
                T[i][j]=9
    return T

def RevZero(T,R,PX,PY,X,Y):
    t=(PY>=1)
    b=(PY<(Y-1))
    l=(PX>=1)
    r=(PX<(X-1))
    if t:
        if T[PY-1][PX]!=9:
            if T[PY-1][PX]==0 and R[PY-1][PX]==0:
                R[PY-1][PX]=1
                R=RevZero(T,R,PX,PY-1,X,Y)
            R[PY-1][PX]=1
        if l:
            if T[PY-1][PX-1]!=9:
                if T[PY-1][PX-1]==0 and R[PY-1][PX-1]==0:
                    R[PY-1][PX-1]=1
                    R=RevZero(T,R,PX-1,PY-1,X,Y)
                R[PY-1][PX-1]=1
        if r:
            if T[PY-1][PX+1]!=9:
                if T[PY-1][PX+1]==0 and R[PY-1][PX+1]==0:
                    R[PY-1][PX+1]=1
                    R=RevZero(T,R,PX+1,PY-1,X,Y)
                R[PY-1][PX+1]=1
    if l:
        if T[PY][PX-1]!=9:
            if T[PY][PX-1]==0 and R[PY][PX-1]==0:
                R[PY][PX-1]=1
                R=RevZero(T,R,PX-1,PY,X,Y)
            R[PY][PX-1]=1
    if r:
        if T[PY][PX+1]!=9:
            if T[PY][PX+1]==0 and R[PY][PX+1]==0:
                R[PY][PX+1]=1
                R=RevZero(T,R,PX+1,PY,X,Y)
            R[PY][PX+1]=1
    if b:
        if T[PY+1][PX]!=9:
            if T[PY+1][PX]==0 and R[PY+1][PX]==0:
                R[PY+1][PX]=1
                R=RevZero(T,R,PX,PY+1,X,Y)
            R[PY+1][PX]=1
        if l:
            if T[PY+1][PX-1]!=9:
                if T[PY+1][PX-1]==0 and R[PY+1][PX-1]==0:
                    R[PY+1][PX-1]=1
                    R=RevZero(T,R,PX-1,PY+1,X,Y)
                R[PY+1][PX-1]=1
        if r:
            if T[PY+1][PX+1]!=9:
                if T[PY+1][PX+1]==0 and R[PY+1][PX+1]==0:
                    R[PY+1][PX+1]=1
                    R=RevZero(T,R,PX+1,PY+1,X,Y)
                R[PY+1][PX+1]=1
    return R

def Rev(M,R,T,PX,PY,X,Y):
    if M[PY][PX]:
        for i in range(Y):
            for j in range(X):
                if M[i][j]:
                    R[i][j]=1
        return True, R
    else:
        if T[PY][PX]!=0:
            R[PY][PX]=1
            return False, R
        else:
            R[PY][PX]=1
            R=RevZero(T,R,PX,PY,X,Y)
            return False, R

def printblank(K,X,Y,V):
    print("  ", end="")
    for i in range(X):
        print(chr(97+i),end=" ")
    print("")
    for j in range(Y):
        print(chr(65+j),end=" ")
        print("%c "%F*X,end=" ")
        print(chr(65+j))
    print("  ", end="")
    for i in range(X):
        print(chr(97+i),end=" ")
    print("")

def printrev(K,N,X,Y,V):
    print("  ", end="")
    for i in range(X):
        print(chr(97+i),end=" ")
    print("")
    for j in range(Y):
        print(chr(65+j),end=" ")
        for i in range(X):
            if K[j][i]:
                print(N[j][i],end=" ")
            else :
                print(F,end=" ")
        print(chr(65+j))
    print("  ", end="")
    for i in range(X):
        print(chr(97+i),end=" ")
    print("")

def InputPos(X,Y):
    try:
        s=str(input("\nEnter Position (xX): "))
        x,y=ord(s[0])-97, ord(s[1])-65
    except:
        print("\nInvalid Input. Try again.")
        x,y=InputPos(X,Y)
        return x,y    
    if not ((0<=x<X)and(0<=y<Y)):
        print("\nBeyond boundaries. Try again.")
        x,y=InputPos(X,Y)
    print("")
    return x,y
    
def CheckWin(M,R,X,Y):
    for i in range(Y):
        for j in range(X):
            if M[i][j]==R[i][j]:
                return False
    return True

def main():
    m,n=InputDimensions()
    p=InputCoeff()
    h=generateMines(m,n,p)
    k=generateBlank(m,n)
    k1=generateFull(m,n)
    g=ComputeNumbers(h,m,n)
    printrev(k,g,m,n,0)
    #printrev(k1,g,m,n,0)
    while 1:
        x,y=InputPos(m,n)
        b,k=Rev(h,k,g,x,y,m,n)
        #print("%d\n"%b)
        printrev(k,g,m,n,0)
        #printrev(k1,g,m,n,0)
        if b:
            print("\n==========\n|YOU LOST|\n==========\n")
            input()
            break
        if CheckWin(h,k,m,n):
            print("\n=========\n|YOU WON|\n=========\n")
            input()
            break

main()