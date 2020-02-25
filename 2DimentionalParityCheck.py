#!/usr/bin/env python
# coding: utf-8

# In[10]:


def testing(reciever,div=5):
    
    message=str()
    length=len(reciever)
    #removing last column parity
    col = reciever[length-div:]
    reciever = reciever[:length-div]
    
    #checking error at parity in rows(added in middle by sender) and then removing
    row=[]
    row_count=0
    while(reciever):
        chunk = reciever[:div]
        old_parity=int(reciever[div])
        reciever = reciever[div+1:]
        message+=chunk
        
        sum_chunk=0
        for i in range(div):
            sum_chunk += int(chunk[i])
        if old_parity != (sum_chunk%2):
            row.append(row_count)
        row_count+=1
        
    print("Error in row_parity at",row)      
    
    #checking parity in columns
    col_len=len(message)//div
    col_parity=[]
    for j in range(div):
        sum_chunk=0
        for i in range(col_len):
            sum_chunk += int(message[i*div+j])
        if int(col[j]) != (sum_chunk%2):
            col_parity.append(j)
            
    print("Error in col_parity at",col_parity)        
    print("message received",message)
    
    if len(row)==0 and len(col_parity)==0:
        print("\nThere is no any error.")
    else:
        for i in range(len(row)):
            idx=row[i]*div+col_parity[-(i+1)]
            print("error found in the message at index",idx)
         
            if message[idx]==0:
                message=message[:idx]+'1'+message[idx+1:]
            else:
                message=message[:idx]+'0'+message[idx+1:]
            print("\nMessage after correcting at index",idx,"is",message)       
    print("\nFinal message is",message)


# In[11]:


# def test(sender,reciever,div=4):
#     length=len(reciever)
#     #removing last column parity
#     send = sender[length-div:]
#     rec = reciever[length-div:]
    
#     #testing row parity
#     column_len=(length-div)//(div+1)    # after removing last column parity
#     row=[]
#     for i in range(1,column_len):
#         x=i*(div+1)-1
#         if sender[x]!=reciever[x]:
#             row.append(i-1)
                
#     #testing column parity
#     col=[]
#     for i in range(div):
#         if send[i]!=rec[i]:
#             col.append(i)
#     idx=(div+1)*(row[0])+col[0]
#     print("row error is", row[0]+col[0])
#     if reciever[row[0]+col[0]]==0:
#         reciever=reciever[:idx]+'1'+reciever[idx+1:]
#     else:
#         reciever=reciever[:idx]+'0'+reciever[idx+1:]
#     print(reciever)


# In[12]:


def addingParity(string,div=5):
    message=str()
    #adding parity in rows format
    while(string):
        chunk = string[:div]
        string = string[div:]
        message+=chunk
        
        sum_chunk=0
        if len(chunk)==div:
            for i in range(div):
                sum_chunk += int(chunk[i])
            #parity adding
            message+=str(sum_chunk%2) 
        else:
            for i in range(div-len(chunk)): #padding zeros
                message+='0'
            for i in range(len(chunk)):
                sum_chunk += int(chunk[i])
            #parity adding  
            message +=str(sum_chunk%2)
            
    #adding parity in columns format
    column_len=len(message)//(div+1)
    for i in range(div):
        sum_column=0
        for j in range(column_len):
            sum_column += int(message[i+(div+1)*j])
        message += str(sum_column%2)
    return message


# In[13]:


if __name__=='__main__':

    input_message=input("\nEnter binary code for sending a message ")

    sender_message=addingParity(input_message)
    print("sender message ",sender_message)
    input_test=input("\nEnter binary code for testing of message ")

#     reciever_message=addingParity(input_test)
#     print("reciever message ",reciever_message)  
    print("\nTesting result is here.......")
#     test(sender_message,reciever_message)
    testing(input_test)



# In[14]:


rec='01011110011001101010010101001'
se='01011110001001001011010101001'
mSenDer='01011100010100111010'
#works only for diagoal [in case of more than 1 bit error]
#It always corrects 1 bit error

