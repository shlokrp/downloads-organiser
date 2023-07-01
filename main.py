import shutil
import os

folder_ex = {
    "Programming Files": {".ipynb", ".py", ".java", ".cs", ".js", ".vsix", ".jar"},
    "Compressed": {".zip", ".rar", ".arj", ".gz", ".sit", ".sitx", ".sea", ".ace", ".bz2", ".7z"},
    "Applications": {".exe", ".msi"},
    "Pictures":  {".jpeg", ".jpg", ".png", ".gif", ".tiff", ".raw", ".webp", ".jfif", ".ico", ".psd", ".svg", ".ai"},
    "Videos":  {".mp4", ".webm", ".mkv", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".M4P", ".M4V", ".WMV", ".MOV", ".QT", ".FLV", ".SWF", ".AVCHD", ".avi", ".mpg", ".mpe", ".mpeg", ".asf", ".wmv", ".mov", ".qt", ".rm"},
    "Documents": {".txt", ".pdf", ".doc", ".xlsx", ".pdf", ".ppt", ".pps", ".docx", ".pptx"},
    "Music":  {".mp3", ".wav", ".wma", ".mpa", ".ram", ".ra", ".aac", ".aif", ".m4a", ".tsa"},
    "Torrents": {".torrent"},
    "Other": set([])
}


def create_folders():
    """Creates the required folders to organize files ('Pictures', 'Videos'...).
    """
    for root in folder_ex:
        try:
            os.mkdir(os.path.join(os.getcwd(), root))
            print(f"'{root:20}' Created ✔")
        except FileExistsError:
            print(f"'{root:20}' Already Exists")


def get_folder(ext):
    """Returns the Folder that corresponds to the given extension.
    Args:
        ext (String): The extension of the file.
    Returns:
        String: The name of the Folder that holds the ext.
    """
    for f, ex in folder_ex.items():
        if ext in ex:
            return f
    return "Other"


def start():
    """Organize files in the current directory, each to the corresponding folder.
    """
    for file in os.listdir():
        # Check it's not filemover.py, a hidden file or a directory
        if file != __file__ and file[0] != '.' and '.' in file:
            try:
                _, ex = os.path.splitext(file)
                folder = get_folder(ex)
                shutil.move(file, os.path.join(os.getcwd(), folder))
            except KeyError as error:
                print(error)
                print("Couldn't move file ", file)


if __name__ == "__main__":
    create_folders()
    start()
    abc = input("Satisfied? ")
