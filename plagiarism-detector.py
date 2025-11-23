## #!/usr/bin/env python3
"""Plagiarism Detector Application"""
import os
import string
import sys

# stop words definition
STOP_WORDS = {
	'a', 'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'about','as', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'between', 'under', 'again', 'further', 'then', 'once', 'here','there', 'when', 'where', 'why', 'how', 'all', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only','own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'should', 'now', 'and', 'but', 'or', 'if', 'because', 'until', 'while','this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they','what', 'which', 'who', 'whom', 'whose', 'am', 'has', 'have','had', 'do', 'does', 'did', 'would', 'could', 'should', 'may', 'might', 'must'
}

#text processing
def process_text(text):
	"""1. Converts all text to lowercase for case-insensitive comparison
	2. Removes all punctuation marks
	3. Splits text into individual words
	4. Filters out stop words
	"""
	
	# Error handling
	if not isinstance(text, str):
		print("Error: Input must be a string")
		return []
	
	text_lower = text.lower()
	
	#remove punctuation
	translator = str.maketrans('', '', string.punctuation)
	text_no_punct = text_lower.translate(translator)
	
	words = text_no_punct.split()
	
	non_stop_words = [word for word in words if word not in STOP_WORDS]
	return non_stop_words

# search words
def search_words(word, essay1_text, essay2_text):

	if not isinstance(word, str) or not word.strip():
		print("Error: Please provide a valid word to search")
		return (0, 0)
	
	search_word = word.lower().strip()
	
	essay1_words = process_text(essay1_text)
	essay2_words = process_text(essay2_text)
		
	count_essay1 = essay1_words.count(search_word)
	count_essay2 = essay2_words.count(search_word)
	return (count_essay1, count_essay2)

# find common words
def find_common_words(words_list1, words_list2):
	"""Identifies words that appear in both essays."""

	if not isinstance(words_list1, list) or not isinstance(words_list2, list):
		print("Error: Both inputs must be lists")
		return set()

	set1 = set(words_list1)
	set2 = set(words_list2)

	common = set1.intersection(set2)
		
	return common

# calculate plagiarism
def calculate_plagiarism(words_list1, words_list2):
	"""Calculates plagiarism percentage using Jaccard Similarity formula.
	Jaccard Similarity Formula: Similarity = (Size of Intersection / Size of Union) × 100"""

	if not isinstance(words_list1, list) or not isinstance(words_list2, list):
		print("Error: Both inputs must be lists")
		return (0.0, set(), set())

	set_essay1 = set(words_list1)
	set_essay2 = set(words_list2)

	intersection = set_essay1.intersection(set_essay2)

	union = set_essay1.union(set_essay2)
		
	# calculate Jaccard Similarity percentage
	if len(union) == 0:
		plagiarism_percentage = 0.0
	else:
		plagiarism_percentage = (len(intersection) / len(union)) * 100 
	return (plagiarism_percentage, intersection, union)

# save report
def save_report(common_words, percentage):
	"""Saves the similarity report to a text file in the reports/ directory."""
	try:
		# Error handling, obviously
		reports_dir = "reports"
		if not os.path.exists(reports_dir):
			os.makedirs(reports_dir)
			print(f"Created '{reports_dir}' directory")
			
		report_path = os.path.join(reports_dir, "similarity_report.txt")
			
		with open(report_path, 'w', encoding='utf-8') as file:
			file.write("...........................\n")
			file.write("PLAGIARISM DETECTION REPORT\n")
			file.write("...........................\n\n")
				
			file.write(f"Similarity Percentage: {percentage:.2f}%\n\n")
				
			file.write(f"Total Common Words: {len(common_words)}\n\n")
				
			file.write("Common Words Found:\n")
			file.write("...................\n")
				
			sorted_words = sorted(common_words)
				
			for i in range(0, len(sorted_words), 5):
				line_words = sorted_words[i:i+5]
				file.write("  ".join(f"{word:<12}" for word in line_words) + "\n")
			file.write("\n\n")
		print(f"\nReport saved successfully to: {report_path}")

		return True
		
	except Exception as e:
		print(f"\nError saving report: {e}")
		return False

# read file
def read_file(filepath):
	"""Reads a text file and returns its content."""
	try:
		if not os.path.exists(filepath):
			print(f"File '{filepath}' does not exist")
			return None
		
		if not os.path.isfile(filepath):
			print(f"'{filepath}' is not a file")
			return None
		
		with open(filepath, 'r', encoding='utf-8') as file:
			content = file.read()
		
		if not content.strip():
			print(f"File '{filepath}' is empty")
			return ""
		
		return content
		
	except PermissionError:
		print(f"Permission denied to read '{filepath}'")
		return None
	except Exception as e:
		print(f"Error reading file '{filepath}': {e}")
		return None

