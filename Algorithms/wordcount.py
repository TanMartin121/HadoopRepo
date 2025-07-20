import pandas as pd
from collections import Counter
import re

def count_words_from_all_columns(csv_file):
    try:
        # Load the CSV
        df = pd.read_csv(csv_file)

        # Flatten all values in the DataFrame to a single text string
        text_data = " ".join(df.astype(str).fillna("").values.flatten()).lower()

        # Tokenize: extract only alphanumeric words
        words = re.findall(r'\b\w+\b', text_data)

        # Count word frequencies
        return Counter(words)

    except Exception as e:
        print(f"Error: {e}")
        return Counter()

def save_word_counts_to_file(counter, output_file):
    sorted_counts = counter.most_common()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("word\tcount\n")
        for word, count in sorted_counts:
            f.write(f"{word}\t{count}\n")

# Example usage
if __name__ == "__main__":
    # change csv file name here
    input_csv = "sample.csv"      # Path to your CSV
    output_file = "output.txt"    # Output result file

    word_counts = count_words_from_all_columns(input_csv)
    save_word_counts_to_file(word_counts, output_file)
    print(f"Word counts saved to {output_file}")
