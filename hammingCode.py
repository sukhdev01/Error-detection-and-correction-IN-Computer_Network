#!/usr/bin/env python
# coding: utf-8

# In[87]:


import numpy as np
if __name__=='__main__':
    length = int(input("Enter the length of the message "))
    r=0
    for i in range(1,20):
        if (2**i >=i + length+1):
            r=i
            break;
    print("R =",r,". (By 2^R >=",length,"+ R + 1)");print()
    message=input("\nEnter binary code of message for sending ")
#     eight=np.arange(8)
    eight=[0,1,2,3,4,5,6,7]
#     array=[[0]*r for i in range(2**r)]
    array=np.zeros([2**r,r],dtype=int)
    for j in range(1,r+1):
        for i in range(len(array)):
            if j==1 and i%2!=0:
                array[i][-1]=1
            if j==2 and (i%4 not in [0,1]):
                array[i][-2]=1
            if j==3 and (i%8 not in [0,1,2,3]):
                array[i][-3]=1
            if j==4 and (i%16 not in eight):
                array[i][-4]=1
    print(array)
    
    


# In[88]:


#adding r1, r2, r3, r4,.... in terms of R only
for i in range(r):
    message=message[:2**i-1]+'R'+message[2**i-1:]
print("message after adding parity as R is",message)  

#padding zeros
for j in range(len(message),2**r-1):
    message+='0'
print("after padding",message)


# In[89]:


#finding parity of R's and placing into message
parity=[]
parity_index=[]
for col in range(1,r+1):
    temp=[]
    for row in range(2**r):
        if (array[row][-col]==1):
            temp.append(row-1)
    parity_index.append(temp)
#     print(temp)
    #for finding parity
    sum_par=0
    for i in range(2**(r-1)):
        if message[temp[i]] !='R':
            sum_par+=int(message[temp[i]])

    tt=2**(col-1) -1    #index for replacing R with in its even parity
    if sum_par%2==0:
        parity.append(0)
        message=message[:tt]+'0'+message[tt+1:]
    else:
        parity.append(1)
        message=message[:tt]+'1'+message[tt+1:]
print("message after replacing R ",message,"and parities are",parity)  


# In[91]:


# message & parity_index & parity
print(message,"has sent by sender.") 
print("So, Enter the message of",length+r,"length for checking errors",end=' ');check_message=input()
result_bits=[]
for x in range(r-1,-1,-1):  #for starting reverse parity checking
    sum_par=0
    for i in range(len(parity_index[0])):    
        sum_par+= int(check_message[parity_index[x][i]])
    result_bits.append(sum_par%2)
print("\nresult in form of binary is",result_bits)
if sum(result_bits)==0:
    print("\nThere is no any error of one bit")
else:  #for converting array of 0/1 into string and then into binary code 
    st="".join(str(i) for i in result_bits)
    print("\nThe error is at",int(st,2))#converting into int

    

