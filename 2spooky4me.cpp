//https://dmoj.ca/problem/2spooky4me
//2spooky4me

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 20005;

int n, l, s, ans;
map<int, int> v;
map<pi, int> mp2;

int main() {
    cin >> n >> l >> s;
    for (int i =0; i < n; i++) {
        int a,b,s;
        cin >> a >> b >> s;
        v[a] = 0;
        v[b+1] = 0;
        mp2[{a, b+1}] += s;
    }
    vi rv;
    rv.PB(0);
    int cnt = 0;
    for (auto &x : v) {x.S = ++cnt; rv.PB(x.F);}
    vi diff((2*n)+1, 0);
    for (auto e : mp2) {
        int a = e.F.F, b = e.F.S, s = e.S;
        diff[v[a]] += s; diff[v[b]] -= s;
    }
    int last = 0;
    for (int i =1; i <= 2*n; i++) {
        diff[i] += diff[i-1];
        if (diff[i] >= s) {
            assert(rv[i]-1 - last >= 0);
            ans += rv[i]-1 - last;
            if (i != 2*n) last = rv[i+1]-1;
        }
    }
    ans += l-last;
    cout << ans << "\n";
}
