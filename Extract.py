import pdfplumber
import csv
import re

pdf_path = input(str("Enter the path to the PDF file: "))
csv_path = input(str("Enter the path to save the CSV file: "))

questions = []

with pdfplumber.open(pdf_path) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"

# Regex to extract questions, options, and answers
pattern = re.compile(
    r"\d+\.\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nAnswer:\s*([A-D])",
    re.DOTALL
)

for match in pattern.finditer(text):
    question, a, b, c, d, answer = match.groups()
    questions.append([question.strip(), a.strip(), b.strip(), c.strip(), d.strip(), answer.strip().lower()])

# Write to CSV
with open(csv_path, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["question", "option_a", "option_b", "option_c", "option_d", "answer"])
    writer.writerows(questions)

print(f"Extracted {len(questions)} questions to {csv_path}")