// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    double n1, n2, n3, n4, exam, average;

    cin >> n1 >> n2 >> n3 >> n4;

    average = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / (2 + 3 + 4 + 1);

    cout << fixed << setprecision(1);
    cout << "Media: " << average << endl;
    
    if (average >= 7)
    {
        cout << "Aluno aprovado." << endl;
    }
    else
    {
        if (average >= 5)
        {
            cout << "Aluno em exame." << endl;
            cin >> exam;
            cout << "Nota do exame: " << exam << endl;

            average = (average + exam) / 2;
            if (average >= 5.0)
            {
                cout << "Aluno aprovado." << endl;
                cout << "Media final: " << average << endl;
            }
            else {
                cout << "Aluno reprovado." << endl;
                cout << "Media final: " << average << endl;
            }
        }
        else
        {
            cout << "Aluno reprovado." << endl;
        }
    }
    


    return 0;
}