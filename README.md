# newton-ring-3d-simulation
This project simulates Newton’s rings in 3D, visualizing the interference pattern formed due to the reflection of light between a convex lens and a flat surface. It helps in understanding optical interference phenomena and can be used for educational and research purposes.


#include <FastLED.h>

#define LED_PIN     3       // Arduino pin connected to Data In of matrix
#define NUM_LEDS    64      // 8x8 matrix = 64 LEDs
#define BRIGHTNESS  64      // Adjust brightness (0-255)
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB

CRGB leds[NUM_LEDS];

void setup() {
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS);
  FastLED.setBrightness(BRIGHTNESS);
  FastLED.clear();
  FastLED.show();
}

void loop() {
  // Example: Fill the matrix with red color
  fill_solid(leds, NUM_LEDS, CRGB::Red);
  FastLED.show();
  delay(1000);

  // Fill the matrix with green color
  fill_solid(leds, NUM_LEDS, CRGB::Green);
  FastLED.show();
  delay(1000);

  // Fill the matrix with blue color
  fill_solid(leds, NUM_LEDS, CRGB::Blue);
  FastLED.show();
  delay(1000);

  // Rainbow animation example
  rainbowCycle(20);
}

// Rainbow cycle animation function
void rainbowCycle(uint8_t wait) {
  static uint8_t startIndex = 0;
  startIndex = startIndex + 1; /* motion speed */
  fill_rainbow(leds, NUM_LEDS, startIndex, 7);
  FastLED.show();
  delay(wait);
}
