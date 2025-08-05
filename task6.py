#!/bin/bash

# Activate the Windows-style virtual environment
source venv/Scripts/activate

# Run the test suite
python -m pytest task5.py

# Capture the exit code and respond accordingly
if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed!"
    exit 1
fi
