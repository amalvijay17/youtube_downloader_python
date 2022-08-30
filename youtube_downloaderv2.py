from pytube import YouTube

link = input("Enter/Copy the Video Link to continue: \n\n")

Download_Video_Link = YouTube(link)

title = Download_Video_Link.title
number_of_views = Download_Video_Link.views
length_of_Video = Download_Video_Link.length
author_of_Video = Download_Video_Link.author
publish_date = Download_Video_Link.publish_date


def Video_Youtube_Details():
    print("\nTitle:", title)
    print("\nNumber of Views:", number_of_views)
    print("\nLength of the Video in seconds:", length_of_Video)
    print("\nYoutube Channel:", author_of_Video)
    print("\nPublish Date:", publish_date)


def Video_Downloader():
    Download_Video_Link.streams.get_highest_resolution().download()
    print("Download finished successfully")


Video_Youtube_Details()
# Video_Downloader()

