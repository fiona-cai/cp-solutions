//USACO 2017 January Contest, Silver Problem 2. Hoof, Paper, Scissors
//http://www.usaco.org/index.php?page=viewproblem2&cpid=691 

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 1e5 + 2;

int n, hcnt, pcnt, scnt, prefmax[maxn], suffmax[maxn], ans;
string s;
int mymax() {
    return max(hcnt, max(pcnt, scnt));
}

int main(){
    freopen("hps.in", "r", stdin);
    freopen("hps.out", "w", stdout);
    cin >> n;
    for (int i =0; i <n; i++) {
        char c; cin >> c; s.PB(c);
        if (c == 'H') hcnt ++;
        else if (c == 'P') pcnt ++;
        else scnt ++;
        prefmax[i] = mymax();
    }
    reverse(s.begin(), s.end());
    hcnt = pcnt = scnt = 0;
    for (int i =0; i <n; i++) {
        char c = s[i];
        if (c == 'H') hcnt ++;
        else if (c == 'P') pcnt ++;
        else scnt ++;
        suffmax[i] = mymax();
    }
    for (int i =0; i <n; i++) {
        ans = max(ans, prefmax[i]+suffmax[n-i-1]);
    }
    cout << min(n, ans) << "\n";
}
