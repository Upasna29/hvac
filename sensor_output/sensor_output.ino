#include <SparkFunTSL2561.h>
#include <Wire.h>
//#include <FirebaseArduino.h>

SFE_TSL2561 light;

boolean gain = 0;     // Gain setting, 0 = X1, 1 = X16;
unsigned int ms = 1000;
unsigned char time = 2;

int tempSensePin = A0; //Arduino pin for temperature sensor input
int tempSensorInput; //Stores sensor input
double temperature; //Stores input converted to temperature in degrees
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  light.begin();
  light.setTiming(gain,time,ms);
  light.setPowerUp();

}

void loop() {
  delay(ms);
  // put your main code here, to run repeatedly:
  tempSensorInput = analogRead(A0);
  temperature = (double)tempSensorInput/1024;
  temperature = temperature * 5;
  temperature = temperature - 0.5;               //Subtract the offset
  temperature = temperature * 100;

//  Serial.println(temperature);

  unsigned int data0, data1;

  if (light.getData(data0, data1)){
    double lux;    // Resulting lux value
    boolean good;  // True if neither sensor is saturated

    good = light.getLux(gain,ms,data0,data1,lux);
    Serial.print(temperature);
    Serial.print(' ');
    Serial.println(lux);
  }

}
