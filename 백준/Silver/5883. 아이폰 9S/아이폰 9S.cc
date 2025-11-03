#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[1001];
int max_length = -987654321;
int main(void){
    int n;
    cin >> n;
    for(int i = 0;i<n;i++){
        cin >> arr[i];
    }

    
    vector<int> Person;
    for(int i = 0;i<n;i++){
        Person.clear();
        for(int j = 0;j<n;j++){
            if(arr[i] != arr[j]){
                Person.push_back(arr[j]);
            }
        }

        for(int p = 0;p<Person.size();p++){
            bool is_end = false;
            int length = 1;
            for(int q = p+1;q<Person.size();q++){
               if(Person[p] != Person[q]){
                is_end = true;
                break;
               }
               length++;
            }
            max_length = max(length,max_length);
        }
    }
    cout << max_length;

}