const mountain = [
  [2, 8, 9, 5, 8],
  [4, 4, 6, 2, 3],
  [5, 7, 5, 6, 1],
  [3, 2, 5, 4, 8],
];

function findBestWay(mountain) {
  const m = mountain.length;
  const n = mountain[0].length;
  const dp = Array.from({ length: m }, () => Array(n).fill(0));
  const nextStep = Array.from({ length: m }, () => Array(n).fill(-1));

  // dòng cuối
  dp[m - 1] = [...mountain[m - 1]];

  // đi từ dưới lên
  for (let i = m - 2; i >= 0; i--) {
    for (let j = 0; j < n; j++) {
      const left = dp[i + 1][j - 1] ?? Infinity;
      const mid = dp[i + 1][j];
      const right = dp[i + 1][j + 1] ?? Infinity;

      dp[i][j] = mountain[i][j] + Math.min(left, mid, right);

      if (dp[i][j] === mountain[i][j] + left) nextStep[i][j] = j - 1;
      else if (dp[i][j] === mountain[i][j] + mid) nextStep[i][j] = j;
      else nextStep[i][j] = j + 1;
    }
  }

  // tìm giá trị nhỏ nhất hàng đầu
  const minCost = Math.min(...dp[0]);

  // biến để lưu bestPath
  let bestPath = null;
  let bestSum = Infinity;

  for (let j = 0; j < n; j++) {
    if (dp[0][j] === minCost) {
      const path = [];
      let curJ = j;
      let sum = 0;

      for (let i = 0; i < m; i++) {
        sum += mountain[i][curJ]; // tính tổng theo giá trị gốc
        path.push(dp[i][curJ]);
        curJ = nextStep[i][curJ];
        if (curJ === -1) break;
      }

      if (sum < bestSum) {
        bestSum = sum;
        bestPath = path;
      }
    }
  }

  return { mountain, dp, cost: bestSum, path: bestPath, nextStep };
}

console.log(findBestWay(mountain));
