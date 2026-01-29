#include <cmath>
#include <cstdlib>
#include <ios>
#include <iostream>
#include <pthread.h>
#include <string>
#include <random>
#include <iterator>
#include <limits>
#include <chrono>

using namespace std::chrono;
using namespace std;

void bai1(){
    string user_name = "Nguyen Van A";
    int user_age = 18;
    string email_address = "nguyenvana@example.com";

    cout << user_name << endl;
    cout << user_age << endl;
    cout << email_address << endl;
}

void bai2(){
    int number = 5;
    number = 10;
    cout << number << endl;
}

void bai3(){
    int a = 5;
    int b = 10;
    int temp = a;
    a = b;
    b = temp;
    cout << "a: " << a << endl;
    cout << "b: " << b << endl;
}

int bai4(int a, int b){
    return a * b;
}

int bai5(int n){
    return n * 2;
}

double bai6(double c){
    return (c * 9/5) + 32;
}

void bai7(int dai, int rong, int co_so, int cao, int canh){
    double s_hcn = dai * rong;
    double s_tg = (co_so * cao) / 2;
    double s_hv = canh * canh;

    cout << "Dien tich hcn: " << s_hcn << endl;
    cout << "Dien tich htg: " << s_tg << endl;
    cout << "Dien tich hv: " << s_hv << endl;
}
void bai8(int n){
    string result = "";
    if (n % 2 == 0){
        result = "Chan";
    }
    else{result = "Le";}
    cout << result << endl;
}

string bai9(int n){
    if(n > 90){
      return "Xuat sac";
    }else if(n > 80){
        return "Gioi";
    }else if(n > 70){
        return "Kha";
    }else if(n > 60){
        return "Trung binh";
    }else{
        return "Yeu";
    }
}

string bai10(int thang){
    // C1
    // string arr[12] = {"Thang mot", "Thang hai", "Thang ba", "Thang tu", "Thang nam", "Thang sau", "Thang bay", "Thang tam", "Thang chin", "Thang muoi", "Thang muoi mot", "Thang muoi hai"};
    // return arr[thang-1];

    // C2
    switch (thang) {
        case 1:
            return "Thang mot";
            break;
        case 2:
            return "Thang hai";
            break;
        case 3:
            return "Thang ba";
            break;
        case 4:
            return "Thang tu";
            break;
        case 5:
            return "Thang nam";
            break;
        case 6:
            return "Thang sau";
            break;
        case 7:
            return "Thang bay";
            break;
        case 8:
            return "Thang tam";
            break;
        case 9:
            return "Thang chin";
            break;
        case 10:
            return "Thang muoi";
            break;
        case 11:
            return "Thang muoi mot";
            break;
        case 12:
            return "Thang muoi hai";
            break;
        default:
            return "Khong co thang: " + to_string(thang);
            break;
    }
}

string bai11(char op, int a, int b){
    switch (op) {
        case '+':
            return to_string(a * b);
            break;
        case '-':
            return to_string(a - b);
            break;
        case '*':
            return to_string(a * b);
            break;
        case '/':
            return (b != 0) ? to_string(a / b): "Khong the chia cho 0";
            break;
        default:
            return "Nhap sai!!!";
            break;
    }
}

void bai12(int start, int end){
    for (int i = start; i <= end; i++) {
        cout << i << " ";
    }
    cout << endl;
}

string bai13(string a){
    int len = a.length();
    string reverse = "";
    for (int i = len - 1; i >= 0; i--) {
        reverse += a[i];
    }
    return reverse;
}

int bai14(int n){
    int factorial = 1;
    for(int i = 1; i <= n; i++){
        factorial *= i;
    }
    return factorial;
}

