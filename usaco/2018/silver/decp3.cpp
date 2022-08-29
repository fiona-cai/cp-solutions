//USACO 2018 December Contest, Silver Problem 3. Mooyo Mooyo
//http://www.usaco.org/index.php?page=viewproblem2&cpid=860

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int maxn = 101;

int n, k, grid[maxn][11], vis[maxn][11], col = 10;
vector<pi> adj = {{1,0}, {0, 1}, {-1, 0}, {0, -1}};
vector<pi> c;

void dfs(int i, int j, int color) {
    c.PB({i, j});
    vis[i][j] = true;
    for (auto [nx, ny] : adj) {
        int x = nx+i, y = ny+j;
        if (x >= 0 && x < n && y >= 0 && y < 10 && grid[x][y] == color && !vis[x][y]) dfs(x, y, color);
    }
}

void gravity() {
    int arr2[200][11];
    memset(arr2, 0, sizeof arr2);

    for (int j =0; j <col; j++) {
        int cnt = 0;
        for (int i = n-1; i >=0; i--) {
            if (grid[i][j] == 0) cnt++;
            else arr2[i+cnt][j] = grid[i][j];
        }
    }
    for (int i =0; i <n; i++) {
        for (int j =0; j < col; j++) {
            grid[i][j] = arr2[i][j];
        }
    }
}

int main() {
    freopen("mooyomooyo.in", "r", stdin);
    freopen("mooyomooyo.out", "w", stdout);
    cin >> n >> k;
    for (int i =0; i <n; i++) {
        for (int j =0; j < col; j++) {
            char c; cin >> c;
            grid[i][j] = c - '0';
        }
    }
    bool work = true;
    while (work) {
        work = false;
        memset(vis, false, sizeof vis);
        for (int i=0; i <n; i++) {
            for (int j =0; j < col; j++) {
                c.clear();
                if (!vis[i][j] && grid[i][j] != 0) dfs(i, j, grid[i][j]);
                if (c.size() >= k) {
                    work = true;
                    for (auto [x, y] : c) {
                        grid[x][y] = 0;
                    }
                }
            }
        }
        gravity();
    }

    for (int i=0; i <n; i++) {
        for (int j =0; j < col; j++) {
            cout << grid[i][j];
        }
        cout << endl;
    }
}


