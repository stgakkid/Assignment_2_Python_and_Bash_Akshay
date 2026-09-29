from datetime import datetime 
file = open("student_info.txt", "w")
datetime =  (datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #Optional enhancement.
file.write("I am writing content to the file \n")
file.write("Adding some more content \n")
file.write(datetime)
file.close()



print(f"File successfully created at {datetime}")  #Used f-strings for insert variables

