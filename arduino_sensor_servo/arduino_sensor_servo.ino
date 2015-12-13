#include <Servo.h> 

///// Reset arduino with pi at start of each run

// Variables
// Sensor pins
int sensorPinControl = A0;
int sensorPins[] = {A1, A2, A3, A4};
int arrayLength = 1;

// Sensor values
int controlValue = 0;
int sensorValues[] = {0, 0, 0, 0};
int sensorValuesHistory[4][10] = {{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}};
int arrayPosition = 0;

// Sensor calibration values
int sensorCalibrations[] = {0, 0, 0, 0};
int margin = 2;

// Broken states
boolean isBroken[] = {false, false, false, false};

// Timing of last break in milliseconds
long breakStartTimes[] = {0, 0, 0, 0};

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
int signalPins[] = {4, 5, 6, 7};

// Signal from pi
int piIn = 12;

void setup()
{
  Serial.begin(9600);
  
  // Servos
  servo2.attach(servoPin2);
  servo3.attach(servoPin3);
  
  // Digital output signals
  pinMode(signalPins[0], OUTPUT);
  pinMode(signalPins[1], OUTPUT);
  pinMode(signalPins[2], OUTPUT);
  pinMode(signalPins[3], OUTPUT);
  
  // Digital input signals
//  pinMode(8, INPUT);
//  pinMode(11, INPUT);
  pinMode(piIn, INPUT);
//  pinMode(13, INPUT);
  
}

void loop()
{
  // Read and store values from sensors
  controlValue = analogRead(sensorPinControl);
  // Move to next array position
  arrayPosition = (arrayPosition + 1) % 10;

  for (int i = 0; i < arrayLength; i++)
  {
    sensorValuesHistory[i][arrayPosition] = analogRead(sensorPins[i]);
    sensorValues[i] = analogRead(sensorPins[i]);//average(sensorValuesHistory[i]);
  }

  // Calibrate
  if (millis() < 1000)
  {
    for (int i = 0; i < arrayLength; i++)
    {
      sensorCalibrations[i] = sensorValues[i];
    }
    Serial.print(sensorCalibrations[0]);
    Serial.print( " , ");
    Serial.print(sensorCalibrations[1]);
    Serial.print(" , ");
    Serial.print(sensorCalibrations[2]);
    Serial.print(" , ");
    Serial.println(sensorCalibrations[3]);
  }
  
  // Print sensor values
  Serial.print("control: ");
  Serial.print(controlValue);
  Serial.print(" sensor1: ");
  Serial.print(sensorValues[0]);
  Serial.print(" sensor2: ");
  Serial.print(sensorValues[1]);
  Serial.print(" sensor3: ");
  Serial.print(sensorValues[2]);
  Serial.print(" sensor4: ");
  Serial.println(sensorValues[3]);

  for (int i = 0; i < arrayLength; i++)
  {
    if (sensorValues[i] < sensorCalibrations[i] - margin) // sensor 1 is broken
    {
      if (!isBroken[i] && ((millis() - breakStartTimes[i]) > 1000)) // for the first time && not broken within the last second
      {
        Serial.println("broken1");
        isBroken[i] = true;
        breakStartTimes[i] = millis();
        digitalWrite(signalPins[i], HIGH);
      }
      else if (isBroken[i]) // is already broken
      {
        if ((millis() - breakStartTimes[i]) < 500) // if it has been broken, send a signal for half a second
        {
          digitalWrite(signalPins[i], HIGH); // send a high output signal
        }
      }
    }
    else // the sensor is not broken
    {
      isBroken[i] = false;
      // If more than 1 second has passed since the sensor has been broken
      // So the the output signal if HIGH for 0.5 seconds
      if ((millis() - breakStartTimes[i]) > 500) 
      {
        digitalWrite(signalPins[i], LOW); // Write low
      }
    }
  }
  
  // Move servos
  if (digitalRead(piIn == HIGH))
  {
    servoPos2 += servoDir2;
    servo2.write(servoPos2);
    servoPos3 += servoDir3;
    servo3.write(servoPos3);
    if ((servoPos2 > 180) || (servoPos2 < 0))
    {
      servoDir2 *= -1;
    }
    if ((servoPos3 > 180) || (servoPos3 < 0))
    {
      servoDir3 *= -1;
    }
  }

  // read in broken
//  if (digitalRead(8) == HIGH )//|| digitalRead(11) == HIGH || digitalRead(12) == HIGH || digitalRead(13) == HIGH)
//  {
//    Serial.println("BROKEN !!!!!!!!!!!!!!!!!!!!!!!");
//  }

}

int average(int array[])
{
  int counter = 0;
  int total = 0;
  for (int i = 0; i < sizeof(array); i++)
  {
    total += array[i];
    counter++;
  }
  return total / counter;
}
