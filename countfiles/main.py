import os
import glob

class Moduls:
    @staticmethod
    def list_directory_and_files():
        diramount = 0
        fileamount = 0
        filetypes = {}

        # Walking a directory tree and counting the directories, files, and filetypes
        for dirpath, _, files in os.walk('.'):
            diramount += 1
            for file_name in files:
                fileamount += 1
                _, ext = os.path.splitext(file_name)
                filetypes[ext] = filetypes.get(ext, 0) + 1

        print(f"\nFolders: {diramount}")
        print(f"Files: {fileamount}")
        for ext, count in filetypes.items():
            print(f"   *{ext}: {count}")
        print("\n")

class Init:
    @staticmethod
    def initialize():
        Moduls.list_directory_and_files()

if __name__ == "__main__":
    Init.initialize()
