//https://dmoj.ca/problem/ccc15j5
//CCC '15 J5 - π-day

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e9;

int n,k;
map<pair<pi, int>, int> answers;

int work(int x, int p, int last) {
    if (x == 0 && p == 0) return 1;
    if (p <= 0) return 0;
    if (answers.find({{x,p}, last}) != answers.end()) return answers[{{x,p},last}];
    int ans = 0;
    int mx = x/p;
    for (int i =last; i<=mx; i++) {
        ans += work(x-i, p-1, i);
    }
    answers[{{x,p},last}] = ans;
    return ans;
}

int main() {
    cin >> n >> k;
    cout << work(n, k, 1) << endl;
}
