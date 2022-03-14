//https://dmoj.ca/problem/ccc20j4
//CCC '20 J4 - Cyclic Shifts

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		String s1 = s.next();
		String s2 = s.next();
		boolean done = false;
		if (s1.contains(s2)) {
			System.out.println("yes");
			done = true;
		} else {
			for (int i=1; i<s2.length(); i++) {
				String out = s2.substring(i) + s2.substring(0, i);
				if (s1.contains(out) && done == false) {
					System.out.println("yes");
					done = true;
				}
			}
		}
		if (done == false) {
			System.out.println("no");
		}
		s.close();
    }
}
