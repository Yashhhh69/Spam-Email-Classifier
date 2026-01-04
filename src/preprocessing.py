# 2. PREPROCESSING (The "Cleaning" Stage)
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation (like !, ?, .)
    text = "".join([char for char in text if char not in string.punctuation])
    # Remove stopwords
    text = " ".join([word for word in text.split() if word not in stop_words])
    return text

print("Cleaning data...")
df['cleaned_message'] = df['message'].apply(clean_text)
