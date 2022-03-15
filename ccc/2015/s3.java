//https://dmoj.ca/problem/ccc15s3
//CCC '15 S3 - Gates

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
        int g = scan.nextInt();
        int p = scan.nextInt();
        TreeSet<Integer> gates = new TreeSet<>();
        ArrayList<Integer> maxGates = new ArrayList<>();
        //ArrayList<Integer> maxGates2 = new ArrayList<>();
        for (int i =1; i <p+1; i++) {
            maxGates.add(scan.nextInt());
            gates.add(i);
        }
        int dockedcnt = 0;
        for (int i = 0; i < p; i ++) {
            //boolean docked = false;
            int maxGate = maxGates.get(i);
            
            Integer gate = gates.floor(maxGate);
            
            if (gate == null) {
                break;
            }
            gates.remove(gate);
            dockedcnt ++;
    }       
        System.out.println(dockedcnt);  
    }
}
