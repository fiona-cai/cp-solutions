//https://dmoj.ca/problem/ccc11j2
//CCC '11 J2 - Who Has Seen The Wind

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int h = s.nextInt();
		int M = s.nextInt();
		for (int t=1; t<M; t++) {
			int A = (-6*t*t*t*t) + (h*t*t*t) + (2*t*t) + t;
			if (A <= 0) {
				System.out.println("The balloon first touches ground at hour:");
				System.out.println(t);
				System.exit(0);
			}
		}
		System.out.println("The balloon does not touch ground in the given time.");
		s.close();
	}
}
