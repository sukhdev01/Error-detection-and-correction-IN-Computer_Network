#include<iostream>
#include<bits/stdc++.h>
using namespace std;


string findErrorFun(int msgRec[],int len){
	int NewParity,sum=0;
	for (int i=0;i<len;i++)
		sum+=msgRec[i];
	NewParity=sum%2;
	if (msgRec[len] == NewParity)
		return "No any error of one bit (might be more than one)\n";
	else
		return "Code have some error\n";
}

int main(){
	int l;
	cout<<"Enter the message code length and message \n";
	cin>>l;
	int msgSend[l], msgRec[l+1];
	int var;
	for(int i=0;i<l;i++){
		cin>>var;
		msgSend[i]=var;
	}
	int parity,sum=0;
	for (int i=0;i<l;i++)
		sum+=msgSend[i];
	parity=sum%2;
	bool input=true;
	while(input){
		cout<<"Enter message of "<<l<<" length to find error and message\n";	
		for(int i=0;i<l;i++){
			cin>>var;
			msgRec[i]=var;
		}
		msgRec[l]=parity;
		cout<<" result : "<<findErrorFun(msgRec,l)<<endl;
		cout<<"for checking further, Enter '1'. if no enter '0' "<<endl;
		cin>>input;
	}
	return 0;
}
