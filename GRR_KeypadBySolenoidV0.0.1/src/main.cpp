#include <Arduino.h>

//Defines
#define solenoid7 2//pin1 in KiCAD
#define solenoid8 4//pin2 in KiCAD
#define solenoid3 3//pin3 in KiCAD
#define solenoidPound 5//pin4 in KiCAD
#define delayAfterHigh 100
#define delayAfterLow 1000

//setup
int soleArr[] = {solenoid7, solenoid3, solenoid7, solenoid3, solenoid8, solenoidPound};
void setup() {
    pinMode(solenoid3, OUTPUT);
    pinMode(solenoid7, OUTPUT);
    pinMode(solenoid8, OUTPUT);
    pinMode(solenoidPound, OUTPUT);
}

void loop() {
    for (unsigned int i=0; i<(sizeof(soleArr)/4 - 1); i++) {
        digitalWrite(soleArr[i], HIGH);
        delay(delayAfterHigh);
        digitalWrite(soleArr[i], LOW);
        delay(delayAfterLow);
        delay(delayAfterHigh);
    }
}

