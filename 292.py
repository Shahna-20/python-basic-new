#Try to open and write to a file that is not writable:

try:
    f = open("demofile.txt")
    try:
        f.write("lorem iseum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")