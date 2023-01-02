//USACO 2022 December Contest, Silver Problem 3. Range Reconstruction
//http://usaco.org/index.php?page=viewproblem2&cpid=1256 

/*
Key points:
- Assume 1 .. i works then add i+1
- Only need to check a[i][i+1] to make array
- 2 choices for each element ans[i-1] + a[i][i+1], ans[i-1] - a[i][i+1]
*/

#include <bits/stdc++.h>
using namespace std;
#define int long long
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 300 + 5;

int n, a[maxn][maxn], ans[maxn];

int getMax(int i, int j) {
    int mx = -1e9 -5;
    for (; i <= j; i++) mx = max(mx, ans[i]);
    return mx;
}
int getMin(int i, int j) {
    int mn = 1e9+5;
    for (; i <= j; i++) mn = min(mn, ans[i]);
    return mn;
}

bool ok(int i) {
    for (int j=1; j < i; j++) {
        int mx = getMax(j, i), mn = getMin(j, i);
        if (mx-mn != a[j][i]) return false;
    }
    return true;
}

void solve() {
    ans[1] = 1;
    assert(ok(1));
    for (int i=2; i <= n; i++) {
        ans[i] = ans[i-1]+a[i-1][i];
        if (!ok(i)) {
            ans[i] = ans[i-1] - a[i-1][i];
            assert(ok(i));
        }
    }
}

signed main() {
    //freopen ("input.txt","r",stdin);
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for (int i=1; i <= n; i++) {
        for (int j=i; j <= n; j++) cin >> a[i][j];
    }
    solve();
    for (int i=1; i <= n; i++) {
        assert(ans[i] <= 1e9);
        cout << ans[i] << " \n" [i==n];
    }
}
