//https://dmoj.ca/problem/ccc22s3
//CCC '22 S3 - Good Samples

#include <bits/stdc++.h>
using namespace std;
#define int long long
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1e6 + 5;

int n, m, k;
vi ans;

signed main() {
    cin >> n >> m >> k;
    if (k < n) {cout << -1 << "\n"; return 0;}
    k -= n;
    ans.PB(1);
    for (int i=2; i <=m && k >= i-1; i++) {
        //cout << i << " " << k << endl;
        ans.PB(i); k -= i-1;
    }
    int x = ans.size();
    for (int i =x; i < n; i++) {
        if (k == 0) ans.PB(ans.back());
        else {
            ans.PB(ans[i-min(k+1, m)]);
            k -= min(k+1, m)-1;
        }
    }
    if (ans.size() != n || k > 0) {cout << -1 << "\n"; return 0;}
    for (int i=0; i <ans.size(); i++) {
        cout << ans[i] << " \n" [i==ans.size()-1];
    }
    return 0;

}
