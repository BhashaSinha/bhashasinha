import random
from datetime import datetime

# List of AI quotes
quotes = [
    "Artificial intelligence is the new electricity.",
    "The future is AI-powered.",
    "AI is not a threat, but a tool.",
    "Machines are learning. Fast.",
    "AI will amplify human potential.",
    "The best way to predict the future is to build it — with AI.",
    "AI is transforming every industry.",
    "Smarter systems mean smarter lives."
]

# Pick a quote based on the day
quote = quotes[datetime.now().day % len(quotes)]

# Read the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the quote section
new_content = content.split("<!--QUOTE_START-->")[0] + "<!--QUOTE_START-->\n" + quote + "\n<!--QUOTE_END-->" + content.split("<!--QUOTE_END-->")[-1]

# Write it back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

