#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N;
  cin >> N;

  while (N--) {
    string seminar;
    cin >> seminar;

    if (seminar == "Algorithm") cout << "204\n";
    else if (seminar == "DataAnalysis") cout << "207\n";
    else if (seminar == "ArtificialIntelligence") cout << "302\n";
    else if (seminar == "CyberSecurity") cout << "B101\n";
    else if (seminar == "Network") cout << "303\n";
    else if (seminar == "Startup") cout << "501\n";
    else if (seminar == "TestStrategy") cout << "105\n";
  }
  
  return 0;
}