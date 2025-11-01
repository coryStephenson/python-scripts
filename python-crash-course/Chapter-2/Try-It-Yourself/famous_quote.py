import sys
import io

# Create a StringIO object to capture the output
zen_output = io.StringIO()

# Redirect stdout to the StringIO object
sys.stdout = zen_output

# Import the 'this' module to trigger the Zen of Python output
import this

# Restore original stdout
sys.stdout = sys.__stdout__

# Get the captured output as a string
zen_of_python = zen_output.getvalue()

# Print the captured output (optional, for verification)
print(zen_of_python)
