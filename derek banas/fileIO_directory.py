import os

def directoryPlay():
    print os.listdir("E:\Youtube Videos")
    print os.path.isfile("E:\Youtube Videos")
    print os.path.isdir("E:\Youtube Videos")

    dirList = os.listdir("E:\Youtube Videos")

    for files in dirList:
        print files
        if os.path.isdir("E:\Youtube Videos" + files):
            print os.listdir("E:\Youtube Videos" + files)
        else:
            continue

    return

def main():
    directoryPlay()


if __name__ == '__main__': main()
