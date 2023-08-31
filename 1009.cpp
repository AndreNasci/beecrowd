// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    char name[255];
    cin >> name;

    double salary, sales, total;
    cin >> salary >> sales;

    total = salary + 0.15 * sales;

    cout << "TOTAL = R$ " << fixed << setprecision(2) << total << endl;
    return 0;
}