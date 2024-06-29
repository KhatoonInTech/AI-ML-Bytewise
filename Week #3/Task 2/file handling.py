#fileNotFound handling
filename="output.txt"
try:
  with open(filename) as file:
    content=file.read()
except FileNotFoundError:
    print(f"\nSorry , we can't locate your file {filename}")    

#reading content of file
print(content)

#writing to file
""" Using Append mode instead of Write mode to prvent OverWriting"""
file="output.txt"
#handling errors in file writing
try:
   with open(file,"a") as f_write:
      f_write.write(input(f"\nWrite your analysis on {filename} here:\n").splitlines())
except OSError or FileNotFoundError or PermissionError:
   print(f"\nSorry , you can't write in {file} .")

# Count the approximate number of words in the file.
def wordcount(file_path: str)   ->int:
   try:
      with open(file_path) as f:
         words=f.read().split()
         return len(words)
   except FileNotFoundError:
     print(f"\nSorry , we can't locate your file {file_path}")    

#demonstrating wordcount function
filepath="data.txt"
print(f"\nThe number of words in the file: {filepath} is {wordcount(filepath)} .")