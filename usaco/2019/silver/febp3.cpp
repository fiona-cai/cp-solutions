//https://dmoj.ca/problem/usaco19febs3
//USACO 2019 February Silver P3 - The Great Revegetation

#include <iostream>
#include <vector>
#include <set>
using namespace std;
typedef long long ll;
const int maxn = 1e5 + 5;

int n, m, vis[maxn], grass[maxn], work = true;
string ans = "";
vector<pair<int, int>> adj[maxn];

bool dfs(int u) {
    vis[u] = true;
    for (auto [v, t] : adj[u]) {
        if (!vis[v]) {
            if (grass[v] == -1) {
                if (t) grass[v] = grass[u];
                else grass[v] = (grass[u] == 1 ? 2 : 1);
            }
            if (!dfs(v))  return false;
        } else {
            if (t && grass[u] != grass[v]) return false;
            else if (!t && grass[u] == grass[v]) return false;
        }
    }
    return true;
}


int main() {
    cin >> n >> m;
    for (int i=1;  i <=n; i++) grass[i] = -1;
    for (int i =0; i <m; i++) {
        char c; int a,b; cin >> c >> a >> b;
        bool same = (c == 'S');
        adj[a].push_back({b, same});
        adj[b].push_back({a, same});
    }
    for (int i=1; i <=n; i++) {
        if (!vis[i]) {
            grass[i] = 1;
            if (dfs(i)) ans =ans + "0";
            else work = false;
        }
    }
    if (work) cout << 1 << ans << "\n";
    else cout <<  0 << "\n";

}
