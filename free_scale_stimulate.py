__author__ = 'Freasy'

from numpy import *

set_printoptions(threshold='nan')

def getConnection(a,b):

    dataMat[a][b] = 1

    edges[a] = edges[a] + 1

    edges[b] = edges[b] + 1

    return 0

dataMat = zeros((100,100))

edges = zeros(100)

edgesRate = zeros(100)

for i in range(5,100):

    if i == 5 :


        getConnection(5,0)
        getConnection(5,1)
        getConnection(5,2)
        getConnection(5,3)
        getConnection(5,4)
        edgesRate= edges / (2*(i-4)*5)
        print edgesRate
        continue

    print edgesRate

    ranNumMat=array([0,0,0,0,0])

    j=0

    while j<5:

        ranNumber=random.uniform(0, 1)

        rate=ranNumber



        for k in range (0,i):

            if edgesRate[k] > rate:

                break

            rate = rate - edgesRate[k]

        check = 1

        for l in range (0,j):

            if k== ranNumMat[l] :

                check = 0

        if check == 1 :

            ranNumMat[j]=k

            j=j+1






    print ranNumMat

    for j in range (0,5):

        x=int(i)

        y=int (ranNumMat[j])

        getConnection(x,y)

    edgesRate= edges / (2*(i-4)*5)
    #print edgesRate
    #print edges
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")
print ("datamat___________________________________________________________________________________")

print dataMat

