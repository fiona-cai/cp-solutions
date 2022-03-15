//https://dmoj.ca/problem/ccc17s2
//CCC '17 S2 - High Tide, Low Tide

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
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] measurements = new int[n];
        for (int i =0; i < n; i ++) {
            int m = scan.nextInt();
            measurements[i] = m;
        }
        Arrays.sort(measurements);
        int s = (int) Math.ceil(n/2.0);
        int c = 0;
        for (int i = s; i > 0; i--) {
            int low = measurements[i-1];
            System.out.print(low + " ");
            if (i + c < n) {
                int high = measurements[i+c];
                System.out.print(high + " ");
            }
            c ++;
            c ++;
        }
        
    }

            
}
