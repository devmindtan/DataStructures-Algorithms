package com.mycompany.app;

/**
 * Câu 1: Viết một lớp NhanVien với các thuộc tính:
 maNV (String) - Mã nhân viên
 hoTen (String) - Họ và tên
 luongCoBan (double) - Lương cơ bản
 hienThiThongTin() - Phương thức in thông tin nhân viên
 Viết constructor, getter, setter.
 */
public class NhanVien {

    protected String maNV;
    protected String hoTen;
    protected double luongCoBan;

    public NhanVien() {}

    public NhanVien(String maNV, String hoTen, double luongCoBan) {
        this.maNV = maNV;
        this.hoTen = hoTen;
        this.luongCoBan = luongCoBan;
    }

    public String getMaNV() {
        return maNV;
    }

    public void setMaNV(String maNV) {
        this.maNV = maNV;
    }

    public String getHoTen() {
        return hoTen;
    }

    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public double getLuongCb() {
        return luongCoBan;
    }

    public void setLuongCb(double luongCoBan) {
        this.luongCoBan = luongCoBan;
    }

    public void hienThiThongTin() {
        System.out.printf(
            "MANV: %s\nHOTEN: %s\nLUONGCB: %.0f\n",
            maNV,
            hoTen,
            luongCoBan
        );
    }
}
