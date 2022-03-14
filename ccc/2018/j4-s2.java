//https://dmoj.ca/problem/ccc18s2
//CCC '18 S2 - Sunflowers

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int a[][] = new int[n][n];
		boolean tf = false;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				a[i][j] = s.nextInt();
			}
		}
		while (tf == false) {
			for (int i=1; i<n; i++) {
				if (a[i-1][0] > a[i][0]){
		            ninety(a, n);
		            break;
		        } else {
		        	for (int j=0; j<n - 1; j++) {
				        if (a[i][j] > a[i][j + 1]) {
				            ninety(a, n);
				            break;
				        } else {
				        	tf = true;
				    	}
				    }
		        }
				
			}
		}
		for (int[] e1:a) {
			for (int e: e1) {
				if (e!=e1[0]) {
					System.out.print(" ");
				}
				System.out.print(e);
			}
			System.out.println("");
		}
		s.close();
	}
	static void ninety(int a[][], int n) {
		for (int i = 0; i < n / 2; i++) {
	        for (int j = i; j < n - i - 1; j++) {
	            int temp = a[i][j];
	            a[i][j] = a[n - 1 - j][i];
	            a[n - 1 - j][i] = a[n - 1 - i][n - 1 - j];
	            a[n - 1 - i][n - 1 - j] = a[j][n - 1 - i];
	            a[j][n - 1 - i] = temp;
	        }
	    }
	}
}
