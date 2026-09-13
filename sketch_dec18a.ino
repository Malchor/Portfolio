//void setup() {
//  pinMode(11, OUTPUT);
//}

//void loop() {
//  if (digitalRead(6)==HIGH) {
//    digitalWrite(11, HIGH);
//  }
//  else {
//    digitalWrite(11, LOW);
//  }
//}



//void setup() {
//  pinMode(11, OUTPUT);
//}

//void loop() {
//  if (digitalRead(6)==HIGH) {
//    digitalWrite(11, !digitalRead(11));
//  }
//}



void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}
void loop() {
  if (digitalRead(6)==HIGH) {
    digitalWrite(11, !digitalRead(11));
    delay(300);
  }
  if (digitalRead(5)==HIGH) {
    digitalWrite(10, !digitalRead(10));
    delay(300);
  }
  if (digitalRead(4)==HIGH) {
    digitalWrite(9, !digitalRead(9));
    delay(300);
  }
  if (digitalRead(3)==HIGH) {
    digitalWrite(8, !digitalRead(8));
    delay(300);
  }
}



