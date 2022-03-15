//https://dmoj.ca/problem/ccc15j4
//CCC '15 J4 - Wait Time

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String [] args){
		Scanner in = new Scanner(System.in);
		int [] r = new int [101];
		int [] s = new int [101];
		int [] w = new int [101];
		int N = in.nextInt(), t = 0;
		for(int i=0; i<N; i++){
			String event=in.next(); int x = in.nextInt();
			if(event.equals("W")) t += x-1;
			else{
				t ++ ;
				if(event.equals("R")){r[x] = t; s[x] = -1; }
				else{ s[x] = t; w[x] += s[x] - r[x]; }
			}
		}
		for(int i=1; i<=100; i++)
			if(r[i] != 0){
				if(s[i] == -1) System.out.println(i + " " + (-1));
				else System.out.println(i + " " + w[i]);
			}
	}
}
