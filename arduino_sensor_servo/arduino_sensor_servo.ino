#include <Servo.h> 

// Variables
// Sensor pins
int sensorPinControl = A0;
int sensorPin1 = A1;
int sensorPin2 = A2;
int sensorPin3 = A3;
int sensorPin4 = A4;

// Sensor values
int controlValue = 0;
int sensorValue1 = 0;
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;

int margin = 0;

// Servo pins
int servoPin2 = 9;
int servoPin3 = 10;

// Servo objects 
// Corresponging to lasers 2 and 3
Servo servo2;
Servo servo3;

// Servo positions
int servoPos2 = 0; 
int servoPos3 = 0; 
int servoDir2 = 1;
int servoDir3 = 1;

// Signal Pins
int signalPin1 = 4;
int signalPin2 = 5;
int signalPin3 = 6;
int signalPin4 = 7;

// Signal Values
boolean signalValue1 = LOW;
boolean signalValue2 = LOW;
boolean signalValue3 = HIGH;
boolean signalValue4 = HIGH;

void setup()
{
  Serial.begin(9600);
  
  // Servos
  servo2.attach(servoPin2);
  servo3.attach(servoPin3);
  
  // Digital output signals
  pinMode(signalPin1, OUTPUT);
  pinMode(signalPin2, OUTPUT);
  pinMode(signalPin3, OUTPUT);
  pinMode(signalPin4, OUTPUT);
  
  // Digital input signals
  pinMode(8, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
}

void loop()
{
  // Read and store values from sensors
  controlValue = analogRead(sensorPinControl);
  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);
  sensorValue3 = analogRead(sensorPin3);
  sensorValue4 = analogRead(sensorPin4);
  
  // Print sensor values
  Serial.print("control: ");
  Serial.print(controlValue);
  Serial.print(" sensor1: ");
  Serial.print(sensorValue1);
  Serial.print(" sensor2: ");
  Serial.print(sensorValue2);
  Serial.print(" sensor3: ");
  Serial.print(sensorValue3);
  Serial.print(" sensor4: ");
  Serial.println(sensorValue4);
  
  // Output the appropriate digital signals
  // true --> high
  // if the sensor value is less than the control, we output HIGH
  digitalWrite(signalPin1, (sensorValue1 < controlValue + margin));
  digitalWrite(signalPin2, (sensorValue2 < controlValue + margin));
  digitalWrite(signalPin3, (sensorValue3 < controlValue + margin));
  digitalWrite(signalPin4, (sensorValue4 < controlValue + margin));
  
  // Move servos
//  servoPos2 += servoDir2;
//  servo2.write(servoPos2);
//  servoPos3 += servoDir3;
//  servo3.write(servoPos3);
//  if ((servoPos2 > 180) || (servoPos2 < 0))
//  {
//    servoDir2 *= -1;
//  }
//  if ((servoPos3 > 180) || (servoPos3 < 0))
//  {
//    servoDir3 *= -1;
//  }

  // read in broken
  if (digitalRead(8) == HIGH || digitalRead(11) == HIGH || digitalRead(12) == HIGH || digitalRead(13) == HIGH)
  {
    Serial.println("BROKEN !!!!!!!!!!!!!!!!!!!!!!!");
  }

  delay(30);
}
