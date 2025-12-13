# ques1
word_mean = {
    "table": ' "a peice of furniture", "list of facts and figures" ',
    "cat": "a small animal",
}
print(word_mean)

# ques2
subjects = {"python", "java", "javascript", "C++", "C", "python", "java"}
print(subjects)
print(len(subjects))

# ques3
Marks = {}
Maths = float(input("Enter your maths marks: "))
English = float(input("Enter your English marks: "))
Science = float(input("Enter your Science marks: "))
Marks.update({"Maths": Maths, "English": English, "Science": Science})
print(Marks)

# ques4
num1 = int(9)
num2 = float(9)
num_set = {num1, num2}
print(num_set)
print("Note that in set 9 and 9.0 will be treated as same")

values = {
    ("float", 9.0), ("int", 9)
}
print(values)