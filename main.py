from tkinter import Tk
from impression_creator import OSARecommendationApp
from medical_parser import MedicalParserApp
from controller import Controller

if __name__ == "__main__":
    root = Tk()
    controller = Controller(root)
    app = OSARecommendationApp(root, controller)
    app = MedicalParserApp(root, controller)
    root.mainloop()