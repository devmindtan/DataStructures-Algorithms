package com.mycompany.app;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {

    public static String reverseString(String name) {
        String reverseName = "";
        for (int i = name.length() - 1; i >= 0; i--) {
            reverseName += name.charAt(i);
        }
        return reverseName;
    }

    public static int findFactorial(int n) {
        if (n == 1) {
            return 1;
        }
        return findFactorial(n - 1) * n;
    }

    public static List<Integer> nhapMang() {
        Scanner sc = new Scanner(System.in);

        String line = sc.nextLine();

        Scanner lineScanner = new Scanner(line);
        List<Integer> numbers = new ArrayList<>();

        while (lineScanner.hasNextInt()) {
            numbers.add(lineScanner.nextInt());
        }

        sc.close();
        lineScanner.close();
        return numbers;
    }

    public static void xuatMang(List<Integer> s) {
        System.out.println(s);
    }

    public static void main(String[] args) {
        // String name = "abc";
        // System.out.println(reverseString(name));
        // System.out.println(findFactorial(5));
        xuatMang(nhapMang());
    }
}
