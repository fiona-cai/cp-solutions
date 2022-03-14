//https://dmoj.ca/problem/ccc19j2
//CCC '19 J2 - Time to Decompress

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		int l = s.nextInt();
		for (int i=0; i<l; i++) {
			int n = s.nextInt();
			String c = s.next();
			for (int j=0; j<n; j++) {
				System.out.print(c);
			}
			System.out.println();
		}
		s.close();
    }
}
