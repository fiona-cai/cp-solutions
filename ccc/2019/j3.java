//https://dmoj.ca/problem/ccc19j3
//CCC '19 J3 - Cold Compress

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		for (int i=0; i<n; i++) {
			String msg = s.next();
			char[] chars = (msg + "0").toCharArray();
			char current = chars[0];
			int count = 0;
			for (int j=0; j<chars.length; j++) {
				char c = chars[j];
				if (c == current) {
					count++;
				} else if (chars.length-1 == j) {
					print(count, current, chars, true);
				}else {
					print(count, current, chars, false);
					current = c;
					count = 1;
				}
			}
			System.out.println();
		}
		s.close();
	}
	
	public static void print(int count, char c, char[] chars, boolean t) {
		if (chars[0] == c) {
			System.out.print(count + " " + c + " ");
		} else if (t) {
			System.out.print(count + " " + c);
		} else {
			System.out.print(count + " " + c + " ");
		}
	}
}
