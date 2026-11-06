words=["cat","apple","dog","banana","sun"]

result=[word.upper()for word in words if len(word) > 3]
print(result)