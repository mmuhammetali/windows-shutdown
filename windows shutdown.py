from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import webbrowser
import os

class CountdownApp(App):
    def build(self):
        Window.size = (300, 400)


        self.ana_pencere = FloatLayout(size_hint=(1.5, 1.5))


        self.süre = Label(text="SÜRE GİRİNİZ:",font_size = 15, pos_hint={"center_x": 0.325, "center_y": 0.6}, size_hint=(0.2, 0.1))
        self.süregiris = TextInput(font_size=35,multiline = False,pos_hint={"center_x": 0.325, "center_y": 0.5}, size_hint=(0.3, 0.1),background_color = ("696969"))
        self.ana_pencere.add_widget(self.süre)
        self.ana_pencere.add_widget(self.süregiris)


        self.time_left = 0# süre dakika cinsinden verilmiştir
        self.label = Label(text=self.format_time(self.time_left),font_size = 40, pos_hint={"center_x": 0.325, "center_y": 0.35}, size_hint=(0.3, 0.2))

        self.ana_pencere.add_widget(self.label)

        self.button = Button(text="BAŞLA",font_size = 25,pos_hint={"center_x": 0.325, "center_y": 0.2}, size_hint=(0.35, 0.1),background_color = ("696969"))
        self.button.bind(on_press = self.kontrol)

        self.opengithub=Button(text=" Git\nHub",font_size = 15,pos_hint={"center_x": 0.63, "center_y": 0.6259}, size_hint=(0.08, 0.08))
        self.opengithub.bind(on_press = self.open_github)



        self.bitirici = Button(text="İPTAL",font_size = 25,pos_hint={"center_x": 0.325, "center_y": 0.1}, size_hint=(0.35, 0.1),background_color = ("696969"))
        self.bitirici.bind(on_press = self.iptal)

        self.quit = Button(text="ÇIKIŞ", font_size=14, background_color=(1, 0, 0, 1),pos_hint={"center_x": 0.325, "center_y": 0.026}, size_hint=(0.35, 0.05))
        self.quit.bind(on_press = self.çık)


        self.ana_pencere.add_widget(self.opengithub)
        self.ana_pencere.add_widget(self.quit)
        self.ana_pencere.add_widget(self.button)
        self.ana_pencere.add_widget(self.bitirici)

        return self.ana_pencere

    def open_github(self, instance):
        webbrowser.open('https://github.com/mmuhammetali')


    def çık(self, args):
        App.get_running_app().stop()



    def on_start(self,args):
        self.title = "WİNDOWS OTO KAPAT"
    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)



    def kontrol(self, args):
        giriş = self.süregiris.text
        if not giriş:
            self.süregiris.text= ""
        else:

            Clock.schedule_interval(self.countdown, 1)
            self.time_left = int(self.süregiris.text)3600
            süresaat = int(self.süregiris.text)3600
            command = f"shutdown /s /t {süresaat} "
            os.system(command)


    def countdown(self, dt):
        self.time_left -= 1
        if self.time_left < 1:
            Clock.unschedule(self.countdown)
        self.label.text = self.format_time(self.time_left)


    def iptal(self, *args):
        self.time_left = 1
        command = "shutdown /a"
        os.system(command)

CountdownApp().run()
