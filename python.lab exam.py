books={
    101:"python",
    102:"maths",
    103:"science"
}

available={101,102,103}
records=[]


student=1
book=101

if book in available:
    available.remove(book)
    records.append((student,book,"Borrowed"))
    print("Book borrowed successfully")
else:
    print("Book not available")
    

print("Available books:", available)
print("Borrowing records:", records)

count=sum(1 for record in records if record[0]==student)
print("Books borrowed by student",student,"is",count)

available.add(book)
print("Book returned successfully")
print("Available books:",available)