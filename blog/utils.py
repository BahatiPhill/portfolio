import time

#Generate Image filename
def set_filename(filename):
    print("### FILENAME: ", filename)
    filename = time.strftime("%Y%m%d-%H%M%S")+ '.jpg'
    return filename