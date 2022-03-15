//https://dmoj.ca/problem/usaco19decbronze2
//USACO 2019 December Bronze P2 - Where Am I?

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
        String n2 = scan.nextLine();
        int n = Integer.parseInt(n2);
        String s = scan.nextLine();
        
        for (int i=1; i < n+1; i++) {
            boolean work = true;
            for (int start=0; start<n-i+1;start++) {
                String seq = s.substring(start, start+i);
                String otherFarms = s.substring(start+1);
                if (otherFarms.contains(seq)) {
                    work = false;
                    break;
                }
            }
            if (work) {
                System.out.println(i);
                break;
            }
        }
        
    }

            
}
