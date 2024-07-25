from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import pandas as pd
import os
import textstat

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# Load positive and negative words from files
def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return set(file.read().split())

positive_words = load_words('positive-words.txt')
negative_words = load_words('negative-words.txt')

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
    
    blob = TextBlob(text)
    
    # Compute variables
    positive_score = sum(1 for word in blob.words if word.lower() in positive_words)
    negative_score = sum(1 for word in blob.words if word.lower() in negative_words)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    sentences = sent_tokenize(text)
    avg_sentence_length = sum(len(word_tokenize(sent)) for sent in sentences) / len(sentences)
    complex_words = sum(1 for word in blob.words if len(word) > 2 and word.lower() not in stop_words)
    percentage_complex_words = complex_words / len(blob.words)
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    avg_words_per_sentence = len(blob.words) / len(sentences)
    word_count = len(blob.words)
    syllable_per_word = sum(textstat.syllable_count(word) for word in blob.words) / len(blob.words)
    personal_pronouns = sum(1 for word in blob.words if word.lower() in ['i', 'we', 'me', 'us', 'my', 'our'])
    avg_word_length = sum(len(word) for word in blob.words) / len(blob.words)
    
    return {
        "POSITIVE SCORE": positive_score,
        "NEGATIVE SCORE": negative_score,
        "POLARITY SCORE": polarity_score,
        "SUBJECTIVITY SCORE": subjectivity_score,
        "AVG SENTENCE LENGTH": avg_sentence_length,
        "PERCENTAGE OF COMPLEX WORDS": percentage_complex_words,
        "FOG INDEX": fog_index,
        "AVG NUMBER OF WORDS PER SENTENCE": avg_words_per_sentence,
        "COMPLEX WORD COUNT": complex_words,
        "WORD COUNT": word_count,
        "SYLLABLE PER WORD": syllable_per_word,
        "PERSONAL PRONOUNS": personal_pronouns,
        "AVG WORD LENGTH": avg_word_length
    }

# Load the input data
df = pd.read_excel('Input.xlsx')

data = []
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    file_path = f'{url_id}.txt'
    if os.path.exists(file_path):
        analysis = analyze_text(file_path)
        analysis["URL_ID"] = url_id  # Add URL_ID to analysis results
        analysis["URL"] = url  # Add URL to analysis results
        data.append(analysis)

# Ensure URL_ID and URL are the first columns
output_df = pd.DataFrame(data)
cols = ["URL_ID", "URL"] + [col for col in output_df.columns if col not in ["URL_ID", "URL"]]
output_df = output_df[cols]

# Save the output data
output_df.to_excel('Output_Data.xlsx', index=False)