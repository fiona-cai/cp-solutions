//https://dmoj.ca/problem/ccc13s5
//CCC '13 S5 - Factor Solitaire

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
        int c = scan.nextInt();
        double score = changeNum(c);
        System.out.println((int) score);
    }
    private static double changeNum(double c) {
        double score = 0;
        while (c != 1) {
            double[] nums = getNums(c);
            double a = nums[0];
            double b = nums[1];
            c = nums[2];
            
            score = score + b;
        }
        return score;
    }
    
    private static double[] getNums(double c) {
        double maxE = 0;
        double[] nums = new double[3];
        for (int pair1 = 1; pair1 < c; pair1 ++) {
            double[] pair = {c-pair1, pair1};
            double[] e = checkEfficiency(pair, c);
            if (e[0] > maxE) {
                maxE = e[0];
                nums[0] = pair[1];
                nums[1] = e[1];
                nums[2] = pair[0];
            }
        }
        return nums;
    }
    private static double[] checkEfficiency(double[] pair, double c) {
        double newc = pair[0];
        double a = pair[1];

        if (newc % a == 0) {
            double b = newc/a;
            double score = b;
            double efficiency = (double) (c-newc)/(score);
            double[] x = {efficiency, score};
            return x;
        } else {
            double[] x = {0,0};
            return x;
        }
    }
        
}
