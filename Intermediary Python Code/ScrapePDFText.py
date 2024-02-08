import PyPDF2
import re

def extract_text_from_pdf(pdf_file: str) -> [str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf,strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text #entire list of pdf

def list_creation(startword,endword,fulltext):
    # Use regular expressions to find the indices of the words
    matches = re.finditer(startword, fulltext)

    # Extract the text between the two indices for each occurrence
    results = []

    for match in matches:
        start = match.end()
        end_match = re.search(endword, fulltext[start:])
        if end_match is not None:
            end = start + end_match.start()
            result = fulltext[start:end].strip()
            results.append(result)

    return results

if __name__ == '__main__':

    extracted_text = extract_text_from_pdf('NALPDirectory2018.pdf')
    for text in extracted_text: #each line in the pdf
        #print(text)
        import re
        import pandas as pd

    #turn list of pdf to string
    text = ' '.join(extracted_text)

    # Organizational Narrative text
    word1 = 'Organization Narrative'
    word2 = 'NALP is committed'

    narratives = list_creation(word1, word2, text)
    narrative = []
    for x in narratives:
        narrative.append(x)


    #General Practice Areas text
    word3 = 'General Practice Areas' #after
    word4 = 'HIRING & RECRUITMENT' #2019 and 2018
    #word4 = "Diversity & Inclusion" #2021 and 2020

    generalPractices = list_creation(word3, word4, text)
    generalPractice = []
    for y in generalPractices:
        #print(y)
        generalPractice.append(y)

    #firm
    word11 = 'Veteran' #after
    word12 = 'Basic Information' #before

    firms = list_creation(word11, word12, text)
    firm = []

    # Firm RegEx, firm websites in parentheses
    for z in firms:
        try:
            match = re.findall('\((www[A-Za-z\.-]+)\)', z)
            # if match empty try
            if not match:
                match = re.findall('\(([A-Za-z\.-]+)\)', z)
                # if empty still try
                if not match:
                    match = re.findall('\(([A-Za-z\.-]+)\)', z)
                    # if empty still try
                    if not match:
                        match = re.findall('\((http://www[A-Za-z\.-]+)/{0,1}\)', z)
                        # if empty still try
                        if not match:
                            match = re.findall('\((http://[A-Za-z\.-]+)/{0,1}\)', z)
                            if not match:
                                match = ["NaN"]
            firm.append(match)
        except IndexError:
            firm.append(["IndexError"])

    # Basic Information
    word8 = 'Basic Information'
    #word9 = '.org'
    #word10 = '.com'
    word9 = "Compensation & Benefits" #2021, 2020, 2019, 2018

    # Use regular expressions to find the indices of the words
    matches = re.finditer(word8, text)

    # Extract the text between the two indices for each occurrence
    results = []
    for match in matches:
        start = match.end()
        end_match = re.search(word9, text[start:]) #or word10
        if end_match is not None:
            end = start + end_match.start()
            result = text[start:end].strip()
            results.append(result)

    # Use RegEx to get just the city
    city = []
    for result in results:
        match = re.search('[A-Za-z]+, [A-Za-z]{2}\s[0-9]{5}-{0,1}[0-9]{0,4}', result) #added {2}, got rid of +
        if match:
            city.append(match.group())
        else:
            match = "NaN"
            city.append(match)

    #create dataframe, use zip files for multiples lists. Get lists of all of this.
    df = pd.DataFrame(list(zip(firm, city, generalPractice, narrative)), columns=['Firm', 'City','General_Practice','Organizational_Narrative'])
    df["Firm"] = df.Firm.apply(lambda x: x[0])
    df.to_csv("NALP_2018_testing328.csv")
