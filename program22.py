import sys
# def display_file(file1):
#     try:
#         with open(file1,'r') as f:
#             print(f.read())
#     except :
#         print("file not found")
def copy_files(file1,file2):
    try:
        with open(file1,'r') as f1,open(file2,'w') as f2:
            for i in f1:
                f2.write(i)
            print("completed....!")
    except:
        print("file not found")
copy_files(sys.argv[1],sys.argv[2])
# display_file(sys.argv[2])
