import 'dart:io';
import 'dart:math';

void main() {
  // print('My name is Bob!');
  // sayName();
  // askForConversionEuroToPound();
  // fahrenheitToCelsius();
  //areaOfCircle();
  circleInfo();
  displayBurgerOrder();
}

void sayName() {
  print(
    'My name is Bob!\nMy ID is 1234567\nMy email address is 1234567@email.co.uk',
  );
}

void askForConversionEuroToPound() {
  print("What is the amount in euros?: ");
  String? input = stdin.readLineSync();
  double conversion = double.parse(input!);
  double converted = conversion * 0.86;
  print("You have $converted GBP");
}

void fahrenheitToCelsius() {
  print("What is the temperature in farenheit?: ");
  String? input = stdin.readLineSync();
  int conversion = int.parse(input!);
  double converted = (conversion - 32) * 5 / 9;
  print("It is $converted degrees celsius");
}

void areaOfCircle() {
  print("what is the radius of your circle in cm?: ");
  String? input = stdin.readLineSync();
  double radius = double.parse(input!);
  num area = pow(radius, 2) * pi;
  print("The area of your circle is $area cm^2");
}

double areaOfCircle2(double radius) {
  return pi * pow(radius, 2);
}

double circumferenceOfCircle(double radius) {
  return 2 * pi * radius;
}

void circleInfo() {
  print("What is the radius of your circle in cm?: ");
  String? input = stdin.readLineSync();
  double radius = double.parse(input!);
  double area = areaOfCircle2(radius);
  double circumference = circumferenceOfCircle(radius);
  print("The area of your circle is $area cm^2");
  print("The circumference of your circle is $circumference cm");
}

void displayBurgerOrder() {
  print("what is your burger order?: ");
  String? input1 = stdin.readLineSync();
  print("what is the price per burger ?: ");
  String? input2 = stdin.readLineSync();
  int amount = int.parse(input1!);
  double priceper = double.parse(input2!);
  for (int i = 1; i <= amount; i++) {
    stdout.write('🍔');
  }
  double total = priceper * amount;
  print("\norder total is \$$total");
}

//void howManyBurgers(){
//  print("How much do you have to spend on burgers?: ");
//  String? input = stdin.readLineSync();
//  double
//}
