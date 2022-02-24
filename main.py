from pynput.keyboard import Key, Controller, KeyCode
import time
from rich.progress import Progress
from rich import print


def get_time():
    minutes_ = input("Minutes ? \n\t> ")
    if minutes_ == "":
        minutes = 0
    else:
        minutes = int(minutes_)

    hours_ = input("Hours ? \n\t> ")
    if hours_ == "":
        hours = 0
    else:
        hours = int(hours_)

    return minutes, hours


if __name__ == "__main__":
    minutes, hours = get_time()

    secs = int(60 * (minutes + 60 * hours))
    while secs == 0:
        print("[red]:warning: The cooldown can't be null !")
        minutes, hours = get_time()
        secs = int(60 * (minutes + 60 * hours))

    print(f"[red]Sleep in [b]{hours} hours[/b] and [b]{minutes} minutes[/b]")
    keyboard = Controller()
    with Progress() as pr:
        task1 = pr.add_task("[blue] Cooldown...", total=secs)
        while not pr.finished:
            pr.update(task1, advance=1)
            time.sleep(1)

    with Progress() as pr:
        task2 = pr.add_task("[gray italic] Sleep...", total=100)
        while not pr.finished:
            pr.update(task2, advance=1)
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            time.sleep(0.5)
    keyboard.press(KeyCode.from_vk(0xB3))
    print("[green b u]Music Paused")
    for i in range(100):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
