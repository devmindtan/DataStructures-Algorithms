const a = "abefcda";
const b = "ayekmcdz";

const arrA = a.split("");
const arrB = b.split("");

// Cách 1: For
const minLen = Math.min(arrA.length, arrB.length);
const res_1 = [];

for (let i = 0; i < minLen; i++) {
  for (let j = 0; j < minLen; j++) {
    if (arrA[i] === arrB[j] && !res_1.includes(arrA[i])) {
      res_1.push(arrA[i]);
    }
  }
}
console.log("C1:", res_1.join(""));

// Cách 2: Set
const res_2 = [...new Set(arrA.filter((ch) => arrB.includes(ch)))];

console.log("C2:", res_2.join(""));
