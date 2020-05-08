import os
import shutil

if not os.path.exists("photos"):
     os.mkdir("photos")    
     
if not os.path.exists("docs"):
      os.mkdir("docs")

if not os.path.exists("other"):    
      os.mkdir("other")

if not os.path.exists("media"):
    os.mkdir("media")

# if not os.path.exists("python"):   
#   os.mkdir("python") 

# '''filename, filext= os.path.splitext("G:\bittu\screen_capture.jpg")

# print(filename)
# print(filext)'''

#filext="G:\bittu\screen_capture.jpg".split(".")
#print(filext[1])
print(len(os.listdir()))
print(os.listdir())

for files in os.listdir() :
     if os.path.isfile( files):

    #  filext=files.split(".")[1]
      #  print(filext)

       imgext=(".jpg", ".jpeg", ".png")
       docext=(".txt",".pdf")
       mediaext=(".mp4",".mp3")


     #  if filext is "py":
         # shutil.move(os.listdir()[i],"python")

       if files.endswith(imgext):
          shutil.move(files,"photos")

       elif files.endswith(docext):
          shutil.move(files,"docs") 

       elif files.endswith(mediaext):
          shutil.move(files,"media")  

       else:
           shutil.move(files,"other")
    


         




      