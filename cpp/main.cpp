// c++ project:

#include <iostream>
#include <cstdlib> // for std::rand
#include <ctime> // for std::time

int main() {
  // Base project: Write a working C++ program in a file named main.cpp in your cpp folder. The program should print out the string “Hello World!” followed by a newline.
  std::cout << "Hello World!" << std::endl;

  // Show a working if statement. This if statement is used to determine which of two numbers is greater.
  // No user input, instead random numbers are generated using <ctime>.
  std::srand(std::time(nullptr));

  // Generate two random numbers and print them out
  int a = std::rand();
  int b = std::rand();
  std::cout << "The two numbers are: " << a << " and " << b << std::endl;
  // Uses if statement to figure out which number is greater and prints accordingly.
  if (a > b) {
    std::cout << a << " is greater than " << b << std::endl;
  } else if (a < b) {
    std::cout << b << " is greater than " << a << std::endl;
  } else {
    std::cout << a << " and " << b << " are equal" << std::endl;
  }

  // Show a working for loop. This for loop is used to print the numbers from 1 to 5.
  for (int i = 1; i <= 5; i++) {
    std::cout << i << std::endl;
  }

  // Show a working function. This function, addTen, adds ten to an int.
  // declare the function
  int addTen(int x);
  // print result(s) of diff trials
  std::cout << addTen(5) << std::endl;
  std::cout <<addTen(96) << std::endl;
  std::cout <<addTen(-14) << std::endl;
  return 0;
}

// addTen function defined below: This function takes in an integer and adds 10 to it.
int addTen(int x) {
  return x + 10;
}

// done!