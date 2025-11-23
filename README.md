Plagiarism Detector
...................

A Python-based application that compares two text documents to determine their content similarity using the Jaccard Similarity algorithm.

Project Overview
This project analyzes two essays about "The Making of a Villain" to detect potential plagiarism or content similarity:

Essay 1: The Making of a Villain: Idi Amin Dada
Essay 2: The Making of a Villain: Adolf Hitler

The application processes text documents, removes stop words, and calculates a similarity percentage based on shared vocabulary and content overlap.

Features
........

Core Functionality
- Text Processing: Converts text to lowercase, removes punctuation, filters stop words
- Word Search: Search for specific words and see their frequency in each essay
- Common Words Analysis: Identifies words that appear in both essays
- Plagiarism Detection: Calculates similarity percentage using Jaccard Similarity formula
- Report Generation: Option to save detailed similarity reports

Quality Features
Comprehensive error handling and validation
Clear, user-friendly interface with progress indicators
Detailed logging and documentation
Cross-platform compatibility (Windows, Linux, macOS)
Professional output formatting

.......................................................................................................................

Getting Started

Prerequisites I used

Python 3.12.3 installed on my system
Bash shell (Ubuntu WSL on Windows)
Two text files to compare (essay1.txt, essay2.txt)

.......................................................................................................................

Usage Guide

Running the Application
In Ubuntu WSL, run
python3 plagiarism-detector.py

The application will guide you through these steps:

1.File Loading: Automatically reads both essays from the essays/ directory
2.Text Processing: Cleans and processes the text
3.Word Search (Optional): Search for specific words to see their frequency
4.Common Words Report: Displays all words found in both essays
5.Similarity Calculation: Shows the plagiarism percentage
6.Save Report (Optional): Option to save the report to reports/similarity_report.txt



Technical Details
Jaccard Similarity
The plagiarism percentage is calculated using the Jaccard Similarity Index:
Similarity = (Size of Intersection / Size of Union) × 100

Where:
Intersection: Unique words that appear in BOTH essays
Union: ALL unique words from BOTH essays combined

The application filters out common English words that don't contribute to content similarity.

.......................................................................................................................

Project Structure
plagiarism-detector/
____setup.sh                      # Setup script to create directories
____setup.log                     # Log file documenting setup process
____plagiarism-detector.py        # Main Python application
____README.md                     # This file
____essays/                       # Directory for input essay files
    ____essay1.txt                # First essay (Idi Amin)
    ____essay2.txt                # Second essay (Adolf Hitler)
____reports/                      # Directory for output reports
    ____similarity_report.txt     # Generated similarity report (if saved)

.......................................................................................................................

Features Implemented

Required Features
Text processing function (lowercase, punctuation removal, stop words filtering)
Word search functionality
Common words report
Plagiarism calculation using Jaccard Similarity
Decision making (50%+ threshold for high similarity)
Save report functionality
Bash setup script with logging

Additional Quality Features
Comprehensive error handling
Input validation for all user inputs
File existence and permission checks
Path handling

.......................................................................................................................

Validation & Error Handling

The application includes robust validation:

File Validation
Checks if essay files exist
Verifies file read permissions
Handles empty files gracefully
Validates file paths

Input Validation
Validates user choices (y/n inputs)
Handles invalid word search inputs
Checks data types
Prevents empty inputs

Error Messages
Clear, informative error messages
Helpful suggestions for fixing issues
Graceful error recovery

.......................................................................................................................

Future Enhancements

While the current implementation meets all assignment requirements for comparing two essays, potential future improvements could include:

Multiple Essay Comparison: Extend functionality to compare 3 or more essays simultaneously
Batch Processing: Compare multiple pairs of essays in one run
GUI Interface: Create a graphical user interface for easier use
Database Integration: Store comparison results for historical analysis
PDF Support: Process PDF files directly without conversion
Web Interface: Deploy as a web application for remote access
Statistical Analysis: Provide more detailed statistical breakdowns

.......................................................................................................................