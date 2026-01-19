package com.mycompany.app;

/*
Lớp NhanVienFullTime có thêm:
heSoLuong (double) - Hệ số lương
Phương thức tinhLuong() = luongCoBan * heSoLuong
Override hienThiThongTin()
*/
public class NhanVienFullTime extends NhanVien implements ILuong {

    protected double heSoLuong;

    public NhanVienFullTime() {
        super();
    }

    public NhanVienFullTime(
        String maNV,
        String hoTen,
        double luongCoBan,
        double heSoLuong
    ) {
        super(maNV, hoTen, luongCoBan);
        this.heSoLuong = heSoLuong;
    }

    @Override
    public double tinhLuong() {
        return luongCoBan * heSoLuong;
    }

    @Override
    public void hienThiThongTin() {
        System.out.printf(
            "MANV: %s\nHOTEN:%s\nLUONGCB:%.0f\nHESOLUONG:%.0f\nTONGLUONG:%.0f\n",
            maNV,
            hoTen,
            luongCoBan,
            heSoLuong,
            tinhLuong()
        );
    }
}
