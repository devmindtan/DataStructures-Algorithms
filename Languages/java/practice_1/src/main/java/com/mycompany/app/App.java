package com.mycompany.app;

public class App {

    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // @formatter:off
        int[] primeList = new int[] {
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 74
        };
        // @formatter:on
        for (int i = 0; i < primeList.length; i++) {
            System.out.printf("%b ", isPrime(primeList[i]));
        }
    }
}
