//https://dmoj.ca/problem/ccc01j1
//CCC '01 J1 - Dressing Up

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int h = Integer.parseInt(s.next());
        for (int i = 0; i < Math.ceil(h/2)+1; i++) {
            System.out.println("*".repeat(2*(i+1)-1) + " ".repeat(2 * (h-(i*2)-1)) + "*" .repeat(2*(i+1)-1));
        }
        for (int i = (h/2)-1; i < Math.ceil(h/2)+1; i--) {
            if (i < 0) {
                break;
            }
            System.out.println("*".repeat(2*(i+1)-1) + " ".repeat(2 * (h-(i*2)-1)) + "*" .repeat(2*(i+1)-1));
        }
        s.close();
    }
}
