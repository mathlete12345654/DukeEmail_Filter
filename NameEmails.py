import pandas as pd
from csv_filter import Name_Emails

# In line below, replace it with name of obtained csv
df = pd.read_csv('new_emails.csv')
Converted_Emails = df["Email Address (mail)"].dropna().to_frame("Email")
Name_Emails = pd.DataFrame(Name_Emails, columns=["Email"])

AllEmails = (pd.concat([Name_Emails, Converted_Emails], ignore_index=True).reset_index(drop=True))
AllEmails = AllEmails.drop_duplicates()
AllEmails.to_csv("NameEmails.csv", index=False, header=False)
