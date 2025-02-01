import pandas as pd

# subscriber.csv is the given data, change the name if necessary
# "email" may not be the actual column, just replace it with whatever column contains the emails
Emails = pd.read_csv('subscriber.csv')["Email Address"]
NetID_Emails = []
Name_Emails = []

for email in Emails:
    local, domain = email.split('@')[0], email.split('@')[1]
    if "." in local or domain != "duke.edu":
        Name_Emails.append(email)
    else:
        NetID_Emails.append(local)
NetIDs = pd.DataFrame(NetID_Emails, columns=["NetID"])
NetIDs.to_csv('NetID.csv', index=False)

# You now have NetID.csv in your downloads (or here) if you declined that.
# Now go to https://idm.oit.duke.edu/tools/ldap (will need to log in)
# Under 'select desired attributes' select 'Email Address (mail)'
# Import NetID.csv under "Choose File to Upload"
# Click submit csv. This should return a new csv which we input in NameEmails.py
