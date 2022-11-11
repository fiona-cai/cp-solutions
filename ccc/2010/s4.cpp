//https://dmoj.ca/problem/ccc10s4
//CCC '10 S4 - Animal Farm

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e9;


int m;
map<pair<int, pi>, pi> costs;  //edge-> pen#1, pen#2
map<int, pair<int, pi>> indexToKey;
int parent[101];
bool connected[101][101];

int findRoot(int v) {
    if (parent[v] != v) {
        parent[v] = findRoot(parent[v]);
    }
    return parent[v];
}
void init() {
    for (int i =0; i<=m; i++) {
        for (int j =0; j <=m; j++) {
            connected[i][j] = false;
        }
    }
    for (int i =0; i<= m; i++) {parent[i] = i;}
}

int main() {
    cin >> m;
    init();
    for (int i =0; i <m; i++) {
        int e;
        cin >> e;
        vi edges;
        for (int j =0; j< e; j++) {
            int ei;
            cin >> ei;
            edges.PB(ei);
        }for (int j =0; j <e; j++) {
            int c;
            cin >> c;
            pair<int, pi>  currEdge;
            currEdge.F = c;
            currEdge.S.F = edges[j];
            if (j == e-1) {
                currEdge.S.S = edges[0];
            } else {
                currEdge.S.S = edges[j+1];
            }
            int w1 = min(currEdge.S.S,currEdge.S.F);
            int w = max(currEdge.S.S,currEdge.S.F);
            currEdge.S.F = w1;
            currEdge.S.S = w;
            if (costs.count(currEdge) > 0) {
                costs[currEdge].S = i+1;
            } else {
                costs[currEdge].F = i+1;
                costs[currEdge].S = 0;
            }
        }

    }
    //  costs.erase({7, {1,2}});
    int i=-1, highestIndex = 0;
    for (pair<pair<int,pi>, pi> e : costs) {
        //cout << e.F.a << endl;
        i++;
        indexToKey[i] = e.F;
        highestIndex = i;
        //cout << e.F.F << " " << e.F.S.F << " " << e.F.S.S << " " << e.S.F << " " << e.S.S  << endl;
    }
    int edgecnt=0, ans = 0;
    for (int i =0; edgecnt != m-1 && i <= highestIndex; i++) {
        pair<int, pi> oldEdge = indexToKey[i];
        int cost = oldEdge.F;
        pi edge = costs[oldEdge];
        if (edge.S == 0) continue;
        if (connected[edge.F][edge.S]) continue;
        int fx = findRoot(edge.F), fy = findRoot(edge.S);
        if (fx != fy) {
            //cout << cost << " " << edge.F << " " << edge.S << " "<< endl;
            edgecnt ++;
            parent[fx] = fy;
            ans += cost;
            connected[edge.F][edge.S] = true;
        }
    }
    //cout << edgecnt << " ------" << endl;
    init();

    int edgecnt2=0, ans2 = 0;
    for (int i =0; edgecnt2 != m && i <= highestIndex; i++) {
        pair<int, pi> oldEdge = indexToKey[i];
        int cost = oldEdge.F;
        pi edge = costs[oldEdge];
        //cout << cost << " " << edge.F << " " << edge.S << " " << endl;
        int fx = findRoot(edge.F), fy = findRoot(edge.S);
        if (connected[edge.F][edge.S]) continue;
        if (fx != fy) {
            //cout << "used" << endl;
            edgecnt2 ++;
            parent[fx] = fy;
            ans2 += cost;
            connected[edge.F][edge.S] = true;
        }
    }
    //cout << ans << " " << ans2 << endl;
    if (edgecnt == m-1) {
        cout << min(ans, ans2) << "\n";
    } else if (edgecnt2 == m) {
        cout << ans2 << "\n";
    }




}