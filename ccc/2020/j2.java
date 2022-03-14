//https://dmoj.ca/problem/ccc18j2
//CCC '18 J2 - Occupy parking

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int out = 0;
		String yes = s.next();
		String tod = s.next();
		for (int i=0; i<n; i++) {
			if (yes.toCharArray()[i] == 'C' && tod.toCharArray()[i] == 'C') {
				out++;
			}
		}
    	System.out.println(out);
		s.close();
    }
}
