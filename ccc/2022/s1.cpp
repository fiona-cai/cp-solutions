#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1e5 + 5;

int n;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    int ans = 0;
    for (int x = 0; 4*x <= n; x++) {
        int val = n - 4*x;
        if (val % 5 == 0) ans ++;
    }
    cout << ans << "\n";
}
