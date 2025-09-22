#Ask for the user file name 
filename = str(input("Enter the file name: ")).strip().lower()
filetype = filename.split(".")[-1] #Split their string into two when "." is found then delete the first string
match filetype:
    case "jpg"|"jpeg"|"png"|"gif"|"bmp"|"tiff"|"webp":
        print("This is an image file.")
    case "mp3"|"wav"|"flac"|"aac"|"ogg":
        print("This is an audio file.")
    case "mp4"|"avi"|"mkv"|"mov"|"flv":
        print("This is a video file.")
    case "pdf"|"doc"|"docx"|"txt"|"xls"|"xlsx":
        print("This is a document file.")
    case "zip"|"rar"|"tar"|"gz"|"7z":
        print("This is a compressed file.")
    case "exe"|"bat"|"sh"|"msi":
        print("This is an executable file.")