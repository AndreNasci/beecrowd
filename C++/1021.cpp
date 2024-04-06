// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    double N;
    unsigned long notes;
    int note_values[] = {100, 50, 20, 10, 5, 2}, int_coin;
    int coin_values[] = {100, 50, 25, 10, 5, 1}, coin;

    cin >> N;

    notes = (int)N;

    cout << "NOTAS:" << endl;
    for (int i=0; i<6; i++)
    {
        cout << notes / note_values[i] << " nota(s) de R$ " << note_values[i] << ".00" << endl;
        notes = notes % note_values[i];
    }

    coin = (N - (int)N + notes) * 100;
    int_coin = (int)coin;
    cout << "MOEDAS:" << endl;
    cout << fixed << setprecision(2);
    for (int i=0; i<6; i++)
    {
        cout << int_coin / coin_values[i] << " moeda(s) de R$ " << coin_values[i]/100.0 << endl;
        int_coin = int_coin % coin_values[i];
    }

    return 0;
}