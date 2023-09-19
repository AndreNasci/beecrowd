// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int maiorab(int a, int b);

int main()
{
    int a, b, c, maior;

    cin >> a >> b >> c;

    maior = maiorab(a, b);
    maior = maiorab(maior, c);
    
    

    cout << maior << " eh o maior" << endl;

    return 0;
}

int maiorab(int a, int b)
{
    return (a + b + abs(a - b)) / 2;
}