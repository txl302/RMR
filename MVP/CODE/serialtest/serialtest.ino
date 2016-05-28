/* Arduino firmware for serial printing test   */
/* working with RMR/MVP/CODE/main/rmrserial.py */
/* By Bowen & Tao                              */
/* 05/24/2016                                  */
/***********************************************/

void setup() {
  // initialize serial
  Serial.begin(115200);
  while (!Serial)  {
    ; // wait for serial port to connect
  }
}

void loop()  {
  for(int x = 0; x < 1000; x++)  {
    Serial.print("test");
    delay(10);
  }
}



