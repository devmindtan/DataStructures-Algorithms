package com.mycompany.app;

/*
Tạo lớp QuanLyNhanVien chứa danh sách nhân viên (ArrayList<NhanVien>).
Thêm các phương thức:
void themNhanVien(NhanVien nv);
void hienThiTatCa();
NhanVien timTheoMa(String maNV);
double tinhTongLuong();

Bài 5: Sắp xếp và tìm kiếm nhân viên
Cập nhật lớp QuanLyNhanVien để thêm các chức năng:
1. Sắp xếp danh sách nhân viên theo lương giảm dần.
o Viết phương thức void sapXepTheoLuong();
2. Tìm kiếm nhân viên có lương cao nhất.
o Viết phương thức NhanVien timLuongCaoNhat();
3. Tìm kiếm nhân viên theo tên (gần đúng).
o Viết phương thức List<NhanVien> timTheoTen(String ten);
o Kiểm tra nếu hoTen chứa chuỗi ten nhập vào.
*/

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class QuanLyNhanVien {

    List<NhanVien> listNV = new ArrayList<NhanVien>();
    Scanner sc = new Scanner(System.in);

    public void themNhanVien() {
        System.out.print("Nhap so luong nhan vien can them: ");
        int n = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < n; i++) {
            System.out.print("Nhap ma: ");
            String maNV = sc.nextLine();
            System.out.print("Nhap ten: ");
            String hoTen = sc.nextLine();
            System.out.print("Nhap luong co ban: ");
            double luongCoBan = Double.parseDouble(sc.nextLine());
            NhanVien nv = new NhanVien(maNV, hoTen, luongCoBan);
            listNV.add(nv);
            System.out.println("");
        }
    }

    public void hienThiTatCa(String choice) {
        String upper = choice.toUpperCase();
        System.out.printf("\t--------DANH SACH NHAN VIEN %s --------\n", upper);
        int count = 1;
        for (NhanVien nv : listNV) {
            System.out.println("STT: " + count);
            nv.hienThiThongTin();
            count += 1;
            System.out.println("");
        }
        System.out.println(
            "Tong luong phai tra cho tat ca nhan vien: " + tinhTongLuong()
        );
    }

    public double tinhTongLuong() {
        double tongLuong = 0;
        for (NhanVien nv : listNV) {
            tongLuong += nv.luongCoBan;
        }
        return tongLuong;
    }

    public void timTheoMa(String maNV) {
        for (NhanVien nv : listNV) {
            if (nv.getMaNV().equals(maNV)) {
                System.out.printf(
                    "Tim thay ma nhan vien '%s' trong danh sach: \n",
                    maNV
                );
                nv.hienThiThongTin();
                break;
            } else {
                System.out.printf(
                    "Khong tim thay ma nhan vien '%s' trong danh sach\n",
                    maNV
                );
            }
        }
    }

    public void sapXepTheoLuong(int choice) {
        int n = listNV.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (
                    choice == 1 &&
                    (listNV.get(j).getLuongCb() < listNV.get(i).getLuongCb())
                ) {
                    NhanVien tmp = listNV.get(i);
                    listNV.set(i, listNV.get(j));
                    listNV.set(j, tmp);
                } else if (
                    choice == 2 &&
                    (listNV.get(j).getLuongCb() > listNV.get(i).getLuongCb())
                ) {
                    NhanVien tmp = listNV.get(i);
                    listNV.set(i, listNV.get(j));
                    listNV.set(j, tmp);
                }
            }
        }
        if (choice == 1) {
            hienThiTatCa("tang dan");
        } else if (choice == 2) {
            hienThiTatCa("giam dan");
        }
    }

    public void timLuongCaoNhat() {
        int n = listNV.size();
        double max = listNV.get(0).getLuongCb();
        for (int i = 0; i < n; i++) {
            if (listNV.get(i).getLuongCb() > max) {
                max = listNV.get(i).getLuongCb();
            }
        }
        System.out.println("Nhan vien co luong cao nhat la: ");
        for (NhanVien nv : listNV) {
            if (nv.getLuongCb() == max) {
                nv.hienThiThongTin();
            }
        }
    }

    public List<NhanVien> timTheoTen(String ten) {
        List<NhanVien> found = new ArrayList<NhanVien>();
        for (NhanVien nv : listNV) {
            int point = 0;
            for (
                int i = 0;
                i < ten.length() && i < nv.getHoTen().length();
                i++
            ) {
                if (
                    Character.toLowerCase(nv.getHoTen().charAt(i)) ==
                    Character.toLowerCase(ten.charAt(i))
                ) {
                    point += 1;
                } else {
                    break;
                }
            }
            if (point > 0) {
                found.add(nv);
            }
        }
        System.out.printf("Danh sach nhan vien co ten '%s' la: \n", ten);
        return found;
    }
}
