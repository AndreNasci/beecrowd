// André Nascimento
// GitHub: github.com/AndreNasci
// Linkedin: linkedin.com/in/andre-nascimento-a01095185

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int worked_hours, number;
    double salary, per_hour;

    cin >> number;
    cin >> worked_hours;
    cin >> per_hour;

    salary = worked_hours * per_hour;

    cout << "NUMBER = " << number << endl;
    cout << "SALARY = U$ " << fixed << setprecision(2) << salary << endl;
    return 0;
}
