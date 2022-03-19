//CCC '12 S5 - Mouse Journey
//https://dmoj.ca/problem/ccc12s5

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 30;

int r,c, k, dp[maxn][maxn];

int solve(int x, int y) {
    if (x == 1 && y == 1) return 1;
    if (dp[x][y] != -1) return dp[x][y];
    int ans = 0;
    if (x-1 >= 0) ans += solve(x-1, y);
    if (y-1 >=0) ans += solve(x, y-1);
    dp[x][y] = ans;
    return ans;
}

int main() {
    cin >> r >> c >> k;
    memset(dp, -1, sizeof dp);
    while (k--) {
        int x, y; cin >> x>> y;
        dp[x][y] = 0;
    }

    cout << solve(r, c) << "\n";
}
