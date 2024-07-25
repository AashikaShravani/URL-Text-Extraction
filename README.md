# URL-Text-Extraction 
URL text extraction involves retrieving and extracting text from a webpage. It starts with sending an HTTP GET request to fetch the webpage's HTML content. 
This content is parsed to locate and extract text nodes, removing unnecessary elements like scripts and styles. Tools like `BeautifulSoup` in Python are commonly used.

# Procedures
* Run `DataExtraction.py` under Text Extraction Directory.
  - It extracts the text from the URL and creates a text document in the given dataset `Input.xlsx`.
* Run `TextAnalysis.py`
  - It returns an `Output_Data.xlsx`
  - It Generates various values like `POSITIVE SCORE`, `NEGATIVE SCORE`, `POLARITY SCORE`, `SUBJECTIVITY SCORE`, `AVG SENTENCE LENGTH`, `AVG WORD LENGTH`, `PERCENTAGE OF COMPLEX WORDS`, `FOG INDEX`, `AVG NUMBER OF WORDS PER SENTENCE`, `COMPLEX WORD COUNT`, `WORD COUNT`, `SYLLABLE PER WORD`, `PERSONAL PRONOUNS`.
  
