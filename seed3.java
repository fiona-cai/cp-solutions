//https://dmoj.ca/problem/seed3
//The Cosmic Era P3 - Battle Positions

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int station = in.nextInt();
        int min = in.nextInt();
        int wave = in.nextInt();
        int dif[] = new int[station+2];
        for(int i = 1; i<=wave;i++){
            int L = in.nextInt();
            int R = in.nextInt();
            int v = in.nextInt();
            dif[L] += v; dif[R+1]-=v;
        }
        int ans = 0;
        for(int i=1; i<= station; i++){
            dif[i]+= dif[i-1];
            if(dif[i]<min)ans++;
        }
        System.out.println(ans);
    }
}
