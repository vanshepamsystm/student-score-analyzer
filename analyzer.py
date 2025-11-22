students=[]
file = open("students.txt","r")
content = file.readlines()
# print(content) 
file.close()

for line in content:
    line = line.strip() #removes newline
    name,score=line.split(",") #split into 2 parts
    score = int(score) #convert score to number
    students.append((name,score)) #add to list
# print(students)
total_students = len(students)
print("total students: ",total_students)

scores = []
for s in students:
    scores.append(s[1])
print(scores)

sum_scores = sum(scores)
average_score = sum_scores/total_students
print("average score: ",average_score)

highest_student = max(students, key = lambda x:x[1])
print("Highest Score: ")
print("Name: ",highest_student[0])
print("Score: ",highest_student[1])
print("-------")
lowest_student = min(students, key = lambda x:x[1])
print("Lowest Score: ")
print("Name: ",lowest_student[0])
print("Score: ",lowest_student[1])



summary_line1 = "Number of students: " + str(total_students) + "\n"
summary_line2 = "Average score: " + str(round(average_score,2)) + "\n"
summary_line3 = "Highest score: " + highest_student[0] + " (" + str(highest_student[1]) + ")\n"
summary_line4 = "lowest score: " + lowest_student[0] + " (" + str(lowest_student[1]) + ")\n"

summary = summary_line1 + summary_line2 + summary_line3 + summary_line4

with open("outpuut.txt","w") as f:
    f.write(summary)

print("Summary written to output.txt")