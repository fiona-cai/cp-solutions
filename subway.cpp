//https://dmoj.ca/problem/subway
//Subway Routes

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 4e5 + 2;

int n, d =0, dis[maxn], cnt[maxn]; ll tot;
vi adj[maxn];

void dfs(int u, int pre) {
    dis[u] = 0; cnt[u] = 1;
    for (int v : adj[u]) {
        if (v != pre) {
            dfs(v, u);
            if (dis[v]+dis[u] +1 > d) {
                d = dis[v] +dis[u] +1;
                tot = 1LL*cnt[u]*cnt[v];
            } else if (dis[v] + dis[u] +1 == d) {
                d = dis[v] + dis[u] + 1;
                tot += 1LL*cnt[u]*cnt[v];
            }

            if (dis[v] +1 > dis[u]) {
                dis[u] = dis[v] + 1; cnt[u] = cnt[v];
            } else if (dis[v] + 1 == dis[u]) {
                cnt[u] += cnt[v];
            }
        }
    }
}

int main() {
    cin >> n;
    for (int i=0; i <n-1; i++) {
        int x, y; cin >> x >> y;
        adj[x].PB(y); adj[y].PB(x);
    }
    dfs(1, -1);
    cout << tot << "\n";
}