int bai15(int a, int b){
    // Neu 1 trong 2 = 0 thi tra va ve 1 trong 2
    // Tim min cua a va b
    // Neu ca 2 chia het cho cac so tu min - 1 thi la uoc so chung lon nhat
    // Neu khong co thi uoc so nho nhat la 1
    // C1
    // if(a == 0 || b == 0){
    //     return a + b;
    // }
    // int min = (a < b) ? a : b;
    // for (int i = min; i >= 1; i--){
    //     if(a % i == 0 && b % i == 0){
    //         return i;
    //     }
    // }
    // return 1;

    // C2: Eculid
    while (b != 0){
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

void bai16(){
    for (int i = 1; i <= 10; i ++){
        for (int j = 2; j <= 9; j++){
            cout << j << " * " << i << " = " << i * j << "\t";
        }
        cout << endl;
    }
}

void nhap_mang(int a[], int n){
    for (int i = 0; i < n; i++){
        cout << "Nhap phan tu thu [" << i+1 << "]: ";
        cin >> a[i];
    }
}
void xuat_mang(int a[], int n){
    for (int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}

void tao_mang_ngau_nhien(int a[], int n){
    static random_device rd;
    static mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100);
    for (int i = 0; i < n; i++){
        a[i] = dis(gen);
    }
}

void xuat_so_chan(int a[], int n){
    cout << "---CAC SO CHAN CO TRONG MANG---" << endl;
    for (int i = 0; i < n; i++){
        if(a[i] % 2 == 0){
            cout << a[i] << " ";
        }
    }
    cout << endl;
}

int tim_so_chan_lon_nhat(int a[], int n){
    int max = 0;
    cout << "---SO CHAN LON NHAT CO TRONG MANG---" << endl;
    for (int i = 0; i < n; i++){
        if(a[i] % 2 == 0){
            if(max < a[i]){
                return a[i];
            }
        }
    }
    return 0;
}

bool kiem_tra_so_chinh_phuong(int n){
    if (n < 0) return false;
    int check = round(sqrt(n));
    return (check * check  == n);
}
void tong_cac_so_chinh_phuong(int a[], int n){
    cout << "---TONG CAC SO CHINH PHUONG CO TRONG MANG---" << endl;
    int total = 0;
    for (int i = 0; i < n; i++){
        total += kiem_tra_so_chinh_phuong(a[i])? a[i] : 0;
    }
    cout << total << endl;
}

bool kiem_tra_so_nguyen_to(int n){
    if(n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

void xuat_cac_so_nguyen_to(int a[], int n){
    cout << "---CAC SO NGUYEN TO CO TRONG MANG---" << endl;
    for (int i = 0; i < n; i++){
        if (kiem_tra_so_nguyen_to(a[i])){
            cout << a[i] << " ";
        }
    }
    cout << endl;
}

void xap_xep_tang_giam(int a[], int n){
    cout << "---SAP XEP TANG DAN---" << endl;
    for (int i = 0; i < n - 1; i++){
        for (int j = 0; j < n - i - 1; j++){
            if(a[j] > a[j + 1]){
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    xuat_mang(a, n);
    cout << "---SAP XEP GIAM DAN---" << endl;
    for (int i = 0; i < n - 1; i++){
        for (int j = 0; j < n - i - 1; j++){
            if(a[j] < a[j + 1]){
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
    xuat_mang(a, n);
}

string bai_them_1(double dtb){
    if(dtb >= 8){
        return "Gioi";
    }else if(dtb >= 6.5){
        return "Kha";
    }else if(dtb >= 5){
        return "Trung binh";
    }else{
        return "Yeu";
    }
}
int bai_them_2_1(int a,int b,int c){
    int arr[] = {a, b, c};
    int max = arr[0];
    for (int i = 0; i < size(arr); i++){
        if(max < arr[i]){
            max = arr[i];
        }
    }
    return max;
}
int bai_them_2_2(int a,int b,int c, int d){
    int arr[] = {a, b, c, d};
    int max = arr[0];
    for (int i = 0; i < size(arr); i++){
        if(max < arr[i]){
            max = arr[i];
        }
    }
    return max;
}
void bai_them_2_3(int n){
    int tong_chan = 0;
    int tong_le = 0;
    for (int i = 0; i <= n; i++){
        if(n % 2 == 0){
            if(i % 2 == 0){
                tong_chan += i;
            }
        }else{
            if(i % 2 != 0){
                tong_le += i;
            }
        }
    }
    cout << "Tong chan: " << tong_chan << endl << "Tong le: " << tong_le << endl;
}

void bai_them_3(int n){
    // a. S = 1 + 2 + … + n
    // b. S = 1^2 + 2^2 + … + n^2
    // c. S = 1 + 1/2 + … + 1/n
    // d. S = 1*2*…*n = n!
    // e. S = 1! + 2! + … + n!
    int a = 0;
    int b = 0;
    long long d = 1;
    int e = 0;
    double c = 0;
    int fac = 1;
    for (int i = 1; i <= n; i++){
        a += i;
        b += (i*i);
        c += (1.0/i);
        d *= i;
        fac *= i;
        e += fac;
    }
    cout << "a: " << a << endl << "b: " << b << endl << "c: " << c << endl << "d: " << d << endl << "e: " << e << endl;
}

bool bai_them_4(int n){
    if(n < 2){
        return false;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

void bai_them_5(){
    int n;
    while (true) {
        cout << "Nhap n: ";
        cin >> n;
        if(cin.fail()){
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            continue;
        }
        for (int i = 0; i < n; i++){
            if(bai_them_4(i)){
                cout << i << " ";
            }
        }
        cout << endl;
        break;
    }
}

int bai_them_6(int n){
    if(n == 0) return 0;
    return (n % 10) + bai_them_6(n / 10);
}
int bai_them_7(int n){
    int total = 0;
    for (int i = 0; i < n; i++){
        if(bai_them_4(i)){
            cout << total << " + ";
            total += i;
            cout << i << " = " << total << endl;
        }
    }
    return total;
}


bool kiem_tra_nam_nhuan(int nam){
    if(nam % 400 == 0 || (nam % 100 != 0 && nam % 4 == 0)){
        return true;
    }
    return false;
}
int chuyen_doi_ngay(int ngay, int thang, int nam){
    static int t[] = { 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 };
    if (thang < 3) nam -= 1;

    int res = (nam + nam/4 - nam/100 + nam/400 + t[thang-1] + ngay) % 7;
    return res;
}
void bai_them_8(int ngay, int thang, int nam){
    if(kiem_tra_nam_nhuan(nam)){
        cout << nam << " la nam nhuan" << endl;
    }else{
        cout << nam << " khong phai la nam nhuan" << endl;
    }
    string day_of_week[] = {"Chu nhat", "Thu hai", "Thu ba", "Thu tu", "Thu nam", "Thu sau", "Thu bay"};
    cout << ngay << "/" << thang << "/" << nam << " la " <<day_of_week[chuyen_doi_ngay(ngay, thang, nam)] << endl;
    // cout << "Ngay ke tiep cua: " << ngay << "/" << thang << "/" << nam << " la " << ngay+1 << "/" << thang << "/" << nam << endl;
}
int test(int n){
    // 123
    // int i = 0;
    // int total = 0;
    // int len = to_string(n).length();
    // while (i < len){
    //     int last = n % 10;

    //     if(last % 2 != 0){
    //         total += last;
    //     }
    //     n = n / 10;

    //     i++;
    // }
    // return total;
    int total = 0;
    for (int i = 1; i <= n; i+=2){
        total += i;

    }
    return total;
}

int main(){
    // bai1();
    // bai2();
    // bai3();
    // cout << bai4(10, 5) << endl;
    // cout << bai5(10) << endl;
    // cout << bai6(25) << endl;
    // bai7(2, 5, 10, 4, 5);
    // bai8(5);
    // bai8(6);
    // cout << bai9(85) << endl;
    // cout << bai9(55) << endl;
    // cout << bai10(11) << endl;
    // cout << bai11('+', 5, 3) << endl;
    // cout << bai11('/', 10, 0) << endl;
    // cout << bai11('x', 10, 15) << endl;
    // bai12(1,12);
    // cout << bai13("hello") << endl;
    // cout << bai13("world") << endl;
    // cout << bai13("JavaScript") << endl;
    // cout << bai14(5) << endl;
    // cout << bai15(60, 48) << endl; //12
    // cout << bai15(12, 15) << endl; //3
    // cout << bai15(100, 80) << endl; //20
    // cout << bai15(7, 13) << endl; //1
    // bai16();

    // int n;
    // cout << "Nhap chieu dai mang: ";
    // cin >> n;
    // int a[n];
    // cout << "---MANG LA---" << endl;
    // // nhap_mang(a, n);
    // tao_mang_ngau_nhien(a,n);
    // xuat_mang(a, n);
    // xuat_so_chan(a, n);
    // cout << tim_so_chan_lon_nhat(a, n) << endl;
    // tong_cac_so_chinh_phuong(a, n);
    // xuat_cac_so_nguyen_to(a, n);
    // xap_xep_tang_giam(a, n);


    // cout << bai_them_1(9) << endl;
    // cout << bai_them_2_1(1,2,0) << endl;
    // cout << bai_them_2_2(1,2,-1, 10) << endl;
    // bai_them_2_3(10);
    // bai_them_3(10);
    // bai_them_5();
    // cout << test(5) << endl;
    // cout << bai_them_6(1234) << endl;
    // cout << bai_them_7(10) << endl;
    bai_them_8(26, 3, 2026);
    return 0;
}
