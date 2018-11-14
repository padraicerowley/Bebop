from Utils import get_files_indirectory, parseXmlfile
import os


def detectLangfromXml(corpus_location, found_msg_path):
    from langdetect import detect
    from shutil import copyfile

    files = get_files_indirectory(corpus_location)
    for f in files:
        try:
            tree = parseXmlfile(f)
            if detect(tree.find("text").text) == 'it':
                copyfile(f, found_msg_path+"\\"+os.path.basename(f))
        except Exception as e:
            print("issue with some file: ", f, e)

