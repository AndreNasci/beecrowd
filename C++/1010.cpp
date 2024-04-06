// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int code1, code2, units1, units2;
    double price1, price2, total;

    cin >> code1 >> units1 >> price1;
    cin >> code2 >> units2 >> price2;

    total = units1 * price1 + units2 * price2;

    cout << "VALOR A PAGAR: R$ " << fixed << setprecision(2) << total << endl;
    return 0;
}