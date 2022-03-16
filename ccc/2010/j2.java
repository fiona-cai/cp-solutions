//https://dmoj.ca/problem/ccc10j2
//CCC '10 J2 - Up and Down

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args){
		Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        int d = input.nextInt();
        int s = input.nextInt();
        int nikkySteps = 0; 
        int nikkysDistance = 0;
        int next = a;
        int sign = 1;
        while(nikkySteps + next < s){
            nikkySteps = nikkySteps + next;
            nikkysDistance = nikkysDistance + sign * next;
            if(sign == 1){
                next = b;
            }
            else{
                next = a;
            }
            sign = sign * -1;
        }
        nikkysDistance = nikkysDistance + sign * (s - nikkySteps);
            int byronSteps = 0; 
            int byronsDistance = 0;
            next = c;
            sign = 1;
            while(byronSteps + next < s){
                byronSteps = byronSteps + next;
                byronsDistance = byronsDistance + sign * next;
                if(sign == 1){
                    next = d;
                }
                else{
                    next = c;
                }
                sign = sign * -1;
            }
            byronsDistance = byronsDistance + sign * (s - byronSteps);
        if(nikkysDistance > byronsDistance)System.out.println("Nikky");
            else if(byronsDistance > nikkysDistance)System.out.println("Byron");
            else System.out.println("Tied");
        input.close();
	}
}
