from yt_dlp import YoutubeDL as yd2


link = input("Paste yt link here: \n")

ydl_opts = {
    'format': 'm4a/bestaudio/best',

    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
    'paths' : {'home': 'music/'}
}

def main():
    with yd2(ydl_opts) as ad:
        info = ad.extract_info(link, False)
        if info["playlist"] != None:
            return
        file = ad.prepare_filename(info)
        ad.process_info(info_dict=info)

if __name__ == "__main__":
    main()