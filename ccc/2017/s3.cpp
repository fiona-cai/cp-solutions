//https://dmoj.ca/problem/ccc17s3
//CCC '17 S3 - Nailed It!

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
const int inf = 1e6 + 1;

int n;
vi lengths; bool used[inf];
map<int,int> freq, freq2;

int main() {
    cin >> n;
    for (int i =0; i <n; i++) {
        int l; cin >> l;
        if (!used[l]) lengths.PB(l);
        used[l] = true;
        freq[l] ++;
    }
    for (int i =0; i< lengths.size(); i++) {
        int v1 = lengths[i];
        if (freq[v1] > 1) {
            freq2[2*v1] += freq[v1]/2;
        }
        for (int j = i+1; j < lengths.size(); j++) {
            int v2 = lengths[j];
            int currfreq = min(freq[v1], freq[v2]);
            freq2[v1+v2] += currfreq;
        }
    }
    int mx = 0, mxf = 0;
    for (auto e : freq2) {
        int h = e.F, f = e.S;
        if (f > mx) {
            mx = f;
            mxf = 1;
        } else if (f == mx) {
            mxf ++;
        }
    }
    printf("%d %d\n", mx, mxf);

}
