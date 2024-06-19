import tkinter as tk
from tkinter import scrolledtext

# List of medical problems to look for
MEDICAL_PROBLEMS = [
    "Allergic rhinitis", "Allergies", "Anxiety", "Asthma", "Atrial fibrillation", "Atrial flutter",
    "Attention deficit hyperactivity disorder", "Bipolar disorder", "Chronic obstructive pulmonary disease",
    "Chronic respiratory failure with hypoxia", "Sleep related hypoventilation", "Narcolepsy",
    "Complete heart block", "Chronic rhinitis", "Chronic sinusitis", "Class III obesity",
    "Congestive heart failure", "Coronary artery disease", "Depression", "Depressive disorder", "Deviated nasal septum",
    "Diabetes", "Diabetes mellitus type I", "Diabetes mellitus type II", "Diabetic neuropathy",
    "Diabetes insipidus", "Emphysema", "Epilepsy", "Gastroesophageal reflux disease", "GERD",
    "Chronic headache", "Hyperlipidemia", "Hypertension", "Hypothyroidism", "Insomnia", "Lumbago",
    "Obesity", "Obstructive sleep apnea", "Peripheral neuropathy", "Pulmonary hypertension",
    "Pulmonary embolism", "Restless legs syndrome", "Seizures", "Stroke", "Status post bariatric surgery",
    "Status post upper airway surgery"
]

class MedicalParserApp(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.master.title("Parser")
        self.master.geometry("800x600")

        self.var = tk.IntVar()
        self.var.set(1)  # Default to Medications

        self.setup_ui()

    def setup_ui(self):
        # Create radio buttons
        self.radio_medications = tk.Radiobutton(self, text="Medications", variable=self.var, value=1)
        self.radio_medications.pack(pady=10)

        self.radio_problems = tk.Radiobutton(self, text="Medical Problems", variable=self.var, value=2)
        self.radio_problems.pack(pady=10)

        # Create input field
        self.input_label = tk.Label(self, text="Paste Text Here:")
        self.input_label.pack(pady=10)

        self.input_field = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=100, height=20)
        self.input_field.pack(pady=10)

        # Create submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)

        # Create output field
        self.output_label = tk.Label(self, text="Parsed List:")
        self.output_label.pack(pady=10)

        self.output_field = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=100, height=10, state='disabled')
        self.output_field.pack(pady=10)

        self.next_button = tk.Button(self, text="Back", command=self.controller.next_frame)
        self.next_button.place(anchor="nw")

    def parse_medications(self, input_text):
        lines = input_text.strip().split('\n')
        med_names = []
        for line in lines:
            if '(' in line and ')' in line:
                start = line.find('(') + 1
                end = line.find(')')
                med_name = line[start:end].split(',')[0].strip().title()
                med_names.append(med_name)
            else:
                words = line.split()
                if len(words) > 0:
                    med_name = words[0].title()
                    med_names.append(med_name)
        return ', '.join(med_names)

    def parse_medical_problems(self, input_text):
        found_problems = []
        for problem in MEDICAL_PROBLEMS:
            if problem.lower() in input_text.lower():
                found_problems.append(problem)
        return ', '.join(found_problems)

    def on_submit(self):
        input_text = self.input_field.get("1.0", tk.END)
        if self.var.get() == 1:
            result = self.parse_medications(input_text)
        else:
            result = self.parse_medical_problems(input_text)
        self.output_field.config(state='normal')
        self.output_field.delete('1.0', tk.END)
        self.output_field.insert(tk.END, result)
        self.output_field.config(state='disabled')



