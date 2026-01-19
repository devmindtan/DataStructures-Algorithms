package com.mycompany.app;

public class App {

    public static void main(String[] args) {
        // NhanVienFullTime nvfTime = new NhanVienFullTime("NV01", "TAN", 100, 2);
        // NhanVienPartTime nvpTime = new NhanVienPartTime(
        //     "NV01",
        //     "TAN",
        //     0,
        //     40,
        //     20
        // );

        // nvfTime.hienThiThongTin();
        // System.out.println("----------------------");
        // nvpTime.hienThiThongTin();
        QuanLyNhanVien qlNhanVien = new QuanLyNhanVien();
        qlNhanVien.themNhanVien();

        // qlNhanVien.timTheoMa("nv01");

        System.out.println("1. Tang dan\n2. Giam dan");
        qlNhanVien.sapXepTheoLuong(2);
        qlNhanVien.timLuongCaoNhat();

        for (NhanVien nv : qlNhanVien.timTheoTen("t")) {
            nv.hienThiThongTin();
            System.out.println("");
        }
    }
}
