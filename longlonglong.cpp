#include<bits/stdc++.h>
#include<vector>

using namespace std;

long long TotalCustomerPenalties(vector<int> InitialAsk) {
    
   queue<array<long long,3>>q;
    int n = InitialAsk.size();
    vector<bool>vis(n+1,false);
    long long ans =0LL;
    
    for(int&i : InitialAsk){
        if(!vis[i])
            vis[i]= true;
            
        else {
            q.push({i+1,0,1LL});
        }
    }
    	while(q.size()>0){
        
        auto curr = q.front();
        q.pop();
        
        if(vis[curr[0]]==false){
            vis[curr[0]]=true;
            ans+=(curr[2]*1LL);
            continue;
        }
        
        curr[0]++;
        curr[1]++;
        curr[2]+=(long long)pow(2,curr[1]);
        q.push(curr);
    }
    
    ans*=10LL;
    
    return ans;

}

int main(int argc, char const *argv[])
{
    /* code */
    int a=10, b=2, c;
    a = !(c=c==c) &&++b;
    printf("%d-%d-%d", b, c,a);
    return 0;
}