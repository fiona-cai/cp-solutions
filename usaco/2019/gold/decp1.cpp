//https://dmoj.ca/problem/usaco19decgoldp1
//USACO 2019 December Gold P1 - Milk Pumping

#include <bits/stdc++.h>
using namespace std;
#define int long long
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1e3 + 2;

int n, m, dist[maxn];
struct e {int v, w, f; };
vector<e> adj[maxn]; vi flows;

int dij(int f) {
    memset(dist, 0x3f, sizeof dist); dist[1] = 0;
    priority_queue<pi, vector<pi>, greater<pi>> pq;
    pq.push({0, 1});
    while (!pq.empty()) {
        auto [d, u]  = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        if (u == n) return dist[u];
        for (auto [v, w, fx] : adj[u]) {
            if (fx < f) continue;
            if (dist[u] + w < dist[v]) {
                dist[v] = d+w; pq.push({dist[v], v});
            }
        }
    }
    return -1;
}

signed main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> m;
    for (int i=1, u, v, w, f; i <= m; i++) {
        cin >> u >> v >> w >> f; flows.PB(f);
        adj[u].PB({v, w, f}); adj[v].PB({u, w, f});
    }
    int bf = 0, bc = 1;
    for (int f : flows) {
        int cc = dij(f);
        if (cc == -1) continue;
        if (f*bc > bf*cc) {
            bf = f; bc = cc;
        }
    }
    cout << 1000000*bf/bc << endl;
}