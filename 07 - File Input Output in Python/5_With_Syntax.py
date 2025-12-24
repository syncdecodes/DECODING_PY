with open("demo2.txt", "a") as f:
    data = f.write("\nHow are you man")
    print(data)

print("with syntax automatically closes the file so no need to do f.close()")