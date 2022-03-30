//https://dmoj.ca/problem/ccc07j3
//CCC '07 J3 - Deal or No Deal Calculator

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int[] amounts = {100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000};
		int n = s.nextInt();
		for (int i = 0; i < n; i++) {
			int a = s.nextInt();
			amounts[a - 1] = 0;
		}
		int num = s.nextInt();
		int sum = 0;
		int counter = 10;

		for (int i = 0; i < amounts.length; i++) {
			sum += amounts[i];
			if (amounts[i] == 0) {
				counter--;
			}
		}

		num *= counter;
		if (num >= sum) {
			System.out.println("deal");
		} else {
			System.out.println("no deal");
		}
		s.close();
	}
}
