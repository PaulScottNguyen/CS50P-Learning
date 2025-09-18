#Input string and strip whitespaces
PlaybackSpeed = str(input(f"Please input some text here and I shall make it slower frfr: ")).strip()
#Output the string but replace all whitespaces with "..."
print(PlaybackSpeed.replace(" ","..."))