// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    unsigned long N;
    
    cin >> N;

    cout << N / 365 << " ano(s)" << endl;
    N = N % 365;
    cout << N / 30 << " mes(es)" << endl;
    N = N % 30;
    cout << N << " dia(s)" << endl;
    return 0;
}