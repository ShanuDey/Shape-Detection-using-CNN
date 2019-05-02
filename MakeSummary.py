import os

def makeSummary(input_path):

    fp = open(input_path+"summary.csv",'w')
    fp.write("image,label\n")
    try:
        for i in os.listdir(input_path):
            if(i=='summary.csv'):
                continue

            sub_path = input_path + i
            label = i
            count = 0
            for j in os.listdir(sub_path):
                fp.write(sub_path+"/"+j+","+i+"\n")
                count+=1
            print(i, "count is :",count)
        print("Check output here :",input_path+"summary.csv")

    except Exception as e:
        print("An exception occured")
        print(e)

    finally:
        fp.close()

if __name__== '__main__':
    print("This is",__name__)
    input_path = 'shapes/'
    makeSummary(input_path)