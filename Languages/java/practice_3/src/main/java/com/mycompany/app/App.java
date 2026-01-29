package com.mycompany.app;

import java.util.Scanner;

public class App {

    static Scanner sc = new Scanner(System.in);

    public static boolean checkInput() {
        try {
            System.out.print("Nhap n: ");
            Integer.parseInt(sc.nextLine());
            return true;
        } catch (NumberFormatException e) {
            System.out.println("Nhap sai kieu du lieu");
            return false;
        } catch (Exception e) {
            System.out.println(e);
            return false;
        }
    }

    public static void Cau1() {
        boolean flag = true;
        while (flag) {
            if (checkInput()) {
                System.out.println("Thanh cong");
                flag = false;
            } else {
                System.out.println("Nhap lai!!!");
                checkInput();
            }
        }
    }

    public static void main(String[] args) {
        Cau1();
    }
}
