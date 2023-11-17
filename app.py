# Import Modules
import time
from termcolor import colored
import pyfiglet
from colorama import Fore
from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable, ExtractError, RegexMatchError
import os

# Variables

separator = "#" * 70

option_list = colored(
    """
----------------------
: - "V" => Video     :
----------------------
: - "A" => Audio     :
----------------------
: - "P" => Playlist  :
----------------------
:--------------------:
----------------------
: - "Q" => Quit App  :
----------------------
""",
    "green",
)
input_message = f"""
Here You Need To Choose , What Do You Want To Download ??

{option_list}

Choose Option:
"""

resolution_message = colored(
    """
---------------------------------
: - 1) ===> Highest Resolution  :
---------------------------------
: - 2) ===> 720p Resolution     :
---------------------------------
: - 3) ===> 480p Resolution     :
---------------------------------
: - 4) ===> 360p Resolution     :
---------------------------------
: - 5) ===> 240p Resolution     :
---------------------------------
: - 6) ===> 144p Resolution     :
---------------------------------

* Type A Number (1,2,3,4,5,6):
""",
    "green",
)
complete_message = colored("Download Completed", "green")

# Lists

available_commands = ["V", "A", "P", "Q"]
resolution_list = [1, 2, 3, 4, 5, 6]
yes_no = ["Y", "N"]

# Normal Functions


def setSeparator():
    print("")
    time.sleep(1)
    print(colored(separator, "cyan"))
    print("")
    time.sleep(1)


