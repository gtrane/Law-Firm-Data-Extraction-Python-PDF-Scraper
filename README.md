# Law Firm Data Extraction: Python PDF Scraper
Utilized PyCharm and Jupyter Notebooks to convert 13,000 pages of PDFs into a structured dataframe, scraping national law firm general practice information over a four-year period (2018-2021) for 401 law firms. The final file 'FinalNALP2018To2021.xlsx' contains 33,000 rows of data for the firms.

I used the PyPDF2 library to scrape tables from the PDFs. 'ScrapePDFText.py' details this code. Utilized regular expressions with the re library to obtain general practice area information through the use of pattern recognition.

'MainFileNALP.ipynb' details the code used to scrape a general practice table into multiple columns of data. 'NotAllFives_Fours-numbers.ipynb' & 'NotAllFives_Fours-ScrapingPracticeAreas.ipynb' handled scraping when missing/null data was involved.
