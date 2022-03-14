#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e6+2;

int n, anum, bnum, cnum, ans = 1e9;
int a[inf], b[inf], c[inf];
string s;

void solve(int x[], int y[], int i) {
    int nx = x[n], ny = y[n];
    int notworkx = nx-(x[i] - x[i-nx]), notworky = ny-(y[i-nx] - y[i-nx-ny]);
    int yinx = y[i] - y[i-nx], xiny = x[i-nx] - x[i-nx-ny];
    ans = min(ans, notworkx +notworky- min(yinx,xiny));
}

int main() {
    cin >> s; n = s.size();
    for (int i =1; i <= n; i++) {
        a[i] = a[i-1]; b[i] = b[i-1]; c[i] = c[i-1];
        if (s[i-1] == 'A') a[i] ++;
        else if (s[i-1] == 'B') b[i] ++;
        else c[i] ++;
    }
    anum = a[n], bnum = b[n], cnum = c[n];
    for (int i =1; i <=n; i++) {
        if (i >= anum + bnum) {solve(a,b,i); solve(b,a,i);}
        if (i >= anum + cnum) {solve(a,c,i); solve(c,a,i);}
        if (i >= bnum + cnum) {solve(b,c,i); solve(c,b,i);}
    }
    cout << ans << "\n";

}
