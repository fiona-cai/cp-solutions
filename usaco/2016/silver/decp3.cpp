//USACO 2016 December Contest, Silver Problem 3. Moocast
//http://www.usaco.org/index.php?page=viewproblem2&cpid=668

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 205;

struct cow {int x, y, r;};

int n, currans;
cow cows[maxn];
vi adj[maxn];
bitset<maxn> vis;

int dfs(int u) {
   vis[u] = 1;
   currans++;
   for (int v : adj[u]) {
       if (!vis[v]) dfs(v);
   }
}

int main(){
   freopen("moocast.in", "r", stdin);
   freopen("moocast.out", "w", stdout);
   cin >> n;
   for (int i =0; i <n; i++) cin >> cows[i].x >> cows[i].y >> cows[i].r;
   for (int i =0; i <n; i++) {
       for (int j = 0; j <n; j++) {
           int dist = (cows[i].x - cows[j].x)*(cows[i].x - cows[j].x) + (cows[i].y - cows[j].y)*(cows[i].y- cows[j].y);
           if (dist <= cows[i].r*cows[i].r) adj[i].PB(j);
       }
   }
   int ans = 0;
   for (int i =0; i <n; i++) {
       currans = 0;
       vis.reset();
       dfs(i);
       ans = max(currans, ans);
   }
   cout << ans << "\n";
}
