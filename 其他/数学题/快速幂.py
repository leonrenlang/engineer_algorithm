# 逐步推导： https://blog.csdn.net/qq_19782019/article/details/85621386

'''
#include<bits/stdc++.h>

using namespace std;
const int mod=1e9+7;
long long quick_pow(long long a,long long b){
    long long ans=1;
    while(b){
        if(b&1)ans=ans*a%mod;
        a=a*a%mod;
        b>>=1;
    }
    return ans;
}
int main(){
    long long n;
    cin>>n;
    cout<<n*quick_pow(2, n-1)%mod<<endl;
}


'''
