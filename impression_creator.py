import re
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog


class OSARecommendationApp(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.master.title("OSA Recommendation")
        self.controller = controller

        self.my_font = Font(family="Times New Roman", size=9)

        self.text_frame = Frame(self)
        self.text_frame.pack()

        self.scrollbar = Scrollbar(self.text_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.report_text = Text(self.text_frame, font=self.my_font, yscrollcommand=self.scrollbar.set)
        self.report_text.pack()

        self.scrollbar.config(command=self.report_text.yview)

        self.next_button = Button(self, text="Next", command=self.controller.next_frame)
        self.next_button.pack()

        self.var_list = [IntVar() for _ in range(17)]

        self.check_texts = [
            "Mild Apnea", "Moderate or Severe Apnea", "CPAP no setting normalized",
            "CPAP arousal index remained elevated", "CPAP arousal index normalized",
            "Limb movements, no arousals", "Limb movements with arousals",
            "The patient endorses symptoms of RLS", "Hypersomnia", "Low sleep duration",
            "RBD on quest", "Split-night protocol was not met due to low apnea-hypopnea index (AHI).",
            "treatment emergent central apneas",
            "Low oxygen saturation was noted ",
            "Sleep related hypoventilation .",
            "Hypersomnia, OSA and low TST.",
            "Poor sleep efficiency."
        ]

        for i, check_text in enumerate(self.check_texts):
            Checkbutton(self, text=check_text, variable=self.var_list[i], command=lambda i=i: self.show_text()).pack()

        Button(self, text="Save Report", command=self.save_report).pack()
        Button(self, text="Clear Selections", command=self.clear_selections).pack()

    def show_text(self):
        self.report_text.delete(1.0, END)
        if self.var_list[0].get():
            mild_text = "1. Mild obstructive sleep apnea exacerbated in REM supine sleep. Respiratory events were associated with oxygen desaturations to a nadir of ***%.\n2. The severity of this sleep related breathing disorder maybe underestimated due to the absence of recorded REM and supine sleep in the baseline portion of the study, and to the presence of mild flow and effort decrements associated with arousal and/or oxygen desaturation not meeting established CMS respiratory event criteria.\n3. Treatment options for mild sleep apnea, include oral appliance, conservative measures (avoidance of alcohol, sedative medications and sleeping in the back position, management of nasal obstruction and weight loss), surgery and potentially PAP therapy if daytime symptoms and certain comorbidities are present."
            lines = re.split(r'(\d+\. )', mild_text)
            for line in lines:
                self.report_text.insert(END, line)
        if self.var_list[1].get():
            mod_text = "1. Moderate/Severe obstructive sleep apnea exacerbated in REM supine sleep. Respiratory events were associated with oxygen desaturations to a nadir of ***%. \n2. The severity of this sleep related breathing disorder maybe underestimated due to the absence of recorded REM and supine sleep in the baseline portion of the study, and to the presence of mild flow and effort decrements associated with arousal and/or oxygen desaturation not meeting established CMS respiratory event criteria.\n3. Untreated sleep apnea is associated with a variety of consequences, including, but not limited to hypertension, heart disease, stroke, obesity, and daytime sleepiness that can affect normal daytime functioning. Because of these consequences, treatment of sleep apnea is recommended.\n4. Treatment options for sleep apnea, including positive airway pressure (PAP) therapy, surgery, oral appliance and conservative measures (avoidance of alcohol, sedative medications and sleeping in the back position, management of nasal obstruction and weight loss), should be individualized. In many situations, a PAP titration study is the next step."
            lines = re.split(r'(\d+\. )', mod_text)
            for line in lines:
                self.report_text.insert(END, line)
        if self.var_list[2].get():
            self.report_text.insert(END, "\n\n1. None of the tested PAP settings normalized the apnea-hypopnea index (AHI).")
        if self.var_list[3].get():
            self.report_text.insert(END, "\n\n1. At a PAP setting of *** cmH2O during which supine *** REM sleep was *** was not "
                            "recorded the apnea-hypopnea index (AHI) was normalized snoring was *** was not eliminated "
                            "and oxygen saturation was maintained above *** %. The arousal index remained elevated at "
                            "this setting.")
        if self.var_list[4].get():
            self.report_text.insert(END, "\n\n1. At a PAP setting of *** cmH2O during which supine *** REM sleep was *** was not "
                            "recorded the apnea-hypopnea and arousal indices were normalized snoring was *** was not "
                            "eliminated and the oxygen saturation was maintained above ***%.")
        if self.var_list[5].get():
            self.report_text.insert(END, "\n\n4. Frequent periodic limb movements not causing arousal from sleep were observed, "
                            "which is a non-specific finding. These can be seen in a variety of conditions such as normal "
                            "aging, primary sleep disorders such as restless legs syndrome, sleep apnea, and narcolepsy, "
                            "or in association with certain medications. Clinical correlation is advised.")
        if self.var_list[6].get():
            self.report_text.insert(END, "\n\n4. Frequent periodic limb movements resulting in arousals from sleep were observed and "
                            "may be contributing to the patient’s sleep complaints.")
        if self.var_list[7].get():
            self.report_text.insert(END, "\n\n4. The patient endorses symptoms suggestive of restless legs syndrome (RLS) on the "
                            "pre-study questionnaire. As RLS remains a clinical diagnosis, further clinical correlation "
                            "is advised.")
        if self.var_list[8].get():
            self.report_text.insert(END, "\n\n4. Significant daytime sleepiness based on the Epworth Sleepiness Scale. Further "
                            "evaluation is warranted.")
        if self.var_list[9].get():
            self.report_text.insert(END, "\n\n4. The patient reports a total habitual sleep duration of 4***** hours. Seven to nine "
                            "hours of sleep is the recommendation for adults.")
        if self.var_list[10].get():
            self.report_text.insert(END, "\n\n4. On the provided sleep questionnaire, the patient endorses items including: sleep "
                            "walking, sleep talking, falling out of bed, nightmares, eating, seizures/convulsions in "
                            "sleep, night terrors, acting out dreams, and teeth grinding.  No abnormal behavior was noted "
                            "and normal REM sleep with atonia was noted.")
        if self.var_list[11].get():
            self.report_text.insert(END, "\n\n4. Split-night protocol was not met due to low apnea-hypopnea index (AHI).")
        if self.var_list[12].get():
            self.report_text.insert(END, "\n\n4. Of note, treatment emergent central apneas may indicate the presence of complex sleep apnea or a lack of PAP acclimation.")
        if self.var_list[13].get():
            self.report_text.insert(END, "\n\n4. Low oxygen saturation was noted during the study, with *** without hypercapnia, even in the absence of respiratory events. There may be another underlying cardiopulmonary disorder that explains these findings. Further clinical correlation is advised.")
        if self.var_list[14].get():
            self.report_text.insert(END, "\n\n4. Sleep related hypoventilation was noted. There was a >10 mmHg increase in end-tidal CO2 (ETCO2) and/or transcutaneous CO2 (TcpCO2) values during sleep as compared to the baseline wake ETCO2 value of *** mmHg and/or the baseline wake TcpCO2 value of *** mmHg. The ETCO2 and/or TcpCO2 value was >50 mmHg for > 10 minutes during sleep. The ETCO2 and/or TcpCO2 value was >55 mmHg for > 10 minutes during sleep. There may be another underlying cardiopulmonary disorder that explains these findings. Further clinical correlation is advised.")
       # if self.var_list[15].get():
       #     self.report_text.insert(END, "\n\n4. To further evaluate hypersomnia, a multiple sleep latency test was performed following this study and will be reported separately.")
        if self.var_list[15].get():
            self.report_text.insert(END, "\n\n4. Hypersomnia, as indicated by the elevated Epworth sleepiness scale, is not otherwise explained by the findings on this study. Of note the patient endorses a habitual sleep time of *** hours per night. A comprehensive sleep evaluation may be warranted if symptoms persist following the successful treatment of OSA and after increasing total sleep time.")
        if self.var_list[16].get():
            self.report_text.insert(END, "\n\n4. Poor sleep efficiency of 29.4% (total recording time (TRT) = 365 m) and a prolonged sleep latency of 97.0 minutes were noted. These could be explained in part by the patient having difficulty acclimating to PAP therapy.")

    def save_report(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.report_text.get(1.0, END))

    def clear_selections(self):
        for var in self.var_list:
            var.set(0)
        self.report_text.delete(1.0, END)


