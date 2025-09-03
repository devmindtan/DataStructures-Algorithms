// recursion
// function fib(n) {
//   if (n <= 1) {
//     return n;
//   }
//   return fib(n - 1) + fib(n - 2);
// }
// console.log(fib(10));

// dynamic programing (top-down)
// function fib(n) {
//   let dp = [];
//   if (n <= 1) {
//     return n;
//   }
//   if (dp[n] != undefined) {
//     return dp[n];
//   }
//   dp[n] = fib(n - 1) + fib(n - 2);
//   return dp[n];
// }
// console.log(fib(6));

// dynamic programing (bottom-up)
// function fib(n) {
//   if (n <= 1) {
//     return n;
//   }
//   let dp = [0, 1];
//   for (let i = 2; i <= n; i++) {
//     dp[i] = fib(i - 1) + fib(i - 2);
//   }
//   return dp[n];
// }
// console.log(fib(6));

// dynamic programing (space optimization)
// function fib(n) {
//   if (n <= 1) return n;
//   let a = 0,
//     b = 1;
//   for (let i = 2; i <= n; i++) {
//     let c = a + b;
//     a = b;
//     b = c;
//   }
//   return b;
// }
// console.log(fib(6));
