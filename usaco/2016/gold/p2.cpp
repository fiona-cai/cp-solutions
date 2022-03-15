#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 200001;

int n,m, parent[maxn],order[maxn], open[maxn];
vi adj[maxn];

int findRoot(int u) {
   if (parent[u] != u) {
       parent[u] = findRoot(parent[u]);
   }
   return parent[u];
}
void init() {
   for (int i=1; i <=n; i++) parent[i] = i;
}

int main(){
    freopen("closing.in", "r", stdin);
    freopen("closing.out", "w", stdout);
    cin >> n >> m;
    for (int i =0; i <m; i++) {
       int u, v; cin >> u >> v;
       adj[u].PB(v); adj[v].PB(u);
    }
    init();
    for (int i =0; i <n; i++) {
       cin >> order[i];
    }
    int j = 0, ans=0;
    string a;
    for (int i =n-1; i >=0; i--) {
       int u = order[i], fu = findRoot(u);
       open[u] = true;
       for (int v : adj[u]) {
           if (!open[v]) continue;
           int fv = findRoot(v);
           if (fu != fv) {
               parent[fv] = fu;
               ans++;
           }
       }
       j++;
       if (ans == j-1) a += "SEY";
       else a += "ON";
       if (i > 0) a += "\n";
    }
    reverse(a.begin(), a.end());
    cout << a << "\n";

}
