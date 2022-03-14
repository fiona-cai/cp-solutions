#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 207;

int n, t, ans = 0;
set<int> xc;
vi xcoords;
unordered_map<int, set<int>> ycoords;

int main() {
    cin >> n >> t;

    for (int i =0, x, y; i <t; i++) {
        cin >> x >> y;
        xc.insert(x); ycoords[x].insert(y);
    }
    xc.insert(0); xc.insert(n+1);
    for (int c : xc) xcoords.PB(c);

    for (int i=0; i <xcoords.size(); i++) {
        for (int j =i+1; j <xcoords.size(); j++) {
            int maxsize = 0;
            vector<int> top;
            top.push_back(0); top.push_back(n+1);

            for (int k = i+1; k < j; k++) {
                for (auto ycoord : ycoords[xcoords[k]]) top.PB(ycoord);
            }
            sort(top.begin(), top.end());
            for (int k=1; k < top.size(); k++) {
                maxsize = max(maxsize, min(top[k] - top[k-1], xcoords[j] - xcoords[i])-1);
            }
            ans = max(ans, maxsize);
        }
    }
    cout << ans << "\n";
}
