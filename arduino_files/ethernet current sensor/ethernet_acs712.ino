
//python code to read this data 
//lambda url: urllib.request.urlopen(url).read().decode("utf-8").split(" ")[0:-1]

#include <SD.h>
#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = { 
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(10,42, 0, 2);

const int sd_chipSelect = 4;

// Initialize the Ethernet server library
// with the IP address and port you want to use 
// (port 80 is default for HTTP):
EthernetServer server(80);


const int analogIn = A0;
int mVperAmp = 185; // use 100 for 20A Module and 66 for 30A Module
int RawValue= 0;
int ACSoffset = 2500; 
double Voltage = 0;
double Amps = 0;

void setup() {
 // Open serial communications and wait for port to open:
  Serial.begin(9600);

  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());

  // Bring up the SD card  
  if (!SD.begin(sd_chipSelect)) {
    Serial.println("SD card failed, or not present");
    // don't do anything more, infinite loop here until we get reset
    while(1) { }
  }
  Serial.println("SD card initialized.");
}


void loop() {

  RawValue = analogRead(analogIn);
  Voltage = (RawValue / 1024.0) * 5000; // Gets you mV
  Amps = ((Voltage - ACSoffset) / mVperAmp);
   
  File dataFile = SD.open("anyFile.txt", FILE_WRITE);
  if (dataFile) {
    dataFile.print(Amps);
    dataFile.print(" ");
    dataFile.close();
    Serial.println(Amps);
  }
  else {
    Serial.println("error opening datalog.txt");
  }
  delay(2000);

  // listen for incoming clients
  EthernetClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // read file from SD card and send response
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/plain");
          client.println("Connnection: close");
          client.println();
          
          // open the file. note that only one file can be open at a time,
          // so you have to close this one before opening another.
          File dataFile = SD.open("anyFile.txt");

          // if the file is available, read its contents one byte at a time and send it to the ethernet client
          if (dataFile) {
            while (dataFile.available()) {
              client.print((char)dataFile.read());
                // delete the file:

            }
            dataFile.close();
            client.println();
            Serial.println("Removing example.txt...");
            SD.remove("anyFile.txt");
            }
            // if the file isn't open, pop up an error:
            else {
              Serial.println("error opening anyFile.txt");
              client.println("error opening anyFile.txt");
            } 
            break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } 
        else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(200);
    // close the connection:
    client.stop();
    Serial.println("client disonnected");
  }
}