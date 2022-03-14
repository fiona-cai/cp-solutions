// https://dmoj.ca/problem/ccc19j1
//CCC '19 J1 - Winning Score

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		int a3 = s.nextInt();
		int a2 = s.nextInt();
		int a1 = s.nextInt();
		int b3 = s.nextInt();
		int b2 = s.nextInt();
		int b1 = s.nextInt();
		if ((a3*3 + a2*2 + a1*1) > (b3*3 + b2*2 + b1*1)) {
	    	System.out.println("A");
		} else if ((a3*3 + a2*2 + a1*1) == (b3*3 + b2*2 + b1*1)) {
			System.out.println("T");
		} else {
			System.out.println("B");
		}
		s.close();
    }
}
