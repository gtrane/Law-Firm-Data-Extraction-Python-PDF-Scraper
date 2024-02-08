# Law Firm Data Extraction: Python PDF Scraper
Under the leadership of Dr. Eleazar Welbourne, I utilized PyCharm and Jupyter Notebooks to convert 12,659 PDF pages into a structured dataframe, scraping national law firm general practice information over a four-year period (2018-2021) for 401 law firms. The final file **_'FinalNALP2018To2021.xlsx'_** contains 33,000 rows of data for 401 firms. This completed the data collection process for Dr. Welbourne and her team. We were interested in a subset of data in the PDFs, sourced from nalpdirectory.com - each firm's General Practice Areas, number of partners, number of counsel, number of associates, number of entry-level placements last year, number of non-traditional track/staff attorneys, and their organizational narrative. 

In order to scrape the data into a structured dataframe, I used PyPDF2 and re python libraries. _**'ScrapePDFText.py'**_ details this code.
**_'MainFileNALP.ipynb'_** details my code to scrape the General Practice table into multiple columns of data. 
**_'NotAllFives_Fours-numbers.ipynb'_** & **_'NotAllFives_Fours-ScrapingPracticeAreas.ipynb'_** handled scraping when missing data was involved.

This project involved a self-start mentality and problem solving skills in order to troubleshoot the pattern recognition required to successfully scrape the data and thereafter disaggregate it into multiple new columns. I relied on my critical thinking skills and curiosity to achieve a desired outcome.
