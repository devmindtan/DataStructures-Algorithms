function climbStairs(n) {
  if (n <= 2) return n;

  let dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp;
}

/*
  - Xác định điều kiện đề bài
  - Xác định base case
  - Xác định input / output
*/

console.log(climbStairs(3));
