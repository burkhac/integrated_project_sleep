import tkinter as tk
from impression_creator import OSARecommendationApp
from medical_parser import MedicalParserApp


class Controller:
    def __init__(self, root):
        self.root = root
        self.frames = {}
        self.current_frame = None

        self.create_frames()
        self.show_frame("OSARecommendationApp")

    def create_frames(self):
        self.frames["OSARecommendationApp"] = OSARecommendationApp(self.root, self)
        self.frames["MedicalParserApp"] = MedicalParserApp(self.root, self)

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack(fill="both", expand=True)

    def next_frame(self):
        if self.current_frame == self.frames["OSARecommendationApp"]:
            self.show_frame("MedicalParserApp")
        elif self.current_frame == self.frames["MedicalParserApp"]:
            self.show_frame("OSARecommendationApp")

    def previous_frame(self):
        self.next_frame()  # If you only have two frames, next and previous are the same
