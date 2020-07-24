# import os
# import subprocess
# from pdf2docx.main import parse


class Parse:
    lineList = []
    sentenceList = []
    temp = ""
    temp2 = ""

    def __init__(self, filepath):

        text_file = open(filepath, 'r')
        for line in text_file:
            self.lineList.append(line)

        # Finds title

    def find_title(self):
        lineList = self.lineList[:]
        for i in range(0, len(lineList)):
            if lineList[i] == "Program Title:\n":
                print(lineList[i])
                print(lineList[i + 1])
                break

        # finds due dates

    def find_due_dates(self):
        lineList = self.lineList[:]
        for i in range(0, len(lineList)):
            if lineList[i] == "C. Due Dates\n":
                i += 1

                while lineList[i] != "Proposal Review Information Criteria\n":
                    print(lineList[i])
                    i += 1
                return

    def find_program_description(self, length):
        temp = ""
        temp2 = ""
        lineList = self.lineList[:]
        sentenceList = self.sentenceList[:]
        for i in range(0, len(lineList)):
            if lineList[i] == "II. PROGRAM DESCRIPTION\n":
                sentenceList = lineList
                del sentenceList[0:i]

                for x in range(0, len(sentenceList)):
                    temp = temp + sentenceList[x]

                for x in range(0, length):
                    temp2 = temp.find('.')
                    sentenceList[x] = temp[:temp2]
                    temp = temp[temp2 + 1:len(temp)]

                temp = ""
                for x in range(0, length):
                    temp = temp + sentenceList[x] + "."

                print(temp)
                return

    def find_congnizant_program_officers(self):
        lineList = self.lineList[:]
        for i in range(0, len(lineList)):
            if lineList[i] == "Cognizant Program Officer(s):\n":
                while lineList[i] != "Applicable Catalog of Federal Domestic Assistance (CFDA) Number(s):\n":
                    print(lineList[i])
                    i += 1
                return
