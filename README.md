# Law Firm Data Extraction: Python PDF Scraper
Utilized Pycharm and Jupyter Notebooks to convert over 12,000 pages of PDFs into a structured dataframe, scraping national law firm general practice information over a four-year period (2018-2021) for 401 law firms. 

The PyPDF2 library was used to scrape text from the PDFs, 'ScrapePDFText.py' details this code. I then used Regular Expressions to obtain the correct table information with pattern recognition.

'MainFileNALP.ipynb' details the code used to scrape a general practice table into multiple columns of data. 'NotAllFives_Fours-numbers.ipynb' & 'NotAllFives_Fours-ScrapingPracticeAreas.ipynb' handled scraping when missing/null data was involved.

The final file 'FinalNALP2018To2021.xlsx' contains 33,000 rows of data for the 401 firms.
