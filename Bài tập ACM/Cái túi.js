function knapsack(weights, values, W) {
  const m = weights.length;
  const n = W;
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      console.log(weights[i - 1]);
      if (weights[i - 1] <= j) {
        dp[i][j] = Math.max(
          dp[i - 1][j], // không chọn đồ i
          dp[i - 1][j - weights[i - 1]] + values[i - 1] // chọn đồ i
        );
      } else {
        dp[i][j] = dp[i - 1][j];
      }
    }
  }

  return dp[m][n]; // giá trị lớn nhất
}

// Ví dụ
const weights = [2, 3, 4, 5];
const values = [3, 4, 5, 6];
const W = 5;

// console.log(knapsack(weights, values, W)); // 7 (chọn đồ 1 + đồ 2)

function knapsack01_1D(weights, values, W) {
  const dp = Array(W + 1).fill(0);
  for (let i = 0; i < weights.length; i++) {
    const wi = weights[i],
      vi = values[i];
    for (let w = W; w >= wi; w--) {
      dp[w] = Math.max(dp[w], dp[w - wi] + vi);
    }
  }
  return dp[W];
}
console.log(knapsack01_1D(weights, values, W)); // 7 (chọn đồ 1 + đồ 2)