def live_typing(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print("")


# Check Functions


def yes_no_check(option_name):
    while True:
        if option_name not in yes_no:
            live_typing("Please Try Again: ")
            option_name = input().strip().capitalize()
        else:
            break


def resolution_check(option_name):
    while True:
        if option_name not in resolution_list:
            live_typing("Please Try Again: ")
            option_name = int(input().strip())
        else:
            break


def linkCheck(link):
    pass


# YouTube Function


# Video
def downloadVideo():
    try:
        time.sleep(1)
        live_typing("OK, Please Paste The YouTube Video Link: ")
        url = input().strip()
        print("")

        yt = YouTube(url)
        colored_title = colored(yt.title, "magenta")
        time.sleep(1)

        # Show Title
        live_typing(f'You Want To Download "{colored_title}",')
        print("")
        live_typing(f"Do You Want To Start Download Now ? [Y/N]")
        start_download_option = input().strip().capitalize()
        print("")

        # Yes Or No Check
        yes_no_check(start_download_option)

        # Download Options
        while True:
            if start_download_option == "N":
                time.sleep(1)
                live_typing("OK, Paste Another YouTube Video Link: ")
                url = input().strip()

                print("")
                yt = YouTube(url)
                colored_title = colored(yt.title, "magenta")
                time.sleep(1)

                # Show Title
                live_typing(f'You Want To Download "{colored_title}",')
                print("")
                live_typing(f"Do You Want To Start Download Now ? [Y/N]")
                start_download_option = input().strip().capitalize()
                print("")

                # Yes Or No Check
                yes_no_check(start_download_option)

            else:
                break

        live_typing("Choose The Resolution :")
        live_typing(resolution_message, 0.01)
        resolution_input = int(input().strip())
        print("")

        setSeparator()

        resolution_check(resolution_input)

        # Downloading
        if resolution_input == 1:
            video_stream = yt.streams.get_highest_resolution()
            output_path = f"./Downloaded Videos/{username}/"
            os.makedirs(output_path, exist_ok=True)
            print("")
            live_typing("Downloading ......")
            print("")
            video_stream.download(output_path)

            live_typing(f'Video ==> "{colored_title}" Is Downloaded')
            print("")
        elif resolution_input == 2:
            video_stream = yt.streams.filter(res="720p", file_extension="mp4").first()
            output_path = f"./Downloaded Videos/{username}/"
            os.makedirs(output_path, exist_ok=True)
            print("")
            live_typing("Downloading ......")
            print("")
            video_stream.download(output_path)

            live_typing(f'Video ==> "{colored_title}" Is Downloaded')
            print("")
        elif resolution_input == 3:
            video_stream = yt.streams.filter(res="480p", file_extension="mp4").first()
            output_path = f"./Downloaded Videos/{username}/"
            os.makedirs(output_path, exist_ok=True)
            print("")
            live_typing("Downloading ......")
            print("")
            video_stream.download(output_path)

            live_typing(f'Video ==> "{colored_title}" Is Downloaded')
            print("")
        elif resolution_input == 4:
            video_stream = yt.streams.filter(res="360p", file_extension="mp4").first()
            output_path = f"./Downloaded Videos/{username}/"
            os.makedirs(output_path, exist_ok=True)
            print("")
            live_typing("Downloading ......")
            print("")
            video_stream.download(output_path)

            live_typing(f'Video ==> "{colored_title}" Is Downloaded')
            print("")
        elif resolution_input == 5:
            video_stream = yt.streams.filter(res="240p", file_extension="mp4").first()
            output_path = f"./Downloaded Videos/{username}/"
            os.makedirs(output_path, exist_ok=True)
            print("")
            live_typing("Downloading ......")
            print("")
            video_stream.download(output_path)

            live_typing(f'Video ==> "{colored_title}" Is Downloaded')
            print("")
        elif resolution_input == 6:
            video_stream = yt.streams.filter(res="144p", file_extension="mp4").first()
            output_path = f"./Downloaded Videos/{username}/"
            os.makedirs(output_path, exist_ok=True)
            print("")
            live_typing("Downloading ......")
            print("")
            video_stream.download(output_path)

            live_typing(f'Video ==> "{colored_title}" Is Downloaded')
            print("")
        quitApp()

    except RegexMatchError as e:
        print("")
        err = colored(
            f"""
Error: {e}" 
Invalid YouTube URL. Please provide a valid YouTube video URL.
""",
            "red",
        )
        live_typing(err)

    except VideoUnavailable as e:
        print("")
        err = colored(
            f"""
Error: {e}"
The video is unavailable or restricted.
""",
            "red",
        )
        live_typing(err)

    except ExtractError as e:
        print("")
        err = colored(
            f"""
Error: {e}"
There was an error extracting the video information.
""",
            "red",
        )
        live_typing(err)

    except Exception as e:
        print("")
        err = colored(
            f"""
Error: {e}"
An unexpected error occurred.
""",
            "red",
        )
        live_typing(err)


# Audio


def downloadAudio():
    try:
        time.sleep(1)
        live_typing("OK, Please Paste The YouTube Video Link: ")
        url = input().strip()
        print("")

        yt = YouTube(url)
        colored_title = colored(yt.title, "magenta")
        time.sleep(1)

        # Show Title
        live_typing(f'You Want To Download "{colored_title}" As An Audio,')
        print("")
        live_typing(f"Do You Want To Start Download Now ? [Y/N]")
        start_download_option = input().strip().capitalize()
        print("")

        # Yes Or No Check
        yes_no_check(start_download_option)

        # Download Options
        while True:
            if start_download_option == "N":
                time.sleep(1)
                live_typing("OK, Paste Another YouTube Video Link: ")
                url = input().strip()

                print("")
                yt = YouTube(url)
                colored_title = colored(yt.title, "magenta")
                time.sleep(1)

                # Show Title
                live_typing(f'You Want To Download "{colored_title}" As An Audio,')
                print("")
                live_typing(f"Do You Want To Start Download Now ? [Y/N]")
                start_download_option = input().strip().capitalize()
                print("")

                # Yes Or No Check
                yes_no_check(start_download_option)

            else:
                break
        setSeparator()
        # Downloading
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = f"./Downloaded Videos/{username}/"
        os.makedirs(output_path, exist_ok=True)
        print("")
        live_typing("Downloading ......")
        print("")
        audio_stream.download(output_path)
        live_typing(f'Video ==> "{colored_title}" Is Downloaded As An Audio')
        print("")
        quitApp()

    except RegexMatchError as e:
        print("")
        err = colored(
            f"""
Error: {e}" 
Invalid YouTube URL. Please provide a valid YouTube video URL.
""",
            "red",
        )
        live_typing(err)

    except VideoUnavailable as e:
        print("")
        err = colored(
            f"""
Error: {e}"
The video is unavailable or restricted.
""",
            "red",
        )
        live_typing(err)

    except ExtractError as e:
        print("")
        err = colored(
            f"""
Error: {e}"
There was an error extracting the video information.
""",
            "red",
        )
        live_typing(err)

    except Exception as e:
        print("")
        err = colored(
            f"""
Error: {e}"
An unexpected error occurred.
""",
            "red",
        )
        live_typing(err)


# Playlist


def downloadPlaylist():
    try:
        time.sleep(1)
        live_typing("OK, Please Paste The YouTube Playlist Link: ")
        url = input().strip()
        print("")

        pl = Playlist(url)
        coloredPl_title = colored(pl.title, "blue")
        time.sleep(1)

        # Show Title
        live_typing(f'You Want To Download "{coloredPl_title}" Playlist,')
        print("")
        live_typing(f"Do You Want To Start Download Now ? [Y/N]")
        start_download_option = input().strip().capitalize()
        print("")

        # Yes Or No Check
        yes_no_check(start_download_option)

        # Download Options
        while True:
            if start_download_option == "N":
                time.sleep(1)
                live_typing("OK, Paste Another YouTube Playlist Link: ")
                url = input().strip()

                print("")
                pl = Playlist(url)
                coloredPl_title = colored(pl.title, "blue")
                time.sleep(1)

                # Show Title
                live_typing(f'You Want To Download "{coloredPl_title}" Playlist,')
                print("")
                live_typing(f"Do You Want To Start Download Now ? [Y/N]")
                start_download_option = input().strip().capitalize()
                print("")

                # Yes Or No Check
                yes_no_check(start_download_option)

            else:
                break

        live_typing("Choose The Resolution :")
        live_typing(resolution_message, 0.01)
        resolution_input = int(input().strip())

        setSeparator()

        resolution_check(resolution_input)

        if resolution_input == 1:
            live_typing(f'Downloading "{coloredPl_title}" Playlist')
            for video in pl.videos:
                colored_title = colored(video.title, "magenta")
                video_stream = video.streams.get_highest_resolution()
                output_path = f"./Downloaded Videos/{username}/"
                os.makedirs(output_path, exist_ok=True)
                print("")
                live_typing(f' - Downloading "{colored_title}"')
                print("")
                video_stream.download(output_path)

                live_typing(f' -- Video ==> "{colored_title}" Is Downloaded')
                print("")
            live_typing(complete_message)
        elif resolution_input == 2:
            live_typing(f'Downloading "{coloredPl_title}" Playlist')
            for video in pl.videos:
                colored_title = colored(video.title, "magenta")
                video_stream = video.streams.filter(
                    res="720p", file_extension="mp4"
                ).first()
                output_path = f"./Downloaded Videos/{username}/"
                os.makedirs(output_path, exist_ok=True)
                print("")
                live_typing(f' - Downloading "{colored_title}"')
                print("")
                video_stream.download(output_path)

                live_typing(f' -- Video ==> "{colored_title}" Is Downloaded')
                print("")
            live_typing(complete_message)
        elif resolution_input == 3:
            live_typing(f'Downloading "{coloredPl_title}" Playlist')
            for video in pl.videos:
                colored_title = colored(video.title, "magenta")
                video_stream = video.streams.filter(
                    res="480p", file_extension="mp4"
                ).first()
                output_path = f"./Downloaded Videos/{username}/"
                os.makedirs(output_path, exist_ok=True)
                print("")
                live_typing(f' - Downloading "{colored_title}"')
                print("")
                video_stream.download(output_path)

                live_typing(f' -- Video ==> "{colored_title}" Is Downloaded')
                print("")
            live_typing(complete_message)
        elif resolution_input == 4:
            live_typing(f'Downloading "{coloredPl_title}" Playlist')
            for video in pl.videos:
                colored_title = colored(video.title, "magenta")
                video_stream = video.streams.filter(
                    res="360p", file_extension="mp4"
                ).first()
                output_path = f"./Downloaded Videos/{username}/"
                os.makedirs(output_path, exist_ok=True)
                print("")
                live_typing(f' - Downloading "{colored_title}"')
                print("")
                video_stream.download(output_path)

                live_typing(f' -- Video ==> "{colored_title}" Is Downloaded')
                print("")
            live_typing(complete_message)
        elif resolution_input == 5:
            live_typing(f'Downloading "{coloredPl_title}" Playlist')
            for video in pl.videos:
                colored_title = colored(video.title, "magenta")
                video_stream = video.streams.filter(
                    res="240p", file_extension="mp4"
                ).first()
                output_path = f"./Downloaded Videos/{username}/"
                os.makedirs(output_path, exist_ok=True)
                print("")
                live_typing(f' - Downloading "{colored_title}"')
                print("")
                video_stream.download(output_path)

                live_typing(f' -- Video ==> "{colored_title}" Is Downloaded')
                print("")
            live_typing(complete_message)
        elif resolution_input == 6:
            live_typing(f'Downloading "{coloredPl_title}" Playlist')
            for video in pl.videos:
                colored_title = colored(video.title, "magenta")
                video_stream = video.streams.filter(
                    res="144p", file_extension="mp4"
                ).first()
                output_path = f"./Downloaded Videos/{username}/"
                os.makedirs(output_path, exist_ok=True)
                print("")
                live_typing(f' - Downloading "{colored_title}"')
                print("")
                video_stream.download(output_path)

                live_typing(f' -- Video ==> "{colored_title}" Is Downloaded')
                print("")
            live_typing(complete_message)
        quitApp()

    except RegexMatchError as e:
        print("")
        err = colored(
            f"""
Error: {e}" 
Invalid YouTube URL. Please provide a valid YouTube video URL.
""",
            "red",
        )
        live_typing(err)

    except VideoUnavailable as e:
        print("")
        err = colored(
            f"""
Error: {e}"
The video is unavailable or restricted.
""",
            "red",
        )
        live_typing(err)

    except ExtractError as e:
        print("")
        err = colored(
            f"""
Error: {e}"
There was an error extracting the video information.
""",
            "red",
        )
        live_typing(err)

    except Exception as e:
        print("")
        err = colored(
            f"""
Error: {e}"
An unexpected error occurred.
""",
            "red",
        )
        live_typing(err)


# Quit
def quitApp():
    setSeparator()
    live_typing("Thanks For Using YouTube Downloader :)")
    time.sleep(1)
    print("")
    live_typing(f"Goodbye {colored_username} ^_^")
    time.sleep(1)
    setSeparator()


# Welcome
time.sleep(0.5)
print(f"{Fore.RED}", pyfiglet.figlet_format("YouTube Downloader"), f"{Fore.RESET}")
time.sleep(1)

live_typing("Hello There...", 0.05)
time.sleep(0.5)
live_typing("Here You Are, So You Want To Download Something From YouTube.", 0.05)
time.sleep(0.5)
live_typing("Let Me Help You :)", 0.05)

setSeparator()
# Name
live_typing("What Is Your Name ??", 0.02)
username = input().strip().capitalize()
colored_username = colored(username, "yellow")

setSeparator()

live_typing(f"Hi {colored_username},")
time.sleep(1)

# Choose The Option
live_typing(input_message, 0.01)
user_choice = input().strip().capitalize()
print("")


# Check The Input Command
while True:
    if user_choice not in available_commands:
        live_typing("Please Choose A Valid Option: ")
        live_typing(option_list, 0.01)
        user_choice = input().strip().capitalize()
        print("")

    else:
        break


# Making Commands

if user_choice == "V":
    downloadVideo()

elif user_choice == "A":
    downloadAudio()

elif user_choice == "P":
    downloadPlaylist()

else:
    quitApp()
