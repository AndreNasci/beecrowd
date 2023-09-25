// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int x, y;

    cin >> x >> y;

    cout << "Total: R$ ";
    cout << fixed << setprecision(2);

    switch(x)
    {
        case 1:
            cout << y * 4.00 << endl;
            break;
        case 2:
            cout << y * 4.50 << endl;
            break;
        case 3:
            cout << y * 5.00 << endl;
            break;
        case 4:
            cout << y * 2.00 << endl;
            break;
        case 5:
            cout << y * 1.50 << endl;
            break;
        default:
            break;
    }
    return 0;
}