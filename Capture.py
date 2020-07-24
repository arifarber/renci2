from Parse import Parse


# List of fields captured
class Capture:
    rfp = Parse(r'C:\Users\arile\Documents\renciTextExamples\rfpAI.txt')
    rfp.find_title()
    rfp.find_due_dates()
    rfp.find_program_description(4)  # argument is the number of sentences of description
    rfp.find_congnizant_program_officers()
