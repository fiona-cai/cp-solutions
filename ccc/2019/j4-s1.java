//https://dmoj.ca/problem/ccc19s1
//CCC '19 S1 - Flipper

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] grid = {1,2,
					  3,4};
		Scanner s = new Scanner(System.in);
		char[] vhs = s.next().toCharArray();
		for (char c:vhs) {
			if (c == 'H') {
				int temp = grid[0];
				grid[0] = grid[2];
				grid[2] = temp;
				temp = grid[1];
				grid[1] = grid[3];
				grid[3] = temp;
			} else {
				int temp = grid[0];
				grid[0] = grid[1];
				grid[1] = temp;
				temp = grid[2];
				grid[2] = grid[3];
				grid[3] = temp;
			}
		}
		System.out.print(grid[0] + " ");
		System.out.println(grid[1]);
		System.out.print(grid[2] + " ");
		System.out.println(grid[3]);
		s.close();
    }
}
