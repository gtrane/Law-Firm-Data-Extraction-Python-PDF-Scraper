# Law Firm Data Extraction: Python PDF Scraper
Under the leadership of Dr. Eleazar Welbourne, I utilized PyCharm and Jupyter Notebooks to convert 13,000 pages of PDFs into a structured dataframe, scraping national law firm general practice information over a four-year period (2018-2021) for 401 law firms. The final file 'FinalNALP2018To2021.xlsx' contains 33,000 rows of data for the firms, the final data collection document before passing this data to Dr. Welbourne and her team.

I used the PyPDF2 library to scrape tables from the PDFs. 'ScrapePDFText.py' details this code. Utilized regular expressions with the re library to obtain general practice area information through the use of pattern recognition.

'MainFileNALP.ipynb' details the code used to scrape a general practice table into multiple columns of data. 'NotAllFives_Fours-numbers.ipynb' & 'NotAllFives_Fours-ScrapingPracticeAreas.ipynb' handled scraping when missing/null data was involved.

This project involved a self-start mentality and problem solving skills in order to troubleshoot the pattern recognition required to successfully scrape the data and thereafter disaggregate it into multiple new columns. I relied on my critical thinking skills and curiosity to achieve a desired outcome.
