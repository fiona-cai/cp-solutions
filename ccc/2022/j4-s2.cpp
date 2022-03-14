//https://dmoj.ca/problem/ccc22s2
//CCC '22 S2 - Good Groups

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 3e5 + 5;

int x, y, g, parent[maxn];
set<pair<string, string>> cons;  map<pair<string, string>, bool> cons2;
map<string, int> nameToV;



int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> x;
    while (x--) {
        string a, b; cin >> a >> b;
        cons2[{min(a,b), max(a,b)}] = false;

    }
    cin >> y;
    while (y--) {
        string a, b; cin >> a >> b;
        cons.insert({min(a, b), max(a, b)});
    }
    cin >> g;

    int lasti = 1;
    int ans = 0;
    for (int i=1; i <=g; i++)  {
        string a,b,c; cin >> a >> b >> c;
        nameToV[a] = lasti; nameToV[b] = lasti+1; nameToV[c] = lasti+2;
        lasti += 3;
        if (cons.count({min(a, b), max(a,b)}) > 0) ans ++;
        if (cons.count({min(c, b), max(c,b)}) > 0) ans ++;
        if (cons.count({min(a, c), max(a,c)}) > 0) ans ++;
        cons2[{min(a, b), max(a,b)}] = true;
        cons2[{min(c, b), max(c,b)}] = true;
        cons2[{min(a, c), max(a,c)}] = true;
    }

    for (auto e : cons2) {
        if (!e.S) ans ++;
    }
    cout << ans << "\n";

}
