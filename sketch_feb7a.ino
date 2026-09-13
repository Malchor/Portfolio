const byte blue = 3;
const byte red = 5;
const byte green = 6;

void setup() {
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
}

void loop() {
  analogWrite(blue, random(0, 256));
  analogWrite(red, random(0, 256));
  analogWrite(green, random(0, 256));
  delay(500);
}
