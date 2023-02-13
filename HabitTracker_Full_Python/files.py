def read_file(filename):
    """ read a file from path
    :param filename: path to file
    :return: Object or None
    """
    import io
    try:
        f = io.open(filename, mode="r", encoding="utf-8")
        return f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)  # Sorry, the file John.txt does not exist.


def delete_file(path):
    """ read a file from path
    :param path: path to file
    :return: some text
    """
    import os
    try:
        os.remove(path)
        print("Removed file in path:")
        print(path)
    except FileNotFoundError:
        msg = "Sorry, the file " + path + " does not exist."
        print(msg)  # Sorry, the file does not exist.
    except PermissionError:
        print("Wasn't able to delete the file. (maybe in 'used' status..)")
