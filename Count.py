import os

def count_dir(path):

    list_dir = os.listdir(path)

    #print(list_dir)

    total = 0

    for i in range(len(list_dir)):
        dir_path = path+list_dir[i]
        count = len(os.listdir(dir_path))
        list_dir[i] = (list_dir[i],count)
        total += count

    print(list_dir)
    print("Total = ",total)

    return list_dir

if __name__=='__main__':
    path = 'shapes/'

    print("This is ",__name__)

    count_dir(path)
