#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int t;
    cin>>t;
    while(t--){
        string s;
        cin>>s;
        vector<vector<int>>a(26);
        bool f=true;
        for(int i=1;i<s.length();i++){
            a[s[i]-'a'].push_back(s[i-1]-'a');
            a[s[i-1]-'a'].push_back(s[i]-'a');
            if(a[s[i]-'a'].size()>2||a[s[i-1]-'a'].size()>2){
                f=false;
                break;
            }
        }
        if(!f){
            cout<<"NO"<<endl;
            continue;
        }
        s="";
        for(int i=0;i<26;i++){
            if(a[i].size()==0){
                s+=('a'+i);
            }
        }
        
    }
    return 0;
}