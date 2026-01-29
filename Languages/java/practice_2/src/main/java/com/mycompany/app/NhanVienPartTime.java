package com.mycompany.app;

/*
Lớp NhanVienPartTime có thêm:
soGioLam (int) - Số giờ làm
luongTheoGio (double) - Lương theo giờ
Phương thức tinhLuong() = soGioLam * luongTheoGio
Override hienThiThongTin()
*/
public class NhanVienPartTime extends NhanVien implements ILuong {

    private double luongTheoGio;
    private int soGioLam;

    public NhanVienPartTime() {
        super();
    }

    public NhanVienPartTime(
        String maNV,
        String hoTen,
        double luongCoBan,
        double luongTheoGio,
        int soGioLam
    ) {
        super(maNV, hoTen, luongCoBan);
        this.luongTheoGio = luongTheoGio;
        this.soGioLam = soGioLam;
    }

    @Override
    public double tinhLuong() {
        return soGioLam * luongTheoGio;
    }

    @Override
    public void hienThiThongTin() {
        System.out.printf(
            "MANV: %s\nHOTEN:%s\nLUONGTHEOGIO:%.0f\nSOGIOLAM:%d\nTONGLUONG:%.0f\n",
            maNV,
            hoTen,
            luongTheoGio,
            soGioLam,
            tinhLuong()
        );
    }
}
