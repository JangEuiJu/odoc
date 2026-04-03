#include <iostream>
#define fio cin.tie(0)->sync_with_stdio(0)
using namespace std;

#include <map>
int main(){
    fio;
    int T; cin >> T;
    for(int t = 1; t <= T; t++){
        int N; cin >> N;
        map<int, int> map_;
        for(int i=1; i<=N; i++){
            int tmp; cin >> tmp;
            if(map_.find(tmp) == map_.end()){
                map_[tmp] = i;
            }
        }
        //
        int ans = 0;
        map<int, int>::iterator iter;
        for(iter = map_.begin(); iter!=map_.end(); iter++){
            ans = max(ans, (*iter).second);
        }
        cout <<"Case "<<t<<": "<<ans<<'\n';
    }

    return 0;
}