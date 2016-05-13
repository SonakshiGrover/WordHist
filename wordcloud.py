

import string


fin=open('story.py','r')   # We manually copy paste the webpage onto the text file 'story.txt' 
fout=open('dict.py','w')   # contains distinct words ( which  are not stop words ) along with  their frequencies
fin2=open('stop.py','r')   # contains all the stop words
fout2=open('rfile.py','w') # contains all the words( which are not stop words) and this file will be passed to R  make a histogram

d=dict()


def chkdigit(m):                        # to check for digits 
    for i in m:
            if i.isdigit()==1:
                return 1
    return 0

def chkword(n):             # to check whether a word is a stop word or not 
    flag=0
    for line in fin2:
        for v in line.split():
            if v==n:
                flag=1
            elif v==n.lower():
                flag=1
                
    fin2.seek(0,0)
    if (flag==1):
        return 1
    else:
        return 0            
        
line=fin.readline()
for line in fin:
    for word in line.split():
        word=word.strip(string.punctuation)
        if(chkdigit(word)!=1):
            
            if (chkword(word)!=1):
                fout2.write("{}".format(word))
                fout2.write("\n")
                if word not in d:                    # making  a dictionary
                    d[word] = 1
                else:
                    d[word]+=1
   
                

e=dict()

for word in d:             
    value=d[word]
    if value not in e:
        e[value]=[word]
    else:
        e[value].append(word)

    
def bub(x):                              #sorting the dictionary in descending order 
    for i in range(len(x)-2,-1,-1):
        for j in range(0,i+1):
            if x[j]<x[j+1]:
                tmp=x[j]
                x[j]=x[j+1]
                x[j+1]=tmp
    return x                

x=[]
for i in d:
    x.append(d[i])
   

x=list(set(x))

x=bub(x)



for j in x:
    for word in e[j]:
        fout.write("{}".format(word))
        fout.write("{}".format(j))
        fout.write("\n")
        

fin.close()
fout.close()
fin2.close()
fout2.close()

print(" THE END")

