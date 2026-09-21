#define buzzer 8

void setup() {
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (digitalRead(3)== LOW) {
    tone(buzzer, 262, 500);
    delay(250);
    tone(buzzer, 262, 500);
    delay(250);
    tone(buzzer, 262, 500);
    delay(500);
  }
  if (analogRead(A0)>200) {
    tone(buzzer, 262, 500);
    delay(500);
    tone(buzzer, 294, 500);
    delay(500);
    tone(buzzer, 330, 500);
    delay(500);
    tone(buzzer, 349, 500);
    delay(500);
    tone(buzzer, 392, 500);
    delay(500);
    tone(buzzer, 440, 500);
    delay(500);
    tone(buzzer, 494, 500);
    delay(500);
    tone(buzzer, 523, 500);
    delay(1000);
  }
}