# main
def main():
	"""It will:
	1. Display welcome message
	2. Read essay files
	3. Process text
	4. Offer word search feature
	5. Find common words
	6. Calculate plagiarism percentage
	7. Display results
	8. Offer to save report"""
		
	# Display header
	print("\n")
	print("...................")
	print("PLAGIARISM DETECTOR")
	print("...................")
	print("\nComparing essays...")

	print("How would you like to provide the essays?")
	print("1. Load from existing files (default)")
	print("2. Paste the essay text manually")

	while True:
		choice = input("Choose option (1 or 2): ").strip()

		if choice in ["", "1"]:
			print("\nLoading essays from files...")
			essay1_path = os.path.join("essays", "essay1.txt")
			essay2_path = os.path.join("essays", "essay2.txt")

			essay1_text = read_file(essay1_path)
			if essay1_text is None:
				print("\nFailed to read essay1.txt. Please ensure:")
				print("1. The file exists in the essays/ directory")
				print("2. The file has read permissions")
				print("3. Run setup.sh first to create directories")
				sys.exit(1)

			essay2_text = read_file(essay2_path)
			if essay2_text is None:
				print("\nFailed to read essay1.txt. Please ensure:")
				print("1. The file exists in the essays/ directory")
				print("2. The file has read permissions")
				print("3. Run setup.sh first to create directories")
				sys.exit(1)

			break

		elif choice == "2":
    print("\nPaste Essay 1. When done, type a single line with 'END':\n")
    lines1 = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines1.append(line)
    essay1_text = "\n".join(lines1)

    print("\nPaste Essay 2. When done, type 'END':\n")
    lines2 = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines2.append(line)
    essay2_text = "\n".join(lines2)

    # Ensure essays directory exists
    essays_dir = "essays"
    if not os.path.exists(essays_dir):
        os.makedirs(essays_dir)
        print(f"\nCreated '{essays_dir}' directory")

    # Save Essay 1
    essay1_path = os.path.join(essays_dir, "essay1.txt")
    with open(essay1_path, "w", encoding="utf-8") as f:
        f.write(essay1_text)
    print(f"\nSaved Essay 1 to {essay1_path}")

    # Save Essay 2
    essay2_path = os.path.join(essays_dir, "essay2.txt")
    with open(essay2_path, "w", encoding="utf-8") as f:
        f.write(essay2_text)
    print(f"Saved Essay 2 to {essay2_path}")

    break

		else:
			print("Invalid choice. Enter 1 or 2.")

	print("Essays loaded successfully ^_^\n")
	print("Processing text...")
	essay1_clean = process_text(essay1_text)
	essay2_clean = process_text(essay2_text)
		
	print(f"Essay 1: {len(essay1_clean)} meaningful words found")
	print(f"Essay 2: {len(essay2_clean)} meaningful words found\n")
	
	print("Word Search Feature")
	print("...................")

	while True:
		search_choice = input("\nWould you like to search for a specific word? (y/n): ").strip().lower()
		if search_choice not in ['y', 'n', 'yes', 'no']:
			print("Invalid input. Please enter 'y' for yes or 'n' for no.")
			continue
			
		if search_choice in ['y', 'yes']:
			search_word = input("Enter the word to search: ").strip()
			if not search_word:
				print("Please enter a valid word")
				continue
			count1, count2 = search_words(search_word, essay1_text, essay2_text)
				
			print(f"\nSearch Results for '{search_word}':")
			print(f"Essay 1: {count1} occurrence(s)")
			print(f"Essay 2: {count2} occurrence(s)")
		else:
			print("On to the next step...")
		break
		
	print("\n")
	print("Common Words Analysis")
	print(".....................")
		
	common_words = find_common_words(essay1_clean, essay2_clean)
		
	print(f"\nTotal common words found: {len(common_words)}")
		
	if len(common_words) > 0:
		print("\nCommon words (sorted alphabetically):")
		sorted_common = sorted(common_words)
		#columns just so we can read better
		for i in range(0, len(sorted_common), 5):
			line_words = sorted_common[i:i+5]
			print("  " + "  ".join(f"{word:<12}" for word in line_words))
	else:
		print("No common words found between the essays.")
		
	print("\n")
	print("Plagiarism Calculation")
	print("......................")
		
	percentage, intersection, union = calculate_plagiarism(essay1_clean, essay2_clean)
		
	print(f"\nJaccard Similarity Calculation:")
	print(f"Intersection (common unique words): {len(intersection)}")
	print(f"Union (all unique words): {len(union)}")
	print(f"Formula: ({len(intersection)} / {len(union)}) × 100")
	print("\n")
	print(f"Similarity Percentage: {percentage:.2f}%")
	print("..............................")
		
	print("\nInterpretation:")
	if percentage >= 50:
		print(f"HIGH SIMILARITY detected ({percentage:.2f}%)")
		print("The essays show significant content overlap.")
		print("This may indicate potential plagiarism or similar source material.")
	elif percentage >= 25:
		print(f"MODERATE SIMILARITY detected ({percentage:.2f}%)")
		print("The essays share some common themes or vocabulary.")
	else:
		print(f"LOW SIMILARITY detected ({percentage:.2f}%)")
		print("The essays appear to be largely original and distinct.")
		
	print("\n")
	print("Save Report")
	print("...........")
		
	while True:
		save_choice = input("\nWould you like to save this report? (y/n): ").strip().lower()
			
		if save_choice not in ['y', 'n', 'yes', 'no']:
			print("Invalid input. Please enter 'y' for yes or 'n' for no.")
			continue
			
		if save_choice in ['y', 'yes']:
			save_report(common_words, percentage)
		else:
			print("\nReport not saved.")
			break
		
	print("\n")
	print("Analysis Complete ^_^")
	print(".....................")
	print("\nThank you for using the Plagiarism Detector")
	print("\n")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\n\nProgram interrupted by user")
		sys.exit(0)
	except Exception as e:
		print(f"\nUnexpected error occurred: {e}")
		sys.exit(1)
