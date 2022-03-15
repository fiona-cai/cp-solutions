//https://dmoj.ca/problem/ccc22j3
//CCC '22 J3 - Harp Tuning

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1e5 + 5;

string s;

int main() {
    cin >> s;
    int i=0;
    string currans;
    while (i < s.size()) {
        if (s[i] == '+' || s[i] == '-') {
            cout << currans << (s[i] == '+' ? " tighten" : " loosen") << " ";
            i ++;
            while (isdigit(s[i])) {
                cout << s[i];
                i++;
            }
            cout << "\n";
            currans = "";
        } else {
            currans += s[i];
            i++;
        }
    }
    return 0 ;
}
