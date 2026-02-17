#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
int main() {
    
    int ans=-1;
    int N,S,D,F,B,K;
    cin>>N>>S>>D>>F>>B>>K;
    
    int k;
    vector<int> visited(N+1,0);
    for(int i=0;i<K;i++){
        cin>>k;
        visited[k]=-1; 
    }
    
    queue<pair<int,int>> q;
    q.push(make_pair(S,0));
    while(!q.empty()){
        int location=q.front().first;
        int cnt=q.front().second;
        q.pop();
        
        if(location==D){
            ans=cnt;
            break;
        }
        
        if(location+F<=N && visited[location+F]==0){
            visited[location+F]++;
            q.push(make_pair(location+F,cnt+1));
        }
        
        if(location-B>=1 && visited[location-B]==0){
            visited[location-B]++;
            q.push(make_pair(location-B,cnt+1));
        }
    }
    
    if(ans==-1) cout<<"BUG FOUND"<<endl;
    else    cout<<ans<<endl;
    
    return 0;
}
 