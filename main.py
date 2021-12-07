from pynput.keyboard import Key, Controller, KeyCode
import time

if __name__ == '__main__':
    t = str(input("Saisissez le temps avant d'éteindre la musique: (ex: 20m)\n\t> "))
    minutes = 0
    hour = 0
    t_ = t.split("h")
    if len(t_) == 2:
        minutes = int(t_[1].replace("m", ""))
        hour = int(t_[0])
    elif len(t_) == 1:
        if "m" in t:
            minutes = int(t_[0].replace("m", ""))
        elif "h" in t:
            hour = int(t_[0])
    print(f"Sleep in {minutes} minutes and {hour} hours.")
    keyboard = Controller()
    secs = 60*minutes + 60*60*hour
    for i in range(secs):
        time.sleep(0.9)
        print(secs-i)
    for i in range(100):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        time.sleep(0.5)
    print("Music Paused")
    keyboard.press(KeyCode.from_vk(0xB3))
    for i in range(100):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
