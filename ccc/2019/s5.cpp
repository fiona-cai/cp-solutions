#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const ll inf = 1e9;

int n, k;
vector<vi> triangle;


void solve(int k) {
    if (k == 1) return;
    int s = (2*k + 2)/3;
    if (k == 2) {
        s = 1;
    }
    solve(s);
    for (int i =0; i <= triangle.size() - k;i++) {
        for (int j = 0; j <= i; j++) {
            triangle[i][j] = max(triangle[i][j], max(triangle[i+k-s][j], triangle[i+k-s][j+k-s]));
        }
    }
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n >> k;
    triangle.resize(n);
    for (int i =0; i < n ;i++) {
        for (int j = 0; j <= i; j++) {
            int x;
            cin >> x;
            triangle[i].PB(x);
        }
    }
    solve(k);
    ll sum = 0;
    for (int i =0; i <= n-k ;i++) {
        for (int j = 0; j <= i; j++) {
            sum += triangle[i][j];
        }
    }
    cout << sum << "\n";
}
