// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    unsigned long N;
    int values[] = {100, 50, 20, 10, 5, 2, 1};

    cin >> N;
    cout << N << endl;

    for (int i=0; i<7; i++)
    {
        cout << N / values[i] << " nota(s) de R$ " << values[i] << ",00" << endl;
        N = N % values[i];
    }

    return 0;
}