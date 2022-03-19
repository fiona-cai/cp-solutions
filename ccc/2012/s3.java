//CCC '12 S3 - Absolutely Acidic
//https://dmoj.ca/problem/ccc12s3

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
        int n = scan.nextInt();
        HashMap<Integer, Integer> readings = new HashMap<>();
        for (int i = 0; i < n; i ++) {
            int r = scan.nextInt();
            if (readings.containsKey(r)) {
                readings.replace(r, readings.get(r) + 1);
            }
            else {
                readings.put(r, 1);
            }
        }
        int diff = 0;
        int maxRead = 0;
        int maxFreq = Integer.MIN_VALUE;
        int maxRead2 = 0;
        int maxFreq2 = Integer.MIN_VALUE;
        for (int reading : readings.keySet()) {
            int freq = readings.get(reading);
            if (freq > maxFreq) {
                maxFreq2 = maxFreq;
                maxRead2 = maxRead;
                maxFreq = freq;
                maxRead = reading;
                diff = Math.abs(maxRead - maxRead2);
                
            } else if (freq > maxFreq2) {
                maxFreq2 = freq;
                maxRead2 = reading;
                diff = Math.abs(maxRead - maxRead2);
            } else if (freq == maxFreq2) {
                int diff2 = Math.abs(maxRead - reading);
                if (diff2 > diff) {
                    maxFreq2 = freq;
                    maxRead2 = reading;
                    diff = diff2;
                }
            }
        }
        System.out.println(Math.abs(maxRead2 - maxRead));
    }
}
