from pytube import YouTube

def convert_to_mp4(video_url, output_path='output.mp4'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path)

        print("Conversion complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_YOUTUBE_URL' with the actual YouTube video URL
    youtube_url = input("Enter YouTube video URL: ")
    convert_to_mp4(youtube_url)
