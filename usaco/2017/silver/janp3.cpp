//USACO 2017 January Contest, Silver Problem 3. Secret Cow Code
//http://www.usaco.org/index.php?page=viewproblem2&cpid=692

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e5 + 5;

ll n;
string s;

char solve(ll i, ll l) {
    if (i < s.size()) return s[i];
    if (i < l/2) return solve(i, l/2);
    else return solve((i-1)%(l/2), l/2);
}

int main() {
    freopen("cowcode.in", "r", stdin);
    freopen("cowcode.out", "w", stdout);
    cin >> s >> n;
    ll tot = s.size();
    while (tot < n) {
        tot*=2;
    }
    cout << solve(n-1, tot) << "\n";
}
