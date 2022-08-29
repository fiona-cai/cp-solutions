//https://dmoj.ca/problem/aac4p2
//An Animal Contest 4 P2 - Lavish Lights

#include <bits/stdc++.h>
using namespace std;

#define int long long
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e9;

int n,q;
int psa[200005];

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
int lcm(int a, int b) {
    return (a*b)/gcd(a,b);
}

signed main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n >> q;
    bool flag = false;
    cin >> psa[0];
    for(int i = 1; i < n; i++){
        int a;
        cin >> a;
        if(flag){
            psa[i] = -1;
            continue;
        }
        int ans = lcm(psa[i - 1], a);
        if(ans > 1000000000) {psa[i] = -1, flag = true;}
        else psa[i] = ans;
    }
    for (int i =0; i <q; i++) {
        int t;
        cin >> t;
        if (t == 0) {
            cout << -1 << "\n";
            continue;
        }
        int low = 0, high =n-1, lastworkedmid = -1;
        while (low <= high) {
            int mid = (low+high)/2;
            if(psa[mid] == -1 || t % psa[mid] != 0){
                high = mid - 1;
            } else if(t % psa[mid] == 0){
                low = mid + 1;
                lastworkedmid = mid;
            }
        }
        lastworkedmid += 2;
        if(lastworkedmid == n+1)   cout << "-1" << endl;
        else    cout << lastworkedmid << endl;
    }


}
