//USACO 2017 January Contest, Silver Problem 1. Cow Dance Show
//http://www.usaco.org/index.php?page=viewproblem2&cpid=690

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1e4 + 2;

int n, t, cowtime[maxn];

int works(int k) {
    int currTime = 0;
    priority_queue<int, vi, greater<int>> cowsDancing;
    for (int i =0; i <n; i++) {
        if (cowsDancing.size() == k) {currTime = cowsDancing.top(); cowsDancing.pop(); }
        cowsDancing.push(currTime+cowtime[i]);
    }
    while (!cowsDancing.empty()) {
        if (cowsDancing.top() > t) return false;
        cowsDancing.pop();
    }
    return true;
}

int main() {
    freopen("cowdance.in", "r", stdin);
    freopen("cowdance.out", "w", stdout);
    cin >> n >>t;
    for (int i =0; i < n;i++) cin >> cowtime[i];
    int low = 0, high = n+1;
    while (low != high) {
        int mid = (low+high)/2;
        if (works(mid)) high = mid;
        else low = mid+1;
    }
    cout << high << "\n";
}
