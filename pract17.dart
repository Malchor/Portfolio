import 'dart:io';
import 'dart:math';

void main() {
  isValidEmail();
  checkExpenses();
  List<double> temps = [15.5, 18.2, 20.1, 16.8];
  double diff = weatherDifference(temps);
  print("Temperature difference: $diff");

  Set<String> foods = {"Milkshake", "Bread", "Almond milk", "Eggs"};
  Set<String> filteredFoods = removeMilk(foods);
  print("Foods without milk: $filteredFoods");
}

void isValidEmail() {
  print("What is your email?: ");
  String? input1 = stdin.readLineSync();

  if (input1 == null || input1.isEmpty) {
    print("Invalid input.");
    return;
  }

  int amount = numberTally(input1);
  for (int i = 1; i <= amount; i++) {
    stdout.write('Number ');
  }
  print("\nYour email is valid and is $input1");
}

int numberTally(String email) {
  int count = 0;
  for (int i = 0; i < email.length; i++) {
    if (RegExp(r'\d').hasMatch(email[i])) {
      count++;
    }
  }
  return count;
}

void checkExpenses() {
  print("Enter your expenditures here then write 'done' when complete:");
  int entryAmount = 0;
  double totalAmount = 0;
  int maximumAmount = 100;

  String? input;
  while (true) {
    stdout.write("Expenditure $entryAmount: ");
    input = stdin.readLineSync();

    if (input == null || input.toLowerCase() == "done") {
      break;
    }

    double? value = double.tryParse(input);
    if (value == null) {
      print("Invalid number, try again.");
      continue;
    }
    totalAmount += value;
    entryAmount++;
  }
  String message = totalAmount < maximumAmount ? 'Within budget' : 'Over budget';
  print("$message. Total: $totalAmount");
}

double weatherDifference(List<double> temperatures) {
  if (temperatures.isEmpty) {
    return 0.0;
  }
  return (temperatures.first - temperatures.last).abs();
}


Set<String> removeMilk(Set<String> foodSet) {
  return foodSet
      .where((food) => !food.toLowerCase().contains('milk'))
      .toSet();
}


void capMarks(){

}


void priceRise (){

}

