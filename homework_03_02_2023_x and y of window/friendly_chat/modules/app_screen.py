import customtkinter
# створюємо клас App 
class App(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        
        # зліва зверху
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        
        
        #по центру 1
        #self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH // 2}+{self.PC_SCREEN_HEIGHT // 2}")
        
        #по центру 2
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH // 2 - self.APP_WIDTH // 2}+{self.PC_SCREEN_HEIGHT // 2 - self.APP_HEIGHT // 2}")
        
        #зліва знизу 1
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{self.PC_SCREEN_HEIGHT}")
        
        #зліва знизу 2
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{self.PC_SCREEN_HEIGHT-self.APP_HEIGHT}")
        
        #справа зверху 1
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH}+{0}")
        
        #справа зверху 2
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH - self.APP_WIDTH}+{0}")
        
        #справа знизу 1
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH}+{self.PC_SCREEN_HEIGHT}")
        
        #справа знизу 2
        # self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH - self.APP_WIDTH}+{self.PC_SCREEN_HEIGHT - self.APP_HEIGHT}")
        
        
        
        
        
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
# створюємо об'єкт від класу App
app = App(app_width= 400, app_height = 300)
