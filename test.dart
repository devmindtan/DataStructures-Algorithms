bool isPalindrome(String s) {
  String validate = s.toLowerCase().replaceAll(" ", "");
  String reversed = "";
  for (var i = validate.length - 1; i >= 0; i--) {
    reversed += validate[i];
  }
  if (reversed == validate) {
    return true;
  }
  return false; // tạm thời
}

void main() {
  print(isPalindrome("Race car")); // true
  print(isPalindrome("hello")); // false
  print(isPalindrome("Able was I ere I saw Elba")); // true
}
