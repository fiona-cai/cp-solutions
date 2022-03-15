//https://dmoj.ca/problem/usaco19febs2
//USACO 2019 February Silver P2 - Painting the Barn

#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <numeric>
#include <cmath>
#include <queue>
#include <vector>

using namespace std;
const long long inf = 1e18;
const int maxh = 1e6 + 2;

int n, k, dp[1005][1005], ans = 0;

int main() {
    cin >> n >> k;
    for (int i=0; i <n; i++) {
        int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        dp[x1][y1] ++; dp[x2][y2] ++;
        dp[x1][y2] --; dp[x2][y1] --;
    }
    for (int i=0; i <1001; i++) {
        for (int j =0; j <1001; j++) {
            if(i > 0) dp[i][j] += dp[i-1][j];
            if(j > 0) dp[i][j] += dp[i][j-1];
            if(i > 0&& j > 0) dp[i][j] -= dp[i-1][j-1];
            if(dp[i][j] == k) ans++;
        }
    }
    cout << ans << "\n";
}
