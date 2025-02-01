# Duke-Email-Filters
Duke Student Organizations: do you have a raw subscriber list
that contains both netID and name emails, where some instances refer to the same person? Then this project may help, as it will 
take the netIDs and convert them to name emails while removing duplicates.

This is done with two python scripts: csv_filter is where one inputs their raw 
csv file containing the emails and other things. Examples include
imports from Monkey Mailchimp. This then returns NetIDs.csv,
which csv_filter.py has comments on what to do with it.

NameEmails.py is where one inputs the new name emails, and gives the final product.
