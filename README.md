# PDF-Scraper
Converted over 10,000 pages of PDFs into a data frame by scraping law firm general practice information from a four-year period (2018-2021) for 401 law firms. 

ScrapePDFText.py details the code used to scrape the actual text from all of the PDFs. I then used Regular Expressions to obtain the correct table information with pattern recognition.
MainFileNALP.ipynb details the code to scrape a general practice table into multiple columns of data. NotAllFives_Fours-numbers.ipynb & NotAllFives_Fours-ScrapingPracticeAreas.ipynb handled scraping with missing data, that would be followed by manual checks of these scraped columns.

The final file (FinalNALP2018To2021.xlsx) contains 33,000 rows of data for the 401 firms. 
