import time
from customtkinter import *
from client_methods import *

HE_client = HEClient()

""" UI CLASSES """
class Preview(CTkFrame):
    def __init__(self, master, value=None, **kwargs):
        super().__init__(master, **kwargs)

        # Content
        self.content = CTkLabel(self, text=value, font=("Inter", 13), wraplength=840, justify="left")
        self.content.grid(row=0, column=0, padx="15px", pady="15px", sticky="news")
        self.grid_rowconfigure(0, weight=1)

class Visual(CTkFrame):
    def __init__(self, master, label=None, value=None, time=None, **kwargs):
        super().__init__(master, **kwargs)

        # Label
        self.label = CTkLabel(master=self, text=f"{label}:", font=("Inter", 13))
        self.label.grid(row=0, column=0, padx="20px", pady="10px", sticky="nw")
        self.grid_columnconfigure(0, weight=1)

        self.time = CTkLabel(master=self, text=f"Done in {time}s", font=("Inter", 13))
        self.time.grid(row=0, column=1, padx="20px", pady="10px", sticky="ne")
        self.grid_columnconfigure(1, weight=1)

        # Content
        self.preview = Preview(self, value=value, border_width=1, border_color="#000000", corner_radius=10)
        self.preview.grid(row=1, column=0, padx="20px", pady=(0, 20), sticky="nw", columnspan=2)


