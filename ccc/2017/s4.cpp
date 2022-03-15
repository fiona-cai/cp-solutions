//https://dmoj.ca/problem/ccc17s4
//CCC '17 S4 - Minimum Cost Flow

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back

struct edge {
    int a, b, w; bool valid;
};
bool mySort (edge elem1, edge elem2) {
    if (elem1.w == elem2.w) {
        return elem1.valid;
    }
    else {
        return (elem1.w < elem2.w);
    }
}

int n,m,d,last;
vector<edge> pipes;
int parent[100001];
int inactive;
int active;

int findRoot(int node) {
    if (parent[node] != node) {
        parent[node] = findRoot(parent[node]);
    }
    return parent[node];
}

int main()
{
    cin >> n >> m >> d;
    for (int i =0; i <= n;i ++) {parent[i] = i;}
    for (int i =0; i <m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        if (i < n-1) {
            pipes.PB({a,b,w, true});
        } else {
            pipes.PB({a,b,w, false});
        }
    }
    sort(pipes.begin(), pipes.end(), mySort);
    int days_needed = 0;
    int nodecnt = 0;
    int last = -1;
    int i = 0;
    while (nodecnt!=n-1) {
        int p1 = pipes[i].a; int p2 = pipes[i].b; int c = pipes[i].w; bool valid = pipes[i].valid;
        int f1 = findRoot(p1); int f2 = findRoot(p2);
        if (f1 != f2) {
            if(!valid) days_needed++;
            nodecnt ++;
            last = i;
            parent[f1] = f2;
            if (valid) active ++;
            else inactive ++;
        }
        i ++ ;
    }
    for (int i =1; i <= n;i ++) parent[i] = i;
    if (pipes[last].valid == 0) {
        int maxcost = pipes[last].w;
        nodecnt = 0;
        last = 0;
        while (last <m) {
            int p1 = pipes[last].a; int p2 = pipes[last].b; int c = pipes[last].w; bool valid = pipes[last].valid;
            int f1 = findRoot(p1); int f2 = findRoot(p2);
            if (f1 != f2) {
                if (c < maxcost || (c == maxcost && valid)) {parent[f1] = f2;}
                else if (valid && c <= d) {days_needed --; break;}
            }
            last ++ ;
        }
    }
    cout << days_needed << "\n";
}
