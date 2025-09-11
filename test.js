const grid = [
  [1, 2, 5, 5],
  [5, 3, 10, 5],
  [3, 5, 3, 1],
  [2, 3, 4, 2],
  [0, 0, 5, 0],
];

function maxPathSumWithPath(grid) {
  const m = grid.length;
  const n = grid[0].length;

  const dp = Array.from({ length: m }, () => Array(n).fill(0));

  // lưu hướng đi: "U" = từ trên xuống, "L" = từ trái sang
  const parent = Array.from({ length: m }, () => Array(n).fill(null));

  dp[0][0] = grid[0][0];

  // hàng đầu tiên
  for (let j = 1; j < n; j++) {
    dp[0][j] = dp[0][j - 1] + grid[0][j];
    parent[0][j] = "L"; // đi từ trái sang
  }

  // cột đầu tiên
  for (let i = 1; i < m; i++) {
    dp[i][0] = dp[i - 1][0] + grid[i][0];
    parent[i][0] = "U"; // đi từ trên xuống
  }

  // các ô còn lại
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (dp[i - 1][j] > dp[i][j - 1]) {
        dp[i][j] = grid[i][j] + dp[i - 1][j];
        parent[i][j] = "U"; // đến từ trên
      } else {
        dp[i][j] = grid[i][j] + dp[i][j - 1];
        parent[i][j] = "L"; // đến từ trái
      }
    }
  }

  // truy ngược đường đi
  let path = [];
  let i = m - 1;
  let j = n - 1;
  while (i !== null && j !== null) {
    path.push([i, j]); // lưu tọa độ
    if (parent[i][j] === "U") {
      i--;
    } else if (parent[i][j] === "L") {
      j--;
    } else {
      break;
    }
  }
  path.reverse(); // đảo ngược để đi từ (0,0) → (m-1,n-1)

  return { maxSum: dp[m - 1][n - 1], path };
}

const result = maxPathSumWithPath(grid);
console.log("Max Sum:", result.maxSum);
console.log("Path (coordinates):", result.path);
console.log(
  "Path (values):",
  result.path.map(([i, j]) => grid[i][j])
);
