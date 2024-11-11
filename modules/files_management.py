import os


def get_new_foldername(lecture):
    for name in sorted(os.listdir("./data/lectures")):
        print(name)

        new_num = int(name.split("_")[0]) + 1

    return str(new_num) + "_" + lecture + "_lecture"


print(get_new_foldername("hallo"))
