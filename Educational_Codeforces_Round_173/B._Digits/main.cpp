#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int n_tests;

    cin >> n_tests;
    for (int i = 0; i < n_tests; ++i)
    {
        int n, d;
        cin >> n >> d;
        cout << 1 << " ";

        if (d % 3 == 0 || n >= 3)
            cout << 3 << " ";
        if (d == 5)
        {
            cout << 5 << " ";
        }
        if (d == 7 || n >= 7)
        {
            cout << 7 << " ";
        }
        if (d == 9 || n >= 6)
        {
            cout << 9 << " ";
        }
        cout << endl;
    }
}