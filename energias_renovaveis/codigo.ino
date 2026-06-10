int ldr = A0;

int ledVerde = 7;
int ledAmarelo = 5;
int ledVermelho = 6;

void setup() {

  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);

  Serial.begin(9600);

  Serial.println("=================================");
  Serial.println("GOODCHARGE AI");
  Serial.println("Sistema Inteligente de Carregamento EV");
  Serial.println("=================================");
}

void loop() {

  int valorLuz = analogRead(ldr);

  Serial.print("Leitura LDR: ");
  Serial.println(valorLuz);

  // RESET DOS LEDS
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarelo, LOW);
  digitalWrite(ledVermelho, LOW);

  // =====================================
  // ALTA DISPONIBILIDADE SOLAR (> 900)
  // =====================================
  if (valorLuz > 900) {

    digitalWrite(ledVerde, HIGH);

    Serial.println("Status Solar: ALTA");
    Serial.println("Modo: CARREGAMENTO MAXIMO");
    Serial.println("Potencia Simulada: 100%");
  }

  // =====================================
  // DISPONIBILIDADE MÉDIA (> 200)
  // =====================================
  else if (valorLuz > 200) {

    digitalWrite(ledAmarelo, HIGH);

    Serial.println("Status Solar: MEDIA");
    Serial.println("Modo: CARREGAMENTO ECONOMICO");
    Serial.println("Potencia Simulada: 60%");
  }

  // =====================================
  // BAIXA DISPONIBILIDADE SOLAR (≤ 200)
  // =====================================
  else {

    digitalWrite(ledVermelho, HIGH);

    Serial.println("Status Solar: BAIXA");
    Serial.println("Modo: CARREGAMENTO REDUZIDO");
    Serial.println("Potencia Simulada: 20%");
  }

  Serial.println("---------------------------------");

  delay(1000);
}