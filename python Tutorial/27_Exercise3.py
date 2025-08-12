# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.


questions = [
    ["Who developed python?", "Games Gosling", "Guido van Rossum", "Dennis Ritchie", "Rasmus Lerdorf", 2],
    ["Who is Spider man?", "Tony Stark", "Bruce wane", "Peter Parker", "Steve Rogers", 3],
    ["How many squares are there in chess board?", "70", "54", "62", "64", 4],
    ["Which of the following is used in pencils?", "Silicon", "Phosphorous", "Graphite ", "Charcoal ", 3],
    ["How many squares are there in chess board?", "70", "54", "62", "64", 4],
    ["How many squares are there in chess board?", "70", "54", "62", "64", 4],
    ["How many squares are there in chess board?", "70", "54", "62", "64", 4],
    ["How many squares are there in chess board?", "70", "54", "62", "64", 4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}           b.{question[2]}")
    print(f"c.{question[3]}           d.{question[4]}")

    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == 0):
        if (i == 0):
            money = 0
            break
        else:
            money = levels[i - 1]
            break
    elif (reply == question[5]):
        print(f"Correct answer, you won Rs.{levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
    else:
        print("Wrong answer!")
        break

print("Total money you take home is:", money)
