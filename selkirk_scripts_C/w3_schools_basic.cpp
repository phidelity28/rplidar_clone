
/* include is a header file library that lets uaw work with input and output objest such a cout */

#include <iostream>

/*using namespace std means that we can use names for objects and variables from the standard library.*/
using namespace std;

/*
Line 4: Another thing that always appear in a C++ program, is int main(). This is called a function. 
Any code inside its curly brackets {} will be executed.

Line 5: cout (pronounced "see-out") is an object used together with the insertion operator (<<) to 
output/print text. In our example it will output "Hello World!".

Note: Every C++ statement ends with a semicolon ;.

Note: The body of int main() could also been written as:
int main () { cout << "Hello World! "; return 0; }

Remember: The compiler ignores white spaces. However, multiple lines makes the code more readable.

Line 6: return 0 ends the main function.

Line 7: Do not forget to add the closing curly bracket } to actually end the main function.


*/

int main() {
  cout << "Hello World!";
  return 0;
}

/* basic data types and their declaraiton*/

int myNum = 5;               // Integer (whole number)
float myFloatNum = 5.99;     // Floating point number
double myDoubleNum = 9.98;   // Floating point number
char myLetter = 'D';         // Character
bool myBoolean = true;       // Boolean
string myText = "Hello";     // String