import 'dart:io';
import 'dart:math';
String timeofday = "";
double guessingnum = 0;

void main(){
 //customisedGreeting();
 //gcd();
 //guessinggame();
 //print(generatePassword(14));
 print(generatePassword());
}

void customisedGreeting() {
  for (int i = 0; i < 3; i++){
    print("What is the current time of day?: ");
    String? input = stdin.readLineSync();
    int time = int.parse(input!);
    double converted = time / 100;
    if (converted > 6 && converted < 12){
      timeofday = "morning";
    } else if (converted > 12 && converted < 17){
      timeofday = "afternoon";
    } else{
      timeofday = "evening";
    }
    print("Have a great $timeofday!");
  }
}

// void gcd() {
//   for (int i = 0; i < 3; i++) {
//     print("What is a?: ");
//     String? input1 = stdin.readLineSync();
//     int variablea = int.parse(input1!);
//     print("What is b?: ");
//     String? input2 = stdin.readLineSync();
//     int variableb = int.parse(input2!);
//     if (variablea == variableb){
//       print(variablea);
//     } else if (variablea > variableb){
//       double biga = variableb + (variablea - variableb);
//       print(biga);
//     } else{
//       double smalla = variablea + (variableb - variablea);
//       print(smalla);
//     }
//   }
// }

// ctrl+/ is //

void gcd() {
  for (int i = 0; i < 3; i++) {
    print("What is a?: ");
    int a = int.parse(stdin.readLineSync()!);

    print("What is b?: ");
    int b = int.parse(stdin.readLineSync()!);

    int result = findGCD(a, b);
    print("GCD is: $result");
  }
}

int findGCD(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

//skipped question 9 for now

void guessinggame() {
  final random = Random();
  double randnum = random.nextInt(100) + 1;
  if (guessingnum != randnum){
    print("what is the number?:");
    int guessingnum = int.parse(stdin.readLineSync()!);
    if (guessingnum > randnum){
      print("you guessed $guessingnum which was wrong! (lower)");
    } else{
      print("you guessed $guessingnum which was wrong! (higher)");
    }
  } else{
    print("yes the number was $randnum!");
  }
}

bool isPrime(int n) {
  if (n <= 1) {
    return false;
  }

  for (int i = 2; i <= n ~/ i; i++) {
    if (n % i == 0) {
      return false;
    }
  }

  return true;
}


String generatePassword([int length = 8]) {
  if (length < 8) {
    length = 8;
  }

  const String letters =
      'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const String numbers = '0123456789';
  const String symbols = '!@#\$%^&*()-_=+[]{}<>?/';

  const String allChars = letters + numbers + symbols;

  final random = Random.secure();
  final password = StringBuffer();

  for (int i = 0; i < length; i++) {
    int index = random.nextInt(allChars.length);
    password.write(allChars[index]);
  }

  return password.toString();
}

