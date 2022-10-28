class Solution {   
   
public:
    char Sum(char a, char b,char c){
       if(a=='1'&&b=='1'&&c=='1')
            return '1';
       if(a=='1'&&b=='1'&&c=='0')
            return '0'; 
       if(a=='1'&&b=='0'&&c=='0')
            return '1'; 
       if(a=='1'&&b=='0'&&c=='1')
            return '0'; 
       if(a=='0'&&b=='1'&&c=='0')
            return '1'; 
       if(a=='0'&&b=='1'&&c=='1')
            return '0'; 
       if(a=='0'&&b=='0'&&c=='0')
            return '0';     
       if(a=='0'&&b=='0'&&c=='1')
            return '1'; 
        else return '0';      
    }
    char Carry(char a, char b,char c){
       if(a=='1'&&b=='1'&&c=='1')
            return '1';
       if(a=='1'&&b=='1'&&c=='0')
            return '1';
       if(a=='1'&&b=='0'&&c=='0')
            return '0';
       if(a=='1'&&b=='0'&&c=='1')
            return '1';
       if(a=='0'&&b=='1'&&c=='0')
            return '0';
       if(a=='0'&&b=='1'&&c=='1')
            return '1';
       if(a=='0'&&b=='0'&&c=='1')
            return '0'; 
       if(a=='0'&&b=='0'&&c=='0')
            return '0';
        else return '0';
    }
    string addBinary(string a, string b) {
string c;
        int len,len2,len3;
        char carry='0',sum='0';
        len=a.size();
        len2=b.size();
        if(len2<len){
        	for(int i=0;i<len-len2;i++)
        	b.insert(0,"0"); 
        }
        if(len<len2){
        	for(int i=0;i<len2-len;i++)
        	a.insert(0,"0");
        }
        len3=a.size()>b.size()?a.size()-1:b.size()-1;     
        for(int i=len3;i>=0;i--)
        {  
sum=Sum(a[i],b[i],carry);                       
        c+=sum;
        carry=Carry(a[i],b[i],carry) ;     
            }      
            if(carry=='1')
            c+='1';
            reverse(c.begin(),c.end());
           return c;               
    }
};