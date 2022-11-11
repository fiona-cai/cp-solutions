//https://dmoj.ca/problem/ccc11s5
//CCC '11 S5 - Switch

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e6 + 5;
const int mx = 25;
const int mxnum = 1 << mx;

int k;
//int steps[mxnum];
bool vis[mxnum];

int work(int s) {
    return s == 0;
}

int main() {
    cin >> k;
    int lights = 0, pw = 1;
    for (int i =0; i <k; i++) {
        char a; cin >> a;
        if (a == '1') lights += pw;
        pw *= 2;
    }

    queue<pair<int,int>> q; q.push({lights,0}); vis[lights] = true;
    while (!q.empty()) {
        auto cc = q.front(); q.pop();
        int c =cc.first;
        int steps=cc.second;
        if (work(c)) {
            printf("%d\n", steps);
            return 0;
        }
        for (int i=0; i <k; i++) {
            if(!((c >> i)&1)) {
                int newlights = c;
                newlights |= (1<<i);
                int cnt = 0;
                for (int j=0; j <k; j++) {
                    if (((newlights >> j)&1)) cnt ++;
                    else {
                        if (cnt >= 4) {
                            for (int a = j-cnt; a <j; a++) {
                                newlights &= ~(1 << a);
                            }
                        }
                        cnt = 0;
                    }
                }
                if (cnt >= 4) {
                    for (int a = k-cnt; a <k; a++) {
                        newlights &= ~(1 << a);
                    }
                }
                if (!vis[newlights]) {
                    //steps[newlights] = steps[c] + 1;
                    q.push({newlights,steps+1});
                    vis[newlights] = true;
                    //cout << newlights << endl;
                }
            }
        }

    }




}