//USACO 2016 January Contest, Silver Problem 1. Angry Cows
//http://usaco.org/index.php?page=viewproblem2&cpid=594

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 5e4 + 2;

int n, k, c[maxn], vis[maxn];

int works(int mid) {
    int j=k;
    for (int i =0; i < n && j > 0; i++) {
        if (vis[i]) continue;
        j--;
        int pos = c[i]+mid;
        for (int j =0; j < n; j++) {
            if (c[j] >= pos-mid && c[j] <= pos+mid) vis[j] = true;
        }
    }
    for (int i =0; i <n; i++) {
        if (!vis[i]) return false;
    }
    return true;
}


int main(){
    freopen("angry.in", "r", stdin);
    freopen("angry.out", "w", stdout);
    cin >> n >> k;
    if (k >= n) {cout << 0 << "\n"; return 0; }
    for (int i =0; i <n; i++) cin >> c[i];
    sort(c, c+n);
    int low = 0, high = 1e9+2;
    while (low!=high) {
        int mid = (low+high)/2;
        for (int i =0; i <n; i++) vis[i] = false;
        if (works(mid)) {
            high = mid;
        } else {
            low = mid+1;
        }
    }
    cout << low << "\n";
}
