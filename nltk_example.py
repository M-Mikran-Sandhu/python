import nltk

# --- NLTK Resource Download Function ---
# NLTK relies on data packages (corpora, tokenizers, taggers, etc.).
# This function attempts to download necessary resources if they are not found.
def download_nltk_resources_if_missing():
    """Checks for and downloads NLTK resources if they are missing."""
    required_resources = [
        ('tokenizers/punkt', 'punkt'), # For sentence tokenization
        ('taggers/averaged_perceptron_tagger', 'averaged_perceptron_tagger') # For POS tagging
    ]
    downloaded_any = False
    for resource_path, resource_id in required_resources:
        try:
            nltk.data.find(resource_path)
            print(f"NLTK resource '{resource_id}' already downloaded.")
        except nltk.downloader.DownloadError:
            print(f"NLTK resource '{resource_id}' not found. Attempting to download...")
            try:
                nltk.download(resource_id, quiet=True) # quiet=True suppresses verbose download output
                print(f"Successfully downloaded '{resource_id}'.")
                downloaded_any = True
            except Exception as e:
                print(f"Error downloading '{resource_id}': {e}")
                print("Please try running `nltk.download('{resource_id}')` manually in a Python console.")
        except LookupError: # Can also indicate resource not found
             print(f"NLTK resource '{resource_id}' not found (LookupError). Attempting to download...")
             try:
                nltk.download(resource_id, quiet=True)
                print(f"Successfully downloaded '{resource_id}'.")
                downloaded_any = True
             except Exception as e:
                print(f"Error downloading '{resource_id}': {e}")
                print("Please try running `nltk.download('{resource_id}')` manually in a Python console.")
    
    if downloaded_any:
        print("\nSome NLTK resources were downloaded. You might need to run the script again if downloads occurred mid-execution for them to be fully available.")
    print("--- NLTK Resource Check Complete ---")


def demonstrate_nltk_operations():
    """Demonstrates some basic NLTK operations for NLP."""

    print("\n--- NLTK Demonstration ---")

    # First, ensure necessary resources are available
    download_nltk_resources_if_missing()
    print("\n(If resources were just downloaded, you might need to re-run the script for all examples below to work correctly)")


    sample_text = "Hello! Natural Language Processing with NLTK is interesting. It allows us to work with text data effectively."

    print(f"\nOriginal Text: '{sample_text}'")

    # 1. Sentence Tokenization
    # Splits text into sentences. Requires 'punkt' tokenizer.
    try:
        sentences = nltk.sent_tokenize(sample_text)
        print("\n1. Sentence Tokenization:")
        for i, sentence in enumerate(sentences):
            print(f"  Sentence {i+1}: {sentence}")
    except Exception as e:
        print(f"Error during sentence tokenization (is 'punkt' downloaded?): {e}")

    # 2. Word Tokenization
    # Splits sentences or text into words. Also uses 'punkt'.
    try:
        words = nltk.word_tokenize(sample_text.lower()) # Convert to lowercase for consistency
        print("\n2. Word Tokenization (from original text, lowercased):")
        print(f"  Words: {words}")
    except Exception as e:
        print(f"Error during word tokenization (is 'punkt' downloaded?): {e}")


    # 3. Part-of-Speech (POS) Tagging
    # Assigns a grammatical category (noun, verb, adj, etc.) to each word.
    # Requires 'averaged_perceptron_tagger'.
    # We'll use the first sentence for this example.
    if 'sentences' in locals() and sentences:
        try:
            first_sentence_words = nltk.word_tokenize(sentences[0])
            pos_tags = nltk.pos_tag(first_sentence_words)
            print("\n3. Part-of-Speech (POS) Tagging (for the first sentence):")
            print(f"  POS Tags: {pos_tags}")
            # You can find explanations of POS tags using: nltk.help.upenn_tagset('NNP')
        except Exception as e:
            print(f"Error during POS tagging (is 'averaged_perceptron_tagger' downloaded?): {e}")
    else:
        print("\nSkipping POS tagging as sentence tokenization might have failed.")

    # 4. Stemming (using Porter Stemmer)
    # Reduces words to their root or base form.
    # Example: "running" -> "run", "cats" -> "cat"
    try:
        porter = nltk.PorterStemmer()
        stemmed_words = [porter.stem(word) for word in words] # using 'words' from word tokenization
        print("\n4. Stemming (Porter Stemmer on tokenized words):")
        print(f"  Original Words: {words}")
        print(f"  Stemmed Words:  {stemmed_words}")
    except Exception as e:
        print(f"Error during stemming: {e}")
        
    # 5. Lemmatization (using WordNet Lemmatizer - often preferred over stemming)
    # Reduces words to their dictionary form (lemma). Requires 'wordnet' and 'omw-1.4' usually.
    # We'll try to download these as well.
    try:
        nltk.data.find('corpora/wordnet')
        nltk.data.find('corpora/omw-1.4') # Open Multilingual Wordnet
    except (nltk.downloader.DownloadError, LookupError):
        print("\n'wordnet' or 'omw-1.4' lemmatizer resource not found. Attempting to download...")
        try:
            nltk.download('wordnet', quiet=True)
            nltk.download('omw-1.4', quiet=True) # For better lemmatization across languages
            print("Successfully downloaded 'wordnet' and 'omw-1.4'. You may need to re-run the script.")
        except Exception as e:
            print(f"Error downloading WordNet/OMW: {e}")
            print("Skipping lemmatization.")
            
    try:
        lemmatizer = nltk.WordNetLemmatizer()
        # POS tagging helps lemmatization, but for simplicity, we'll lemmatize directly here.
        # A more advanced approach would map NLTK POS tags to WordNet POS tags.
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        print("\n5. Lemmatization (WordNet Lemmatizer on tokenized words):")
        print(f"  Original Words:   {words}")
        print(f"  Lemmatized Words: {lemmatized_words}")
    except LookupError: # If wordnet/omw-1.4 still not found after download attempt
        print("Lemmatization skipped as 'wordnet' or 'omw-1.4' resources are not available.")
    except Exception as e:
        print(f"Error during lemmatization: {e}")


    print("\n--- NLTK Demonstration End ---")
    print("Note: NLTK may require downloading data packages (corpora, models).")
    print("The script attempts to download 'punkt', 'averaged_perceptron_tagger', 'wordnet', and 'omw-1.4'.")
    print("If you encounter issues, you might need to run `nltk.download()` interactively in a Python console.")

if __name__ == "__main__":
    demonstrate_nltk_operations()
