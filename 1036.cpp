// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    double a, b, c, delta, delta2;

    cin >> a >> b >> c;

    cout << fixed << setprecision(5);
    if (a == 0) {
        cout << "Impossivel calcular" << endl;
    }
    else {
        delta2 = b * b - 4 * a * c;
        if (delta2 < 0) {
            cout << "Impossivel calcular" << endl;
        }
        else {
            delta = sqrt(delta2);
            cout << "R1 = " << (0 - b + delta) / (2 * a) << endl;
            cout << "R2 = " << (0 - b - delta) / (2 * a) << endl;
        }
    }
    return 0;
}