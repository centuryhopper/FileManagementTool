import os
import shutil

# code by Leo
# inspired by this link: https://www.youtube.com/watch?v=KBjBPQExJLw&t=8s


class FileUtils:
    @staticmethod
    def organizeFilesIntoFolders(path: str, extensionsToSkip: list[str] = [], onlyTargetTheseExtensions: list[str] = []):
        files = os.listdir(path)
        if not files:
            print('this path has no files')
            return
        for file in files:
            # skip these extensions
            for ext in extensionsToSkip:
                if file.endswith(ext):
                    continue
            # only process these extensions
            for ext in onlyTargetTheseExtensions:
                if not file.endswith(ext):
                    continue
            # name of the file followed by .[ext]
            filename, ext = os.path.splitext(file)
            # print(file)
            ext = ext[1:]  # remove the leading period
            # print(filename, ext)
            currentFilePath = f'{path}/{file}'
            destinationFilePath = f'{path}/{ext}/{file}'

            # we need to create that folder first and then move it inside
            if not os.path.exists(f'{path}/{ext}'):
                print(
                    f'{path}/{ext} does not exist, so making a directory for it now')
                os.makedirs(f'{path}/{ext}')
            shutil.move(currentFilePath, destinationFilePath)


FileUtils.organizeFilesIntoFolders('C:\\Users\\Leo Zhang\\Desktop\\testing', onlyTargetTheseExtensions=['.xlsx'])
