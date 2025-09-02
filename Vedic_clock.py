from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import time

# ===============================
# Vedic Units in Seconds
# ===============================
SEC_IN_TRUTI = 0.0004740740740740740
SEC_IN_VEDHA = 100 * SEC_IN_TRUTI
SEC_IN_LAVA = 3 * SEC_IN_VEDHA
SEC_IN_NIMESHA = 3 * SEC_IN_LAVA
SEC_IN_KSHANA = 3 * SEC_IN_NIMESHA
SEC_IN_KASHTHA = 5 * SEC_IN_KSHANA
SEC_IN_LAGHU = 15 * SEC_IN_KASHTHA
SEC_IN_NADIKA = 15 * SEC_IN_LAGHU
SEC_IN_MUHURTA = 2 * SEC_IN_NADIKA

TOTAL_VEDIC_DAY = 30 * SEC_IN_MUHURTA
SECONDS_IN_DAY = 24 * 3600
SCALE = SECONDS_IN_DAY / TOTAL_VEDIC_DAY

class VedicClockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.modern_label = Label(font_size=24, color=(0,0,1,1))
        self.vedic_label = Label(font_size=24, color=(0,1,0,1))
        self.layout.add_widget(self.modern_label)
        self.layout.add_widget(self.vedic_label)

        Clock.schedule_interval(self.update_clock, 1)
        return self.layout

    def update_clock(self, dt):
        now = time.localtime()
        modern_time = f"{now.tm_hour:02}:{now.tm_min:02}:{now.tm_sec:02}"

        seconds_since_midnight = now.tm_hour*3600 + now.tm_min*60 + now.tm_sec
        vedic_seconds = seconds_since_midnight / SCALE

        muhurta = int(vedic_seconds // SEC_IN_MUHURTA)
        rem = vedic_seconds % SEC_IN_MUHURTA
        nadika = int(rem // SEC_IN_NADIKA)
        rem %= SEC_IN_NADIKA
        laghu = int(rem // SEC_IN_LAGHU)
        rem %= SEC_IN_LAGHU
        kastha = int(rem // SEC_IN_KASHTHA)
        rem %= SEC_IN_KASHTHA
        kshana = int(rem // SEC_IN_KSHANA)
        rem %= SEC_IN_KSHANA
        nimesha = int(rem // SEC_IN_NIMESHA)

        vedic_time = f"{muhurta}:{nadika}:{laghu}:{kastha}:{kshana}:{nimesha}"

        self.modern_label.text = f"Modern Time: {modern_time}"
        self.vedic_label.text = f"Vedic Time: {vedic_time}"

if __name__ == "__main__":
    VedicClockApp().run()