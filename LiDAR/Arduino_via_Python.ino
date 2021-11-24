float x=0;

void setup() {
 Serial.begin(9600);
 Serial.print("the data is: ");
 Serial.println(x);
}

void loop() {
  Serial.println(x);
  x = x + 0.1;
  delay(2000);
}
