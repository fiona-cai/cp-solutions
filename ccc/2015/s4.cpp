//https://dmoj.ca/problem/ccc15s4
//CCC '15 S4 - Convex Hull

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e9;

struct seaRoute {
    int b, t, h;
};

int k, n,m;
map<int,vector<seaRoute>> adj;
int dist[2001][201];

int main() {
    cin >> k >> n >> m;
    for (int i =0; i<=n; i++) {
        for (int j =0; j <k; j++) {
            dist[i][j] = inf;
        }
    }
    for (int i =0; i<m; i++) {
        int a,b,t,h; cin >> a >> b >> t >>h;
        adj[a].PB({b,t,h});
        adj[b].PB({a,t,h});
    }
    int A, B;
    cin >> A >> B;
    for (int i=0; i<k; i++) dist[A][i] = 0;
    priority_queue<pi> pq;
    pq.push({A, 0});

    while (!pq.empty()) {
        pi curr = pq.top(); pq.pop();
        int v = curr.F;
        for (seaRoute neighbour : adj[v]) {
            int nv = neighbour.b, nt = neighbour.t, nk = neighbour.h;
            for (int j = 0; j < k -nk; j++) {
                if (dist[nv][j+nk] > dist[v][j]+nt) {
                    dist[nv][j+nk] = dist[v][j]+nt;
                    pq.push({nv, -nt});
                }
            }
        }
    }
    int ans = inf;
    for (int i =0; i<k; i++) {
        ans = min(dist[B][i], ans);
    }
    if (ans != inf) cout << ans << "\n";
    else cout << -1 << "\n";
}
