#include<iostream>
using namespace std;
int main() {
	int input; string pw;
	cin >> input;
	for (int i = 0; i < input; ++i)
	{
		cin >> pw;
		if (pw.length() >= 6 && pw.length() <= 9) cout << "yes" << endl;
		else cout << "no"<< endl;
	}
}