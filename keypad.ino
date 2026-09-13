#include <Keypad.h>
#include <Wire.h> 
//#include <LiquidCrystal_I2C.h>

//LiquidCrystal_I2C lcd(0x27,16,2);

const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
{'1','2','3','*'},
{'4','5','6','/'},
{'7','8','9','-'},
{'C','0','=','+'}
};

byte rowPins[ROWS] = {5, 4, 3, 2};
byte colPins[COLS] = {6, 7, 8, 9};
Keypad kpd = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  //lcd.init();
  //lcd.backlight();
  Serial.begin(9600);
}

void loop() {
  char key = kpd.getKey();
  if (key != NO_KEY){
  //  lcd.setCursor(0,0);
  //  lcd.print(key);
    Serial.println(key);
  }
}
