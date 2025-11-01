 
score = 0
questions = [
        ("What is the capital city of Bangladesh?", "dhaka"),
        ("What is 5+5?", "10"),
        ("What is the capital of India?", "delhi"),
        ("What is 2*6?", "12"),
        ("What is the capital of Nepal?", "kathmandu"),
        ("What is 20/5?", "4"),
        ("What is the capital of Pakistan?", "islamabad"),
        ("What is 15-5?", "10"),
        ("What is the capital of USA?", "washington"),
        ("What is 3*3?", "9")
    ]
for question, Answer in questions :
        UserInput = input(question + "")
        if UserInput.lower()==Answer:
             print("Write Answer")
             score += 1
             print("You Get 1 Mark for right Answer:-",score)
        else:
             print("This is worng Anwser")
             score -= 1
             print("Your 1 Mark Minus for wrong Answer:-",score)
if score == 10:
      score = score +2
      print("Hurrre.... very Good man ")
      print("Your have already get the bonus") 
      print("Your Total mark: ",score)      