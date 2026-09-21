#include <Servo.h>;
Servo my_servo;
String mess;

void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

void loop() {
  if (Serial.available()>0){
    mess = Serial.readString();
    if (mess=="open"){
      my_servo.attach(8);
      my_servo.write(0);
      tone(7,200,50);
      delay(100);
      tone(7,400,50);
      delay(100);
      tone(7,500,50);
      delay(100);
      my_servo.detach();
      digitalWrite(9, LOW);
      Serial.println("key open");
    }
    if (mess=="lock"){
      my_servo.attach(8);
      my_servo.write(180);
      tone(7,200,50);
      delay(100);
      tone(7,200,50);
      delay(100);
      tone(7,200,50);
      delay(100);
      my_servo.detach();
      digitalWrite(9, HIGH);
      Serial.println("key closed");
    }
  }
  
  
  my_servo.write(0);
  delay(2000);
  my_servo.write(90);
  delay(2000);
  my_servo.write(180);
  delay(2000);
}
