// include the library code
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// pinout for flame detector (IR)

int FlamePin = 8;  // This is for input pin
int Flame = HIGH;  // HIGH when FLAME Exposed
unsigned long lastFlameDetectTime;
int flameAlarmTime = 500;
boolean flalarm = false;

// pinout for sound detector

int soundDetectedPin = 7; // Use Pin 10 as our Input
int soundDetectedVal = HIGH; // This is where we record our Sound Measurement
boolean bAlarm = false;
unsigned long lastSoundDetectTime;
int soundAlarmTime = 500;

int sound_count = 0;


// pinout for LCD

LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE); 

// End of pinout

// Start void setup

void setup() {

  // void setup for flame detector
  pinMode(FlamePin, INPUT);

  // void setup for sound detector
  pinMode (soundDetectedPin, INPUT) ;

  // void setup for LCD screen
  lcd.begin(16,2);   // iInit the LCD for 16 chars 2 lines
  lcd.backlight();   // Turn on the backligt (try lcd.noBaklight() to turn it off)
  lcd.setCursor(0,0); //First line
  lcd.print("Welcome");
  lcd.setCursor(0,1); //Second line
  lcd.print("*Smart house portal*"); 


  // Declare serial port
  
  Serial.begin(9600);
  
}

void loop() {
  Flame = digitalRead(FlamePin);
  
  if (Flame == HIGH)
  {
    lastFlameDetectTime = millis();
    if (!flalarm){
    Serial.println("Flame on");
    lcd.clear();
    lcd.print("Flame on");
    flalarm = true;
  }
  else
  {
    if( (millis()-lastFlameDetectTime) > flameAlarmTime  &&  flalarm){
    Serial.println("No flame");
    lcd.clear();
    lcd.print("no flame");
    flalarm = false;
    }
   }
}
  
// code for sound detection..


   soundDetectedVal = digitalRead (soundDetectedPin) ; // read the sound alarm time
  
  if (soundDetectedVal == LOW) // If we hear a sound
  {
  
    lastSoundDetectTime = millis(); // record the time of the sound alarm
    // The following is so you don't scroll on the output screen
    if (!bAlarm){
      Serial.println("LOUD, LOUD");
      lcd.clear();
      lcd.print("LOUD");
      bAlarm = true;

      sound_count = sound_count + 1;
      Serial.println(sound_count);

      if (sound_count == 10){
        Serial.println("ALERT");
        sound_count = 0;
        
      }
    }
  }
  else
  {
    if( (millis()-lastSoundDetectTime) > soundAlarmTime  &&  bAlarm){
      Serial.println("quiet");
      lcd.clear();
      lcd.print("QUIET");
      bAlarm = false;
    }
  }
}

