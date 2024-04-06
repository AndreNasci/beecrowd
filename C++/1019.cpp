// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    unsigned long N, hours, minutes;

    cin >> N;

    hours = N / 3600;
    minutes = N % 3600 / 60;

    cout << hours << ":" << minutes << ":" << N - hours*3600 - minutes*60 << endl;
    return 0;
}