# Book Bot

Book Bot is a Python project developed as part of the [Boot.dev](https://www.boot.dev) programming curriculum.

It analyses text files containing books and produces statistics about their contents.

## Features

- Counts the total number of words in a book.
- Counts the frequency of individual characters.
- Sorts characters by frequency, from most common to least common.
- Displays character statistics in a readable report.

## Requirements

- Python 3
- Git (if cloning the repository)

No external Python packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alexhilbert/bookbot.git
```

### 2. Enter the project directory

```bash
cd bookbot
```

### 3. Run Book Bot

Pass the path to a text file as a command-line argument:

```bash
python3 main.py books/frankenstein.txt
```

You can also analyse the other included books:

```bash
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
```

## Example Output

The program displays a report containing the total word count and character frequencies, ordered from most frequent to least frequent.

## Project Structure

- `main.py` – Main program and command-line interface.
- `stats.py` – Functions for counting and sorting words and characters.
- `books/` – Text files used for analysis.

## Learning Objectives

This project provided practical experience with:

- Python functions and modules.
- Dictionaries and lists.
- File handling.
- Command-line arguments.
- Sorting and working with data.
- Git and version control.