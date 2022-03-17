//USACO 2016 February Contest, Silver Problem 1. Circular Barn
//http://usaco.org/index.php?page=viewproblem2&cpid=618

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1003;

int n, door[maxn], start, mx;

int work() {
   int ans = 0;
   queue<int> q;
   for (int i =start; i <=n; i++) {
       for (int j =0; j < door[i]; j++) q.push(i);
       if (!q.empty()) {
           int cow = q.front(); q.pop();
           ans += (i-cow)*(i-cow);
       }
   }
   for (int i =1; i < start; i++) {
       for (int j =0; j < door[i]; j++) q.push(i);
       if (!q.empty()) {
           int cow = q.front(); q.pop();
           if (cow > i) ans += (n-cow+i)*(n-cow+i);
           else ans += (i-cow)*(i-cow);
       }
   }
   return ans;

}

int main() {
    freopen("cbarn.in", "r", stdin);
    freopen("cbarn.out", "w", stdout);
    cin >> n;
    for (int i=1; i <=n; i++) cin >> door[i];
    start = -1; mx = 0;
    for (int i=1; i <=n; i++) {
        mx = max(0, mx+door[i]-1);
    }
    for (int i=1; i <=n; i++) {
        if(mx==0){start=i; break;}
        mx = max(0, mx+door[i]-1);
    }
    cout << work() << "\n";
}
