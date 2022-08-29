//https://dmoj.ca/problem/ccc05s2
//CCC '05 S2 - Mouse Move

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		int c = s.nextInt();
		int r = s.nextInt();
		int a = s.nextInt();
		int b = s.nextInt();
		int x = 0;
		int y = 0;
		while (!(a == 0 && b == 0)) {
		    x += a;
		    if (x < 0) {
		    	x = 0;
		    }else if (x > c) {
		    	x = c;
		    }
		    System.out.print(x + " ");
		    y += b;
		    if (y < 0) {
		    	y = 0;
		    } else if (y > r) {
		    	y = r;
			}
		    System.out.println(y);
		    a = s.nextInt();
		    b = s.nextInt();
		}
		s.close();
    }
}
