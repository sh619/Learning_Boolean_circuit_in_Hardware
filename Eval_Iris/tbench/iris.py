#Python script to read iris data and binarized the parameters

import numpy as np

## read data from iris dataset and normalize to [0,1]
file = open("Iris.txt", "r")
lines= file.readlines()
filename='Iris_bi.txt'
with open(filename,"w") as f:
    for line in lines:
        s=line.split(",")
        flower=s[len(s)-1]
        a=[float(j) for j in s[0:4:1]]
        for i in a:
            if((i-min(a))/(max(a)-min(a)))>0.5:
                f.write("1")
            else :
                f.write("0")
        if flower == "Iris-setosa\n" :
            f.write("1\n")
        else:
            f.write("0\n")
file.close()

#Write the trained data and test data to corresponding files
tr = open("Iris_train.txt", "w")
t = open("Iris_test.txt","w")
with open(filename,"r") as fd:
        for i in range(len(lines)):
            line = fd.readline()
            if(i<=0 and i<40):
                tr.write(line)
            elif(i>=40 and i<60):
                t.write(line)
            else:
                tr.write(line)
tr.close()
t.close()





