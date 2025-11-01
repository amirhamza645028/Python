

def get_even(number):
    return[ r for r in number if r%2 == 0]
Number = [1,2,3,4,45,5,6,7,8]
print(get_even(Number))
print(Number)
print("Your even Number:{r}")
# *******************************************************************
                        # Dictionary
                        # মূল পয়েন্ট
# ********************************************************************
# for x in dict → শুধু key দেয়।
# for key, value in dict.items() → key আর value দুটোই দেয়।
# ফাংশনে return না দিলে → None ফেরত আসে।
# return হলো ফাংশনের বাইরে ভ্যালু ফেরত পাঠানোর জন্য।
# তুমি চাইলে return দিয়ে string, list, dict — যা খুশি পাঠাতে পারো।

def show_info(student):
    info = []
    for key , value in student.items():
        info.append(f"{key}:{value}")
    return info
student = {"name":"Hamza","dept":"CSE","age":20}
result = show_info(student)
print(result)
print("why couldn't this program ?")
