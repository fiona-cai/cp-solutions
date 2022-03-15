//https://dmoj.ca/problem/ccc17j2
//CCC '17 J2 - Shifty Sum

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int k = s.nextInt();
		int out = 0;
		for (int i = 0; i <= k; i++) {
			out += n*1*Math.pow(10,i);
		}
    	System.out.println(out);
		s.close();
    }
}
