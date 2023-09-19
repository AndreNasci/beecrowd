// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    double N;
    int flag = -1;

    cin >> N;

    if (N < 0 || N > 100) {
        cout << "Fora de intervalo" << endl;
    }
    else
    {
        cout << "Intervalo ";
        if (N <= 25.0) 
        {
            cout << "[0,25]" << endl;
        }
        else 
        {
            if (N <= 50.0)
            {
                cout << "(25,50]" << endl;
            }
            else
            {
                if (N <= 75.0)
                {
                    cout << "(50,75]" << endl;
                }
                else
                {
                    if (N <= 100.0)
                    {
                        cout << "(75,100]" << endl;
                    }
                }
            }
        }
    }
    return 0;
}