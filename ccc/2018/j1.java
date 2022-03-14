//https://dmoj.ca/problem/ccc18j1
//CCC '18 J1 - Telemarketer or not?

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		int c = s.nextInt();
		int d = s.nextInt();
		if (((a == 8 || a == 9) && b == c && (d == 8 || d == 9))) {
			System.out.println("ignore");
		}else {
			System.out.println("answer");
		}
		s.close();
    }
}
