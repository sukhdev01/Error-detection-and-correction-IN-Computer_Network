#!/usr/bin/env python
# coding: utf-8

# In[1]:



def binSum(chunk1,chunk2,div=8):
    
    st=bin(int(chunk1,2)+int(chunk2,2))
    
    if len(st)==div+3:   #for removing first 0b from binay code 0bxxxxxx
        carry='1'
        st1=st[3:]
        st= binSum(st1,carry)
        return st
    else:
        return st[2:]


# In[2]:


def findCheckSum(message,div=8):
    mess_len=len(message)
    
    temp=message[:div]
    message=message[div:]
    for i in range((mess_len//div)-1):
        temp=binSum(temp,message[:div])
        message=message[div:]

    checkSum=temp
    #for taking compliment of check_sum
    for i in range(len(checkSum)):
        if checkSum[i]=='0':
            checkSum=checkSum[:i]+'1'+checkSum[i+1:]
        else:
            checkSum=checkSum[:i]+'0'+checkSum[i+1:]
    return checkSum


# In[3]:



def paddingZeros(message,div=8):
    if (len(message)%div!=0):
        for i in range(len(message)%div):
            message+='0'
    return message


# In[6]:


10011001111000100010010010000100


# In[5]:


if __name__=='__main__':
    
    #sender side
    send_message=input("enter sender message  ")
    sender_check_sum=findCheckSum(paddingZeros(send_message))
    
    print("check sum of sender",sender_check_sum)
    
    #reciever side checking
    rec_message=input("enter recieved message ")
    rec_check_sum=findCheckSum(paddingZeros(rec_message))
    
#     st=bin(int(sender_info,2)+int(reciever_info,2))
    
    if (sender_check_sum==rec_check_sum):
        print("\nNo error")
    else:
        print("\nerror is present")

