usersinput = input("File name: ").strip().lower()

if usersinput.endswith(".jpg") or usersinput.endswith(".jpeg"):
    print("image/jpeg")
elif usersinput.endswith(".gif"):
    print("image/gif")
elif usersinput.endswith(".png"):
    print("image/png")
elif usersinput.endswith(".pdf"):
    print("application/pdf")
elif usersinput.endswith(".txt"):
    print("text/plain")
elif usersinput.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
