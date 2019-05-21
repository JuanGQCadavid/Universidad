


def gausssianSimple(Ab):
    Ub = elimination(Ab)
    print(str(Ub))
    #x = despeje(u,b)
    #return x

def elimination(Ab):

    rows_number = len(Ab) #Rows
    columns_number = len(Ab[0])

    for k in range(0,rows_number - 1):
        #print(Ab)
        print("****")
        for i in range(k + 1,rows_number):
            mik = Ab[i][k]/Ab[k][k]
            for j in range(k,columns_number):
                Ab[i][j] = Ab[i][j] - mik* Ab[k][j]
            
    return Ab

def despeje(u,b):
    pass

#Matrix aumentada n + 1
Ab = [[14,6,-2,3,12],
      [3,15,2,-5,32],
      [-7,4,-23,2,-24],
      [1,-3,-2,16,14]]

gausssianSimple(Ab)
