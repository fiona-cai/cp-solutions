//https://dmoj.ca/problem/ccc12j1
//CCC '12 J1 - Speed fines are not fine!

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int dif = b - a;
        String strS = "You are speeding and your fine is $";

        if(dif <= 0){
            System.out.println("Congratulations, you are within the speed limit!"); 
        }else if(dif >= 1 && dif <= 20){
            System.out.println(strS + 100 + ".");

        }else if(dif >= 21 && dif <= 30){
            System.out.println(strS + 270 + ".");

        }else if(dif >= 31){
            System.out.println(strS + 500 + ".");

        }

    }
}
