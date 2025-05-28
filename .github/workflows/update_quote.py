import random

# List of quotes
quotes = [
    "Artificial intelligence is the new electricity. – Andrew Ng",
    "The future is going to be AI-driven. – Sundar Pichai",
    "AI will be the best or worst thing for humanity. – Stephen Hawking",
    "AI is a tool. The choice about how it gets used is ours. – Oren Etzioni",
    "Humans should be worried about the threat posed by AI. – Elon Musk",
    "AI is neither good nor evil. It's a tool. – Oren Etzioni"
]

# Pick a new quote
new_quote = random.choice(quotes)

# Read README.md
with open("README.md", "r") as file:
    content = file.read()

# Replace the quote between the markers
start_tag = "<!--QUOTE_START-->"
end_tag = "<!--QUOTE_END-->"
start_index = content.find(start_tag) + len(start_tag)
end_index = content.find(end_tag)

new_content = content[:start_index] + "\n" + new_quote + "\n" + content[end_index:]

# Save back to README.md
with open("README.md", "w") as file:
    file.write(new_content)
