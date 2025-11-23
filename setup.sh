#!/bin/bash
# Script to create the necessary directory structure for the plagiarism detector

echo "Plagiarism Detector - Setup Script"
echo ".................................."
echo "Starting setup process..."
echo ""

echo "Setup started at: $(date)" >> setup.log
echo "........................." >> setup.log

# Creating essays directory to store the essay text files + error handling, obvi
if [ ! -d "essays" ]; then
  mkdir essays
  if [ $? -eq 0 ]; then
    echo "Successfully created 'essays' directory" | tee -a setup.log
  else
    echo "Failed to create 'essays' directory" | tee -a setup.log
    exit 1
    fi
else
  echo "'essays' directory already exists. We're skipping its creation" | tee -a setup.log
fi

# Creating the similarity reports
if [ ! -d "reports" ]; then
  mkdir reports
  if [ $? -eq 0 ]; then
    echo "Successfully created 'reports' directory" | tee -a setup.log
  else
    echo "Failed to create 'reports' directory" | tee -a setup.log
    exit 1
    fi
else
  echo "'reports' directory already exists. We're skipping its creation" | tee -a setup.log
fi

echo "Verifying directory structure..."
echo "................................"

if [ -d "essays" ] && [ -d "reports" ]; then
  echo "Directory structure verified successfully" | tee -a setup.log
  echo ""
  echo "Directory structure:"
  echo "  ./essays/   - To store essay text files"
  echo "  ./reports/  - Ready for similarity reports"
else
  echo "Directory structure verification failed" | tee -a setup.log
  exit 1
fi

# Log completion
echo "" >> setup.log
echo "Setup completed successfully at: $(date)" >> setup.log
echo "........................................" >> setup.log
echo "" >> setup.log

# completion message
echo ""
echo "Setup completed successfully ^_^"
echo "................................"
echo "Next steps:"
echo "1. Place your essay files in the 'essays/' directory"
echo "2. Run the plagiarism detector: python3 plagiarism-detector.py"
echo ""

exit 0
