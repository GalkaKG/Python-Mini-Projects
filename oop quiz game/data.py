import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]



# question_data = [
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "RAM stands for Random Access Memory.", "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
#      "incorrect_answers": ["False"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#                                        "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "Time on Computers is measured via the EPOX System.", "correct_answer": "False",
#      "incorrect_answers": ["True"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#                                       "question": "The Windows 7 operating system has six main editions.",
#                                       "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
#      "correct_answer": "True", "incorrect_answers": ["False"]}
# ]
