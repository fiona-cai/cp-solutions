//https://dmoj.ca/problem/usaco19decbronze1
//USACO 2019 December Bronze P1 - Cow Gymnastics

import java.util.*;
import java.io.*;

public class Main 
{
    public static void main(String[] args) throws IOException
    {
        readInput();
    }
    
    private static void readInput()
    {
        // System.setIn(new FileInputStream(new File(".\\test_data\\j5\\j5.8.in")));
        Scanner scan = new Scanner(System.in);
        int k = scan.nextInt();
        int n = scan.nextInt();
        boolean[][] rankings = new boolean[20][20];
        int[] classRanking = new int[n];
        for (int k2 =0; k2 < k; k2 ++) {
            for (int n2 =0; n2 < n; n2++) {
                classRanking[n2] = scan.nextInt();
            }
            for (int i =0; i <n; i++) {
                for (int j=i+1; j < n; j++) {
                    rankings[classRanking[j]-1][classRanking[i]-1] = true;
                }
            }
        }
        int cnt = 0;
        for (int i =0; i <n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (!rankings[j][i] || !rankings[i][j]) {
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
        
    }

            
}
