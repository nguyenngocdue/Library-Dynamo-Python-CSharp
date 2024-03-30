def logger(title, content):
    import datetime
    date = datetime.datetime.now()
    f = open(r"A:\Library-Dynamo-Python-CSharp\python.log", 'a')
    f.write(str(date) + '\n' + title + '\n' + str(content) + '\n')
    f.close()
    