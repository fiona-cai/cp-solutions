//https://dmoj.ca/problem/ccc18j3
//CCC '18 J3 - Are we there yet?

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
		List<Integer> cities = new ArrayList<Integer>(5);
		cities.add(0);
		int d1 = s.nextInt();
		cities.add(d1);
		int d2 = s.nextInt();
		cities.add(d1+d2);
		int d3 = s.nextInt();
		cities.add(d1+d2+d3);
		int d4 = s.nextInt();
		cities.add(d1+d2+d3+d4);
		for (int i=0; i<5; i++) {
			for (int city:cities) {
				int out = Math.abs(cities.get(i)-city);
				System.out.print(out+" ");
			}
			System.out.println("");
		}
    	
		s.close();
    }
}
