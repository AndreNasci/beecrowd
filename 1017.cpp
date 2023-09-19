// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int hours, speed, distance;

    cin >> hours;
    cin >> speed;

    distance = hours * speed;

    cout << fixed << setprecision(3) << distance / 12.0 << endl;
    return 0;
}