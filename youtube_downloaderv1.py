from pytube import YouTube


link = input("Enter/Copy the Video Link to continue: ")

Download_Video_Link = YouTube(link)

Title = Download_Video_Link.title
Number_of_views = Download_Video_Link.views
Length_of_Video = Download_Video_Link.length
Author_of_Video = Download_Video_Link.author
Publish_date = Download_Video_Link.publish_date

print("Title: ", Title)
print("Number of Views:", Number_of_views)
print("Length of the Video in seconds:", Length_of_Video)
print("Youtube Channel:", Author_of_Video)
print("Publish Date:", Publish_date)

Download_Video_Link.streams.get_highest_resolution().download()
print("Download finished successfully")
