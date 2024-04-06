// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    double x1, y1, x2, y2, dist;

    cin >> x1 >> y1;
    cin >> x2 >> y2;

    dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    cout << fixed << setprecision(4) << dist << endl;

    return 0;
}