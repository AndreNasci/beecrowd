// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    unsigned long A, B, C, D;
    int flag = 0;

    cin >> A >> B >> C >> D;

    if (B > C && D > A)
    {
        if (C+D > A+B)
        {
            if (C >= 0 && D >= 0)
            {
                if (A % 2 == 0)
                {
                    cout << "Valores aceitos" << endl;
                    flag = 1;
                }
            }
        }
    }
    if (!flag) cout << "Valores nao aceitos" << endl;
    return 0;
}