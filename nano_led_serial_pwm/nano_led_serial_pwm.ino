const int ledPin = 9;
bool ledState = false; // 처음엔 꺼진 상태

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  randomSeed(analogRead(A0));
  analogWrite(ledPin, 0); 
}

void loop() {
  // 시리얼 신호가 들어오면 즉시 상태 변경
  if (Serial.available() > 0) {
    char input = Serial.read();
    if (input == '1') {
      ledState = true;
    } else if (input == '0') {
      ledState = false;
      analogWrite(ledPin, 0); // 즉시 끄기
    }
  }

  // ledState가 true일 때만 용접 효과(깜빡임) 실행
  if (ledState) {
    analogWrite(ledPin, 255);
    delay(random(20, 100)); // 켜져 있는 시간 랜덤
    
    int light_low = random(100, 150);
    analogWrite(ledPin, light_low);
    delay(30); // 살짝 어두워지는 시간
  }
}