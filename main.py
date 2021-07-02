import os.path, glob, shutil

txtfiles = []

print('Что чекать?')
print('1 - чекать куки')
print('2 - чекать пароли')
info = input("$ ")

if info == "1":
    o = 1
    while o > 0:
            print("Введите название сервиса (пример - coinbase.com , или coinbase)")
            sitec = input("$ ")
            print("  ")
            print('Чекаю логи!')
            i = 1
            for file in glob.glob("data/*/Cookies/*.txt"):
                try:
                    txtfiles.append(file)
                    current_file = open(file, "r")
                    string1 = str(sitec)
                    file1 = open(file, "r")
                    flag = 0
                    index = 0
                    for line in file1:
                        index = 1

                        if string1 in line:
                            flag = 1
                            break
                    if flag == 0:
                        answer = "BAD"
                    else:
                        try:
                            os.mkdir('cookies/' + sitec + '/')
                        except Exception:
                            pass
                        print("  ")
                        print(file)
                        print('Нашел ' + str(sitec))
                        try:
                            os.mkdir('cookies/' + sitec + '/' + str(i) + "/")
                        except Exception:
                            pass
                        dest_dir = "cookies/" + sitec + "/" + str(i) + "/"
                        shutil.copy(file, dest_dir)
                        i = i + 1
                    file1.close()
                except Exception:
                    pass
if info == "2":
    o = 1
    while o > 0:
        print("Введите название сервиса (пример - coinbase.com , или coinbase)")
        sitec = input("$ ")
        print("  ")
        print('Чекаю логи!')
        i = 1
        for file in glob.glob("data/*/Passwords.txt"):
            try:
                txtfiles.append(file)
                current_file = open(file, "r")
                string1 = str(sitec)
                file1 = open(file, "r")
                flag = 0
                index = 0
                for line in file1:
                    index = 1

                    if string1 in line:
                        flag = 1
                        break
                if flag == 0:
                    answer = "BAD"
                else:
                    try:
                        os.mkdir('passwords/' + sitec + '/')
                    except Exception:
                        pass
                    print("  ")
                    print(file)
                    print('Нашел ' + str(sitec))
                    try:
                        os.mkdir('passwords/' + sitec + '/' + str(i) + "/")
                    except Exception:
                        pass
                    dest_dir = "passwords/" + sitec + "/" + str(i) + "/"
                    shutil.copy(file, dest_dir)
                    i = i + 1
                file1.close()
            except Exception:
                pass