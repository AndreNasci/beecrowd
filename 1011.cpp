// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    double R, volume;

    cin >> R;

    volume = 4/3.0 * 3.14159 * pow(R,3);

    cout << "VOLUME = " << fixed << setprecision(3) << volume << endl;
    return 0;
}