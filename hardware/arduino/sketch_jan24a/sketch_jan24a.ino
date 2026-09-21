#include <IRremote.h> 
int RECIEVE_PIN = 2;
IRrecv irrecv(RECIEVE_PIN);
decode_results results;

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.print("0x");
    Serial.println(results.value, HEX);
    delay(50);
    irrecv.resume();
  }
}
