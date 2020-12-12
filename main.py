import pygame
import win32api
import win32con
import win32gui
import os
import keyboard
import json
import importlib

print(os.getcwd())
#os.chdir("../")
#print(os.getcwd())
#---------------------FOR PYGAME----------------------

#-----------------------------------------------------
#------------------END OF FUNCTIONS-------------------
#-----------------------------------------------------

#-----------------------------------------------------
#------------------END OF VARIABLES-------------------
#-----------------------------------------------------


pygame.init()
pygame.display.set_caption('EDPyHelper Alpha')
pygame.font.init()
screen = pygame.display.set_mode([1920, 1080], pygame.NOFRAME)
running = True
transparent = (0, 0, 0)  # Transparency color
#colour = (232, 90, 0)


overlay_font = pygame.font.SysFont(None, 30)



# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent), 0, win32con.LWA_COLORKEY)


#----------------------------------------------------
#------------------LOOP------------------------------
#----------------------------------------------------
class Main():

    default_config = {
        "path": f"{os.environ.get('homedrive')}{os.environ.get('homepath')}/saved games/frontier developments/elite dangerous".replace("\\", "/"),
        "colour": (232, 90, 0)
    }

    started = False



    def __init__(self):

        self.events = {
        'shutdown': self.shutdown
        }


        try:
            with open(f"{os.environ.get('appdata')}/edinfo/config.json") as f:
                self.config = json.load(f)

        except FileNotFoundError as e:
            print(e)
            self.config = self.default_config
            with open(f"{os.environ.get('appdata')}/edinfo/config.json", "w+") as f:
                f.write(json.dumps(self.default_config))

        self.colour = self.config["colour"]

        self.logs_list = [x for x in os.listdir(self.config["path"]) if x[-4:] == ".log"] 

        print(self.logs_list[-1])

        self.log_file = open(f"{self.config['path']}/{self.logs_list[-1]}")

        for i in range(10):
            line = self.log_file.readline()

        self.text = [f"{self.config['path']}/{self.logs_list[-1]}"]
        self.name = f"{self.config['path']}/{self.logs_list[-1]}" 


        #load modules
        for f in os.listdir():
            if f.endswith(".py") and f != "main.py":
                scope = {}
                try:
                    with open(f"./{f}") as code:
                        exec(code.read(), scope)

                    for event in scope["events"]:
                        self.events[event.__qualname__.lower()] = event if event.__qualname__ not in ["shutdown"] else self.events[event.__qualname__]
                except Exception as e:
                    print(e)
                #module = importlib.import_module(f[:-3])
                #try:
                #    for event in module.events:
                #        self.events[event.__qualname__.lower()] = event if event.__qualname__ not in ["shutdown", "fileheader"] else self.events[event.__qualname__]

                #except Exception as e:
                #    print(e)
        
        print(f"Loaded events: {self.events.keys()}")

        
        



    def run(self):
        self.logs_list = [x for x in os.listdir(self.config["path"]) if x[-4:] == ".log"] 

        name = (f"{self.config['path']}/{self.logs_list[-1]}")
        if name != self.name:
            self.log_file.close()
            self.log_file = open(name)
            self.name = name
            self.text = [name]


        line = self.log_file.readline()
        if line:

            event = json.loads(line)
            if event["event"].lower() in self.events.keys():
                try:

                    text = self.events[event["event"].lower()](event)

                    self.text = text.split("\n") if text and self.started else self.text

                except Exception as e:
                    self.text = [str(e).strip("\n")]
                    print(self.text)
        else:
            self.started = True
            return "False"

    def shutdown(self, event):
        if not self.started:
            self.started = True
            return "Waiting for game boot"
        pygame.quit()
        quit()



main = Main()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0x0001)

    


    #PYGAME TEXT UPDATES:
    text = main.run()

    #local_text = overlay_font.render(main.text, True, colour)

    #OVERLAY DRAWS:
    if text != "False":
        screen.fill(transparent)

        i = 40
        for line in main.text:
            text = overlay_font.render(line, True, main.colour)
            screen.blit(text, (15, i))
            #print(i)
            i += 30
        pygame.display.update()
    





    if keyboard.is_pressed("k") and keyboard.is_pressed("alt"): #Press ALT + K to exit.
        running = False
        pygame.quit()
        quit()