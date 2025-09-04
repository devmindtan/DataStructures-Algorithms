function countBits(n) {
  let ans = new Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    ans[i] = ans[i >> 1] + (i & 1);
  }
  return ans;
}

console.log(countBits(5));

// Cách giải:
/*
    - dùng biểu thức >> để dịch phải bit 
    - lẻ thì bit cuối = 1, chẵn thì = 0
    => VD: 0 & 1 = 0, 1 & 1 = 1
*/

// console.log(4 >> 1); // Math.floor(n / 2);
