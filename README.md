# OpenAI API Book Summarizer

![Project Logo](cover.png)

Welcome to the OpenAI API Book Summarizer project! This tool utilizes the power of the OpenAI API to provide insightful summaries of books. Whether you're a student looking for a quick overview or a busy professional trying to grasp the key points of a book on the go, this tool is designed to make your reading experience more efficient.

## Features

- **Automatic Summarization:** Leverage the OpenAI API to generate concise and informative summaries of entire books.
- **Customizable Settings:** Tailor the summarization process to your preferences using the provided settings and options.
- **Efficient Processing:** Utilizes advanced natural language processing techniques to ensure accurate and relevant summaries.

## The Code

### Cleaner

`cleaner.py`

![](https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png | width=100)

![Cleaner Image](cleaner.png width=500x)

### Tokenizer

`tokenizer.py`

![Tokenizer Image](tokenizer.png =500x)

### Summarizer

`summarizer.py`

![Summarizer Image](summarizer.png =500x)

## Getting Started

Follow these simple steps to start using the OpenAI API Book Summarizer:

1. Clone the repository:

```bash
git clone https://github.com/manuelparra1/Book-Summary.git
```

2. Install dependencies:

```bash
requirements.txt
```

3. Run the summarizer:

```bash
python summarizer.py
```

Customize the settings in `summarizer.py` to tailor the summarization process to your needs.

## File Structure

- **`book_chapters_text.zip`:** Archive containing text files for each chapter.
- **`chapter_1.txt to chapter_9.txt`:** Individual text files for each chapter.
- **`cleaner.py`:** Python script for cleaning and preprocessing text data.
- **`summarizer.py`:** Main script for utilizing the OpenAI API for book summarization.
- **`test.ipynb` and `test.py`:** Example notebooks and scripts for testing the functionality.
- **`token_chunks.json`:** JSON file containing token chunks used in the summarization process.
- **`tokenizer.py`:** Tokenization script for breaking down text into tokens.

## Contributing

We welcome contributions from the community! If you have ideas for improvements, bug reports, or want to add new features, please feel free to open an issue or submit a pull request.

## License

- Under Construction -