""" SECTIONS """
class Step4(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label
        labelText = "Step 4: Decryption of Output"
        self.label = CTkLabel(master=self, text=labelText, font=("Inter", 16))
        self.label.grid(row=0, column=0, pady=(40, 20), sticky="nw")

        desc = "Client Side. The client receives encrypted outputs from the server. This means only the client with the private key can decrypt the data."
        self.desc = CTkLabel(master=self, text=desc, font=("Inter", 13), wraplength=900, justify="left")
        self.desc.grid(row=1, column=0, sticky="nw")

        # Dependent Lookup
        self.sub1 = CTkFrame(self, fg_color="transparent")
        self.sub1.grid(row=2, column=0, pady=(20, 0), sticky="ew")
        self.sub1.grid_columnconfigure(0, weight=1)
        self.sub1_label = CTkLabel(self.sub1, text="Operation 2: Dependent Lookup", font=("Inter", 13))
        self.sub1_label.grid(row=0, column=0, sticky="nw")

        # Button
        self.sub1_button = CTkButton(self, text="Decrypt dependent information", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000")
        self.sub1_button.grid(row=3, column=0, pady=(5, 20), sticky="ew")

        # Textarea
        self.sub1_visual = Visual(self, label="Decrypted Dependents", value=desc, time="0.0002", border_width=1, border_color="#000000", corner_radius=10)
        self.sub1_visual.grid(row=4, column=0, sticky="ew")

        # Dependent Declaration
        self.sub2 = CTkFrame(self, fg_color="transparent")
        self.sub2.grid(row=5, column=0, pady=(20, 0), sticky="ew")
        self.sub2.grid_columnconfigure(0, weight=1)
        self.sub2_label = CTkLabel(self.sub2, text="Operation 3: Estimate Contribution", font=("Inter", 13))
        self.sub2_label.grid(row=0, column=0, sticky="nw")

        # Button
        self.sub2_button = CTkButton(self, text="Decrypt estimated contribution", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000")
        self.sub2_button.grid(row=6, column=0, pady=(5, 20), sticky="ew")

        # # Textarea
        self.sub2_visual = Visual(self, label="Decrypted estimated contribution", value=desc, time="0.0002", border_width=1, border_color="#000000", corner_radius=10)
        self.sub2_visual.grid(row=7, column=0, sticky="ew")

class Step3(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label
        labelText = "Step 3: Public Operations"
        self.label = CTkLabel(master=self, text=labelText, font=("Inter", 16))
        self.label.grid(row=0, column=0, pady=(40, 20), sticky="nw")

        desc = "Server Side. Once server receives encrypted input, the server adds the data to the database. Operations can be done on the server without decrypting the data. For the demonstration, three operations are provided: (1) record counting according to condition, (2) dependent lookup, and (3) contribution calculation using a Decision Tree."
        self.desc = CTkLabel(master=self, text=desc, font=("Inter", 13), wraplength=900, justify="left")
        self.desc.grid(row=1, column=0, sticky="nw")

        # Member Personal Details
        self.sub1 = CTkFrame(self, fg_color="transparent")
        self.sub1.grid(row=2, column=0, pady=(20, 0), sticky="ew")
        self.sub1.grid_columnconfigure(0, weight=1)
        self.sub1_label = CTkLabel(self.sub1, text="Operation 1: Record Counting", font=("Inter", 13))
        self.sub1_label.grid(row=0, column=0, sticky="nw")

        # Member Name
        self.sub1_frame = CTkFrame(self.sub1, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_frame.grid(row=1, column=0, pady=(5, 0), sticky="ew")
        self.sub1_name_label = CTkLabel(self.sub1_frame, text="Member Name", font=("Inter", 13))
        self.sub1_name_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_lastname = CTkEntry(self.sub1_frame, placeholder_text="Last Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_lastname.grid(row=1, column=0, padx=(20, 0), pady=(0, 20), sticky="ew")
        self.sub1_firstname = CTkEntry(self.sub1_frame, placeholder_text="First Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_firstname.grid(row=1, column=1, padx="5px", pady=(0, 20), sticky="ew")
        self.sub1_middlename = CTkEntry(self.sub1_frame, placeholder_text="Middle Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_middlename.grid(row=1, column=2, padx=(0, 20), pady=(0, 20), sticky="ew")
        self.sub1_frame.grid_columnconfigure(0, weight=1)
        self.sub1_frame.grid_columnconfigure(1, weight=1)
        self.sub1_frame.grid_columnconfigure(2, weight=1)

        # Birth Details
        self.sub1_bday_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_bday_frame.grid(row=2, column=0, sticky="ew", columnspan=2)
        self.sub1_bday_label = CTkLabel(self.sub1_bday_frame, text="Member Birth Details", font=("Inter", 13))
        self.sub1_bday_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_bday = CTkEntry(self.sub1_bday_frame, placeholder_text="Birthday (DD/MM/YYYY)", font=("Inter", 13), height=40, width=200, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_bday.grid(row=1, column=0, padx=(20, 0), pady=(0, 20), sticky="ew")
        self.sub1_placeofbrith = CTkEntry(self.sub1_bday_frame, placeholder_text="Place of Birth (City/Municipality/Province/Country)", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_placeofbrith.grid(row=1, column=1, padx=(5, 20), pady=(0, 20), sticky="ew")
        self.sub1_bday_frame.grid_columnconfigure(1, weight=1)

        # Income
        self.sub1_income_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_income_frame.grid(row=2, column=2, sticky="ew")
        self.sub1_income_label = CTkLabel(self.sub1_income_frame, text="Income Bracket", font=("Inter", 13))
        self.sub1_income_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_income = CTkComboBox(self.sub1_income_frame, values=["PHP 10k below", "PHP 10k - 50k", "PHP 10k - 100k", "PHP 100k above"], font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_income.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.sub1_income_frame.grid_columnconfigure(0, weight=1)

        # Sex
        self.sub1_sex_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_sex_frame.grid(row=3, column=2, sticky="ew")
        self.sub1_sex_label = CTkLabel(self.sub1_sex_frame, text="Sex", font=("Inter", 13))
        self.sub1_sex_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_sex_var = StringVar(value="male")
        self.sub1_sex_male = CTkRadioButton(self.sub1_sex_frame, text="Male", value="male", font=("Inter", 13), variable=self.sub1_sex_var)
        self.sub1_sex_male.grid(row=1, column=0, padx=(20, 5), pady=(0, 20), sticky="nw")
        self.sub1_sex_female = CTkRadioButton(self.sub1_sex_frame, text="Female", value="female", font=("Inter", 13), variable=self.sub1_sex_var)
        self.sub1_sex_female.grid(row=1, column=1, padx=(0, 20), pady=(0, 20), sticky="nw")

        # Civil Status
        self.sub1_cs_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_cs_frame.grid(row=3, column=1, sticky="ew")
        self.sub1_cs_label = CTkLabel(self.sub1_cs_frame, text="Civil Status", font=("Inter", 13))
        self.sub1_cs_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_cs_var = StringVar(value="single")
        self.sub1_cs_single = CTkRadioButton(self.sub1_cs_frame, text="Single", value="single", font=("Inter", 13), variable=self.sub1_cs_var)
        self.sub1_cs_single.grid(row=1, column=0, padx=(20, 0), pady=(0, 20), sticky="nw")
        self.sub1_cs_married = CTkRadioButton(self.sub1_cs_frame, text="Married", value="married", font=("Inter", 13), variable=self.sub1_cs_var)
        self.sub1_cs_married.grid(row=1, column=1, padx=5, pady=(0, 20), sticky="nw")
        self.sub1_cs_widowed = CTkRadioButton(self.sub1_cs_frame, text="Widowed", value="widowed", font=("Inter", 13), variable=self.sub1_cs_var)
        self.sub1_cs_widowed.grid(row=1, column=2, padx=(0, 20), pady=(0, 20), sticky="nw")

        # Citizenship
        self.sub1_ctz_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_ctz_frame.grid(row=3, column=0, sticky="ew")
        self.sub1_ctz_label = CTkLabel(self.sub1_ctz_frame, text="Citizenship", font=("Inter", 13))
        self.sub1_ctz_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_ctz_var = StringVar(value="indigenous")
        self.sub1_ctz_filipino = CTkRadioButton(self.sub1_ctz_frame, text="Filipino", value="filipino", font=("Inter", 13), variable=self.sub1_ctz_var)
        self.sub1_ctz_filipino.grid(row=1, column=0, padx=(20, 5), pady=(0, 20), sticky="nw")
        self.sub1_ctz_foreign = CTkRadioButton(self.sub1_ctz_frame, text="Foreign National", value="foreign", font=("Inter", 13), variable=self.sub1_ctz_var)
        self.sub1_ctz_foreign.grid(row=1, column=1, padx=(0, 20), pady=(0, 20), sticky="nw")

        # Button
        self.sub1_button = CTkButton(self, text="Count Retrieved Records", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000")
        self.sub1_button.grid(row=3, column=0, pady="20px", sticky="ew")

        # Textarea
        self.sub1_visual = Visual(self, label="Retrieved Records", value=desc, time="0.0002", border_width=1, border_color="#000000", corner_radius=10)
        self.sub1_visual.grid(row=4, column=0, sticky="ew")

        # Dependent Declaration
        self.sub2 = CTkFrame(self, fg_color="transparent")
        self.sub2.grid(row=5, column=0, pady=(20, 0), sticky="ew")
        self.sub2.grid_columnconfigure(0, weight=1)
        self.sub2_label = CTkLabel(self.sub2, text="Operation 2: Dependent Lookup", font=("Inter", 13))
        self.sub2_label.grid(row=0, column=0, sticky="nw")

        # Dependent Name
        self.sub2_frame = CTkFrame(self.sub2, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_frame.grid(row=1, column=0, pady=(5, 0), sticky="ew")
        self.sub2_name_label = CTkLabel(self.sub2_frame, text="Member Name", font=("Inter", 13))
        self.sub2_name_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub2_lastname = CTkEntry(self.sub2_frame, placeholder_text="Last Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_lastname.grid(row=1, column=0, padx=(20, 0), pady=(0, 20), sticky="ew")
        self.sub2_firstname = CTkEntry(self.sub2_frame, placeholder_text="First Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_firstname.grid(row=1, column=1, padx="5px", pady=(0, 20), sticky="ew")
        self.sub2_middlename = CTkEntry(self.sub2_frame, placeholder_text="Middle Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_middlename.grid(row=1, column=2, padx=(0, 20), pady=(0, 20), sticky="ew")
        self.sub2_frame.grid_columnconfigure(0, weight=1)
        self.sub2_frame.grid_columnconfigure(1, weight=1)
        self.sub2_frame.grid_columnconfigure(2, weight=1)

        # Button
        self.sub2_button = CTkButton(self, text="Retrieve dependents and send to client", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000")
        self.sub2_button.grid(row=6, column=0, pady="20px", sticky="ew")

        # # Textarea
        self.sub2_visual = Visual(self, label="Encrypted Dependents", value=desc, time="0.0002", border_width=1, border_color="#000000", corner_radius=10)
        self.sub2_visual.grid(row=7, column=0, sticky="ew")

        # Estimate Contribution
        self.sub3 = CTkFrame(self, fg_color="transparent")
        self.sub3.grid(row=8, column=0, pady=(20, 0), sticky="ew")
        self.sub3.grid_columnconfigure(0, weight=1)
        self.sub3_label = CTkLabel(self.sub3, text="Operation 3: Estimate Contribution", font=("Inter", 13))
        self.sub3_label.grid(row=0, column=0, sticky="nw")

        # Button
        self.sub3_button = CTkButton(self, text="Calculate estimated contribution and send to client", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000")
        self.sub3_button.grid(row=9, column=0, pady=(5, 20), sticky="ew")

        # # Textarea
        self.sub3_visual = Visual(self, label="Encrypted Dependents", value=desc, time="0.0002", border_width=1, border_color="#000000", corner_radius=10)
        self.sub3_visual.grid(row=10, column=0, sticky="ew")

class Step2(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label
        labelText = "Step 2: Client Information"
        self.label = CTkLabel(master=self, text=labelText, font=("Inter", 16))
        self.label.grid(row=0, column=0, pady=(40, 20), sticky="nw")

        desc = "Client Side. Information from client is obtained here. For demonstration purposes, the server uses a system similar to PhilHealth. Client will be requested two groups of information: (1) the client’s personal information and (2) the client’s dependents. Information is encrypted with private key and then sent to the server."
        self.desc = CTkLabel(master=self, text=desc, font=("Inter", 13), wraplength=900, justify="left")
        self.desc.grid(row=1, column=0, sticky="nw")

        # Member Personal Details
        self.sub1 = CTkFrame(self, fg_color="transparent")
        self.sub1.grid(row=2, column=0, pady=(20, 0), sticky="ew")
        self.sub1.grid_columnconfigure(0, weight=1)
        self.sub1_label = CTkLabel(self.sub1, text="Member Personal Details", font=("Inter", 13))
        self.sub1_label.grid(row=0, column=0, sticky="nw")

        # Member Name
        self.sub1_frame = CTkFrame(self.sub1, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_frame.grid(row=1, column=0, pady=(5, 0), sticky="ew")
        self.sub1_name_label = CTkLabel(self.sub1_frame, text="Member Name", font=("Inter", 13))
        self.sub1_name_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_lastname = CTkEntry(self.sub1_frame, placeholder_text="Last Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_lastname.grid(row=1, column=0, padx=(20, 0), pady=(0, 20), sticky="ew")
        self.sub1_firstname = CTkEntry(self.sub1_frame, placeholder_text="First Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_firstname.grid(row=1, column=1, padx="5px", pady=(0, 20), sticky="ew")
        self.sub1_middlename = CTkEntry(self.sub1_frame, placeholder_text="Middle Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_middlename.grid(row=1, column=2, padx=(0, 20), pady=(0, 20), sticky="ew")
        self.sub1_frame.grid_columnconfigure(0, weight=1)
        self.sub1_frame.grid_columnconfigure(1, weight=1)
        self.sub1_frame.grid_columnconfigure(2, weight=1)

        # Birth Details
        self.sub1_bday_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_bday_frame.grid(row=2, column=0, sticky="ew", columnspan=2)
        self.sub1_bday_label = CTkLabel(self.sub1_bday_frame, text="Member Birth Details", font=("Inter", 13))
        self.sub1_bday_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_bday = CTkEntry(self.sub1_bday_frame, placeholder_text="Birthday (DD/MM/YYYY)", font=("Inter", 13), height=40, width=200, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_bday.grid(row=1, column=0, padx=(20, 0), pady=(0, 20), sticky="ew")
        self.sub1_placeofbrith = CTkEntry(self.sub1_bday_frame, placeholder_text="Place of Birth (City/Municipality/Province/Country)", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_placeofbrith.grid(row=1, column=1, padx=(5, 20), pady=(0, 20), sticky="ew")
        self.sub1_bday_frame.grid_columnconfigure(1, weight=1)

        # Income
        self.sub1_income_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_income_frame.grid(row=2, column=2, sticky="ew")
        self.sub1_income_label = CTkLabel(self.sub1_income_frame, text="Income Bracket", font=("Inter", 13))
        self.sub1_income_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_income = CTkComboBox(self.sub1_income_frame, values=["PHP 10k below", "PHP 10k - 50k", "PHP 10k - 100k", "PHP 100k above"], font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub1_income.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.sub1_income_frame.grid_columnconfigure(0, weight=1)

        # Sex
        self.sub1_sex_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_sex_frame.grid(row=3, column=2, sticky="ew")
        self.sub1_sex_label = CTkLabel(self.sub1_sex_frame, text="Sex", font=("Inter", 13))
        self.sub1_sex_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_sex_var = StringVar(value="male")
        self.sub1_sex_male = CTkRadioButton(self.sub1_sex_frame, text="Male", value="male", font=("Inter", 13), variable=self.sub1_sex_var)
        self.sub1_sex_male.grid(row=1, column=0, padx=(20, 5), pady=(0, 20), sticky="nw")
        self.sub1_sex_female = CTkRadioButton(self.sub1_sex_frame, text="Female", value="female", font=("Inter", 13), variable=self.sub1_sex_var)
        self.sub1_sex_female.grid(row=1, column=1, padx=(0, 20), pady=(0, 20), sticky="nw")

        # Civil Status
        self.sub1_cs_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_cs_frame.grid(row=3, column=1, sticky="ew")
        self.sub1_cs_label = CTkLabel(self.sub1_cs_frame, text="Civil Status", font=("Inter", 13))
        self.sub1_cs_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_cs_var = StringVar(value="single")
        self.sub1_cs_single = CTkRadioButton(self.sub1_cs_frame, text="Single", value="single", font=("Inter", 13), variable=self.sub1_cs_var)
        self.sub1_cs_single.grid(row=1, column=0, padx=(20, 0), pady=(0, 20), sticky="nw")
        self.sub1_cs_married = CTkRadioButton(self.sub1_cs_frame, text="Married", value="married", font=("Inter", 13), variable=self.sub1_cs_var)
        self.sub1_cs_married.grid(row=1, column=1, padx=5, pady=(0, 20), sticky="nw")
        self.sub1_cs_widowed = CTkRadioButton(self.sub1_cs_frame, text="Widowed", value="widowed", font=("Inter", 13), variable=self.sub1_cs_var)
        self.sub1_cs_widowed.grid(row=1, column=2, padx=(0, 20), pady=(0, 20), sticky="nw")

        # Citizenship
        self.sub1_ctz_frame = CTkFrame(self.sub1_frame, fg_color="transparent", corner_radius=0, border_width=1, border_color="#000000")
        self.sub1_ctz_frame.grid(row=3, column=0, sticky="ew")
        self.sub1_ctz_label = CTkLabel(self.sub1_ctz_frame, text="Citizenship", font=("Inter", 13))
        self.sub1_ctz_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub1_ctz_var = StringVar(value="filipino")
        self.sub1_ctz_filipino = CTkRadioButton(self.sub1_ctz_frame, text="Filipino", value="filipino", font=("Inter", 13), variable=self.sub1_ctz_var)
        self.sub1_ctz_filipino.grid(row=1, column=0, padx=(20, 5), pady=(0, 20), sticky="nw")
        self.sub1_ctz_foreign = CTkRadioButton(self.sub1_ctz_frame, text="Foreign National", value="foreign", font=("Inter", 13), variable=self.sub1_ctz_var)
        self.sub1_ctz_foreign.grid(row=1, column=1, padx=(0, 20), pady=(0, 20), sticky="nw")

        # Dependent Declaration
        self.sub2 = CTkFrame(self, fg_color="transparent")
        self.sub2.grid(row=3, column=0, pady=(20, 0), sticky="ew")
        self.sub2.grid_columnconfigure(0, weight=1)
        self.sub2_label = CTkLabel(self.sub2, text="Declaration of Dependent", font=("Inter", 13))
        self.sub2_label.grid(row=0, column=0, sticky="nw")

        # Dependent Name
        self.sub2_frame = CTkFrame(self.sub2, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_frame.grid(row=1, column=0, pady=(5, 0), sticky="ew")
        self.sub2_name_label = CTkLabel(self.sub2_frame, text="Member Name", font=("Inter", 13))
        self.sub2_name_label.grid(row=0, column=0, padx="20px", pady=(10, 5), sticky="nw")
        self.sub2_lastname = CTkEntry(self.sub2_frame, placeholder_text="Last Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_lastname.grid(row=1, column=0, padx=(20, 0), pady=(0, 10), sticky="ew")
        self.sub2_firstname = CTkEntry(self.sub2_frame, placeholder_text="First Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_firstname.grid(row=1, column=1, padx="5px", pady=(0, 10), sticky="ew")
        self.sub2_middlename = CTkEntry(self.sub2_frame, placeholder_text="Middle Name", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_middlename.grid(row=1, column=2, padx=(0, 20), pady=(0, 10), sticky="ew")
        self.sub2_bday = CTkEntry(self.sub2_frame, placeholder_text="Birthday (DD/MM/YYYY)", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_bday.grid(row=2, column=0, padx=(20, 0), pady=(0, 20), sticky="ew")
        self.sub2_relationship = CTkEntry(self.sub2_frame, placeholder_text="Relationship with Dependent", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_relationship.grid(row=2, column=1, padx="5px", pady=(0, 20), sticky="ew")
        self.sub2_citizenship = CTkEntry(self.sub2_frame, placeholder_text="Citizenship", font=("Inter", 13), height=40, corner_radius=10, border_width=1, border_color="#000000")
        self.sub2_citizenship.grid(row=2, column=2, padx=(0, 20), pady=(0, 20), sticky="ew")
        self.sub2_frame.grid_columnconfigure(0, weight=1)
        self.sub2_frame.grid_columnconfigure(1, weight=1)
        self.sub2_frame.grid_columnconfigure(2, weight=1)

        # Button
        self.button = CTkButton(self, text="Encrypt input and send to server", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000", command=self.getValues)
        self.button.grid(row=4, column=0, pady="20px", sticky="ew")

        # Textarea
        self.visual = Visual(self, label="Encrypted Input", value=desc, time="0.0002", border_width=1, border_color="#000000", corner_radius=10)
        self.visual.grid(row=5, column=0, sticky="ew")

    def encryptInput(self):
        pass

    def getValues(self):
        self.input_values = {
            'last_name': self.sub1_lastname.get().lower(),
            'first_name': self.sub1_firstname.get().lower(),
            'middle_name': self.sub1_middlename.get().lower(),
            'birthday': self.sub1_bday.get().lower(),
            'birthplace': self.sub1_placeofbrith.get().lower(),
            'income': self.sub1_income.get().lower(),
            'sex': self.sub1_sex_var.get().lower(),
            'civil': self.sub1_cs_var.get().lower(),
            'citizenship': self.sub1_ctz_var.get().lower(),
            'dep_last_name': self.sub2_lastname.get().lower(),
            'dep_first_name': self.sub2_firstname.get().lower(),
            'dep_middle_name': self.sub2_middlename.get().lower(),
            'dep_bday': self.sub2_bday.get().lower(),
            'dep_relationship': self.sub2_relationship.get().lower(),
            'dep_citizenship': self.sub2_citizenship.get().lower()
        }
        
        global HE_client
        test = HE_client.encrypt_data(self.input_values)

class Step1(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label
        labelText = "Step 1: Key Generation"
        self.label = CTkLabel(master=self, text=labelText, font=("Inter", 16))
        self.label.grid(row=0, column=0, pady=(20, 20), sticky="nw")

        desc = "The private key is generated by the client. It is used to encrypt and decrypt the data and shall never be shared with any other party. The public key is used by the server to process encrypted data. It is therefore transmitted to the server for further processing as well."
        self.desc = CTkLabel(master=self, text=desc, font=("Inter", 13), wraplength=900, justify="left")
        self.desc.grid(row=1, column=0, sticky="nw")

        # Button
        self.bgvbutton = CTkButton(self, text="Generate BGV keys and send to server", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000", command=self.generateBGVKeys)
        self.bgvbutton.grid(row=2, column=0, pady=(20, 0), sticky="ew")

        # Button
        self.bfvbutton = CTkButton(self, text="Generate BFV keys and send to server", font=("Inter", 13), height=35, corner_radius=10, border_width=1, fg_color="transparent", border_color="#000000", command=self.generateBFVKeys)
        self.bfvbutton.grid(row=3, column=0, pady=(10, 0), sticky="ew")
        
    """ GENERATION FUNCTIONS """
    def generateBGVKeys(self):
        global HE_client

        # Recording time from generation to sending to server
        start_time = time.time()
        key = HE_client.generate_context('BGV')

        HE_client.send_context_to_server()
        end_time = time.time()
        execution_time = end_time - start_time

        # Textarea
        self.visual = Visual(self, label="Public Key", value=key[:1000], time=f"{execution_time:.6f}", border_width=1, border_color="#000000", corner_radius=10)
        self.visual.grid(row=2, column=0, pady=(20, 0), sticky="ew")

        # Hide button
        self.hideButton(self.bgvbutton)
        self.hideButton(self.bfvbutton)

    def generateBFVKeys(self):
        global HE_client

        # Recording time from generation to sending to server
        start_time = time.time()
        key = HE_client.generate_context('BFV')

        HE_client.send_context_to_server()
        end_time = time.time()
        execution_time = end_time - start_time

        # Textarea
        self.visual = Visual(self, label="Public Key", value=key[:1000], time=f"{execution_time:.6f}", border_width=1, border_color="#000000", corner_radius=10)
        self.visual.grid(row=2, column=0, pady=(20, 0), sticky="ew")

        # Hide button
        self.hideButton(self.bgvbutton)
        self.hideButton(self.bfvbutton)

    """ MISC FUNCTIONS """
    def hideButton(self, button):
        if button.winfo_viewable():
            button.grid_forget()

class Container(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Label
        labelText = "An Experimental Model for an Encrypted Database Using\nSomewhat Homomorphic Encryption"
        self.label = CTkLabel(master=self, text=labelText, font=("Inter", 22))
        self.label.grid(row=0, column=0, pady=(50, 30))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Step 1
        self.step1 = Step1(master=self, fg_color="transparent")
        self.step1.grid(row=1, column=0)

        # Step 2
        self.step2 = Step2(master=self, fg_color="transparent")
        self.step2.grid(row=2, column=0)

        # Step 3
        self.step3 = Step3(master=self, fg_color="transparent")
        self.step3.grid(row=3, column=0)

        # Step 4
        self.step4 = Step4(master=self, fg_color="transparent")
        self.step4.grid(row=4, pady=(0, 60), column=0)

""" MAIN APPLICATION """
class App(CTk):
    def __init__(self):
        super().__init__()

        # Window Properties
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self._state_before_windows_set_titlebar_color = 'zoomed'
        self.title("SHE Demo")

        self.container = Container(master=self, width=self.w, height=self.h, corner_radius=0, fg_color="transparent")
        self.container.grid(row=0, column=0, sticky="nsew")

app = App()
app.mainloop()
