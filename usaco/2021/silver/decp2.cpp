//USACO 2021 December Contest, Silver Problem 2. Connecting Two Barns
//http://www.usaco.org/index.php?page=viewproblem2&cpid=1159

#include <bits/stdc++.h>
using namespace std;
#define int long long
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1e5 + 5;
const int INF = 1e18 + 5;
int t, n, m, vis[maxn];
vi adj[maxn];
set<int> c[maxn];

void dfs(int u, int ori) {
    c[ori].insert(u);
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) dfs(v, ori);
    }
}

void solve() {
    memset(vis, false, sizeof vis);
    cin >> n >> m;
    for (int i=1; i <=n; i++) {adj[i].clear(); c[i].clear();}
    for (int i =0; i <m; i++) {
        int u, v; cin >> u >> v;
        adj[u].PB(v); adj[v].PB(u);
    }
    dfs(1, 1); dfs(n, n);
    for (int i =2; i <=n-1; i++) {
        if (!vis[i]) dfs(i, i);
    }

    int ans = INF;
    set<int> c1 = c[1], c2 = c[n];
    for (int i =2; i <=n-1; i++) {
        int cans1 = INF, cans2 = INF;
        for (auto u : c[i]) {
            auto it = c1.lower_bound(u);
            if (it != c1.end()) cans1 = min(cans1, *it - u);
            if (it != c1.begin()) cans1 = min(cans1, (u-*--it));

            auto it2 = c2.lower_bound(u);
            if (it2 != c2.end()) cans2 = min(cans2, (*it2 - u));
            if (it2 != c2.begin()) cans2 = min(cans2, (u-*--it2));
            ans = min(ans, (cans1*cans1) + (cans2*cans2));
        }
    }

    for (auto u : c1) {
        auto it = c2.lower_bound(u);
        if (it != c2.end()) ans = min(ans, (*it - u)*(*it-u));
        if (it != c2.begin()) ans = min(ans, (u-*--it)*(u-*it));
    }

    cout << ans << "\n";

}

signed main() {
    cin >> t;
    while (t--) solve();
}
