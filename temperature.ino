// This #include statement was automatically added by the Particle IDE.
#include <PietteTech_DHT.h>

#define DHTTYPE  AM2302       // Sensor type DHT11/21/22/AM2301/AM2302
#define DHTPIN   1            // ID of digital pin

PietteTech_DHT DHT(DHTPIN, DHTTYPE);

 double tempC = -1;
 double humidity = -1;

void setup()
{
    DHT.acquireAndWait();
}

void loop()
{
    tempC = DHT.getCelsius();
    humidity = DHT.getHumidity();
    Particle.publish("TEMPERATURE", String(tempC), PRIVATE);
    Particle.publish("HUMIDITY", String(humidity), PRIVATE);
    delay(5000);
}
