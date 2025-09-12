function longestCommonSubstring(a, b) {
  const m = a.length;
  const n = b.length;

  // dp mảng 2D
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

  let maxLen = 0;
  let endIndex = 0; // vị trí kết thúc trong chuỗi a

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (a[i - 1] === b[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;

        if (dp[i][j] > maxLen) {
          maxLen = dp[i][j];
          endIndex = i; // lưu vị trí kết thúc
        }
      }
    }
  }

  // cắt substring từ a
  return a.substring(endIndex - maxLen, endIndex);
}

const a = "abcdexy";
const b = "xtbayabcdez";

console.log(longestCommonSubstring(a, b));
