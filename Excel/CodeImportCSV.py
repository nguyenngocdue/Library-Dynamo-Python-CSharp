import os

'''New Folder'''
##########################################################################
path = r'C:\Users\NGUYEN NGOC DUE\\Desktop\Sheet'
if not os.path.exists(path):
    os.makedirs(path)
    
    
'''NewExcel File'''
##########################################################################
# """ createFile = open(r'C:\Users\NGUYEN NGOC DUE\Desktop\Sheet\Sheet.csv',"w")
# createFile.close()

import csv
with open (r'C:\Users\NGUYEN NGOC DUE\Desktop\Sheet\Sheet.csv','w',newline='') as f:
    write = csv.writer(f)
    #write.writerow(['Create Sheet From Excel File'])
    write.writerow(['NO.i','Sheet Number','Sheet Name','Title Block'])
    write.writerow([1,'A101','Your Sheet Name:Sheet one_1','Your Family Title']) 

with open (r'C:\Users\NGUYEN NGOC DUE\Desktop\Sheet\Sheet.csv','r') as f:
    cs_f = csv.reader(f)
    out = []
    for row in cs_f:
        print('{:<25} {:<25} {:<25} {:<25}'.format(*row))
##########################################################################
# import csv
# with open (r'C:\Users\NGUYEN NGOC DUE\Desktop\Sheet\Sheet.csv','w') as f:
#     write = csv.writer(f)   
#     write.writerow(['Create Sheet From Excel File'])
# with open (r'C:\Users\NGUYEN NGOC DUE\Desktop\Sheet\Sheet.csv','a') as f:
#     fielnames = ['NO.i','Sheet Number','Sheet Name','Title Block']
#     writer = csv.DictWriter(f,fielnames)
#     writer.writeheader()
#     writer.writerow({'NO.i':1,'Sheet Number':'A101','Sheet Name':'Your Sheet Name:Sheet one_1','Title Block':'Your Family Title'})



