function getRow(rowIndex) {
  let result = [1];
  for (let i = 0; i < rowIndex; i++) {
    let row = new Array(i + 2).fill(1); // python là let row = [1] * (i + 2)
    for (let j = 1; j < i + 1; j++) {
      row[j] = result[j - 1] + result[j];
    }
    result = row;
  }
  return result;
}
console.log(getRow(0));
