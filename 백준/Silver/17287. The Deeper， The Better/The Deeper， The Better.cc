#include <iostream>
using namespace std;
int main()
{
    string s;
    int max = -1,sum = 0;

    cin>>s;

    for(int i=0; i<s.size(); i++)
    {
        if(s[i] == '[')
        {
            sum += 3;
        }
        else if(s[i] == '{')
        {
            sum += 2;
        }
        else if(s[i] == '(')
        {
            sum += 1;
        }
        else if(s[i] == ')')
        {
            sum -= 1;
        }
        else if(s[i] == '}')
        {
            sum -= 2;
        }
        else if(s[i] == ']')
        {
            sum -= 3;
        }
        else if(s[i] >= '0' && s[i] <= '9')
        {
            if(sum > max)
                max = sum;
        }
    }
    cout<<max;
    return 0;
}