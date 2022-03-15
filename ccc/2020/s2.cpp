//https://dmoj.ca/problem/ccc20s2
//CCC '20 S2 - Escape Room

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back

bool vis[1001][1001];
map<int, vector<pi>> values;
int n , m;
queue<pi> q;

int main()
{
    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        for (int j =1; j <= m; j++) {
            int val;
            cin >> val;
            values[val].PB({i, j});
            vis[i][j] = false;
        }
    }

    q.push({n, m});
    vis[0][0] = true;
    bool work = false;
    while (!q.empty()) {
        pi curr = q.front(); q.pop();
        if (curr.F == 1 && curr.S == 1) {
            work = true;
        }
        vector<pi> neighbours = values[curr.F * curr.S];
        for (pi neighbour : neighbours) {
            if (vis[neighbour.F][neighbour.S] == false) {
                vis[neighbour.F][neighbour.S] = true;
                q.push(neighbour);
            }
        }

    }
    if (work) {
        cout << "yes" << "\n";
    }
    else {
        cout << "no" << "\n";
    }


}
