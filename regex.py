# Regular Expressions

import re

# Match Function
pattern = r"abc"  # regex pattern
text = "abcdef"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.match(pattern, text)
if result:
    print("Pattern matched at the beginning of the string.")
else:
    print("Pattern not matched.")

# Search Function
pattern = r"abc"  # regex pattern
text = "defabcghi"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.search(pattern, text)
if result:
    print("Pattern found in the string.")
else:
    print("Pattern not found.")

# Findall Function
pattern = r"\d+"  # regex pattern to match digits
text = "There are 123 apples and 456 oranges."

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Numbers found:", result)

# Split Function
pattern = r"\s"  # regex pattern to split on whitespaces
text = "Hello World! How are you?"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.split(pattern, text)
print("Split result:", result)

# Sub Function
pattern = r"apple"  # regex pattern to match
text = "I have an apple. An apple a day keeps the doctor away."

replacement = "banana"

print(f"Pattern: {pattern}")
print(f"Text: {text}")
print(f"Replacement: {replacement}")

result = re.sub(pattern, replacement, text)
print("Updated string:", result)

# Meta-characters
pattern = r"[aeiou]"  # match any vowel
text = "Hello World!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Vowels found:", result)

pattern = r"\."  # match a dot character
text = "Hello. How are you?"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Dot found:", result)

pattern = r"he."  # match 'he' followed by any character
text = "hello, hey, her, his"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"^hello"  # match 'hello' at the start of the string
text = "hello world! hello there!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"there$"  # match 'there' at the end of the string
text = "hello there! are you there?"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"o*"  # match zero or more 'o' characters
text = "hello, ooo, ooooh"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"o+"  # match one or more 'o' characters
text = "hello, ooo, ooooh"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"o{2,3}"  # match 2 to 3 'o' characters
text = "hello, ooo, ooooh"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"hello|world"  # match 'hello' or 'world'
text = "hello world! hi there!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"(hello|hi) world"  # match 'hello world' or 'hi world'
text = "hello world! hi there!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

# Special Sequences
pattern = r"\Ahello"  # match 'hello' at the start of the string
text = "hello world! hello there!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"\bworld\b"  # match 'world' as a whole word
text = "hello world! hi there!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"\Bworld\B"  # match 'world' when not at a word boundary
text = "hello world! hi there!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

pattern = r"\d"  # match a digit
text = "There are 123 apples and 456 oranges."

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Digits found:", result)

pattern = r"\D"  # match a non-digit
text = "There are 123 apples and 456 oranges."

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Non-digits found:", result)

pattern = r"\s"  # match a whitespace character
text = "Hello World!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Whitespaces found:", result)

pattern = r"\S"  # match a non-whitespace character
text = "Hello World!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Non-whitespaces found:", result)

pattern = r"\w"  # match a word character
text = "Hello World!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Word characters found:", result)

pattern = r"\W"  # match a non-word character
text = "Hello World!"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Non-word characters found:", result)

pattern = r"there\Z"  # match 'there' at the end of the string
text = "hello there! are you there?"

print(f"Pattern: {pattern}")
print(f"Text: {text}")

result = re.findall(pattern, text)
print("Pattern found:", result)

# Match object and its methods
pattern = r"apple"
text = "I have an apple."

print(f"Pattern: {pattern}")
print(f"Text: {text}")

match = re.search(pattern, text)
if match:
    print("Pattern matched:", match.group())
    print("Start index:", match.start())
    print("End index:", match.end())
    print("Span:", match.span())
    print("Original string:", match.string)
else:
    print("Pattern not found.")
