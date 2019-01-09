class Linux_Traversal:

    def __init__(self):
       pass

    # Method to clear session of Application.
    def clear_session(self):
        self.root = {'key1': 'value1',
                     'key2': 'value2',
                     'key3': {'key3a': 'value3a'},
                     'key4': {'key4a': {'key4aa': {"key4aa.1":""},
                                        'key4ab': {"key4ab.1":""},
                                        'key4ac': {"key4ac.1":""}},
                              'key4b': 'value4b'}}
        self.temproot = self.root
        self.parent_root_1 = self.root
        self.parent_root= self.root
        global switcher, temproot,strpath,current_root,current_root,input1
        strpath = "root:"
        current_root = "root"
        self.path_list = ["root"]
        input1 = ""
        self.path_record = []

    # Method to Store temp dictionary to main dictionary.
    def refresh(self,key, new_value):
        if current_root != "root":
            self.root[key] = new_value
        elif current_root == "root":
            self.root = self.temproot

    # Method to check key present in pass dictionary or not.
    def check(self, folder_name,temproot):
        if folder_name in temproot.keys():
            return 1
        else:return 0

    # Method to check enter command.
    def check_command(self, command):
        if command.startswith("cd ") or command.startswith("rm ") or command.startswith("mkdir ") :
            return 1
        elif self.parent_root == None:

            return 0
        elif command=="ls" or command == "session clear" or command == "pwd" or command == "cd..":
            return 1

        else:return 0

    # Method to make new directory.
    def mkdir(self,folder_name):

        if obj1.check(folder_name,self.temproot) ==1:
            print("ERROR : AlREADY EXIST !")

        else:
            self.temproot[folder_name] = {}
            obj1.refresh(current_root, self.temproot)
            print("SUCCESS: CREATED")

    # Method to list all present items in current working directory.
    def ls(self,temproot):
        try:
            print("DIRECTORIES :"+str(list(temproot.keys())))
        except:
            print("EMPTY DIRECTORY ")

    # Method to remove for directory from pass temp dictionary.
    def rm(self,key_name):

        if obj1.check(key_name,self.temproot) ==0:
            print("ERROR : NOT EXIST !")
        else:
            self.temproot.pop(key_name, None)
            print(self.temproot)
            print(self.root)
            obj1.refresh(current_root, self.temproot)
            print("SUCCESS: DELETED !")
            pass

    # Method to print current working directory.
    def pwd(self):
        print(str(current_root)+ ":/ ")
        pass

    # support method of method(cd)
    def m1(self, d, key):
        # print("running m1")
        temproot_m1 = d.get(key)
        # print(self.temp_root)
        return temproot_m1

    # Method to go in entered path.
    def cd(self,root, temproot):
        global strpath,current_root

        if input1.startswith("cd root:/"):
            working_dict = root
            strpath = "root:/"
        elif not input1.startswith("cd root:/"):
            working_dict = temproot

        if "/" in cmd_part_2 :
            li = cmd_part_2.split("/")
            for key in li:
                if key != "root:":
                    current_root = key
                    working_dict = obj1.m1(working_dict, key)
                    self.parent_root_2 = self.temproot
                    self.parent_root_1 = self.temproot
                    self.temproot = working_dict
        else:
            key = cmd_part_2
            current_root = key
            working_dict = obj1.m1(working_dict, key)

        if cmd_part_2.startswith("root:/"):
            self.path_list = li
        elif "/" in cmd_part_2 and not cmd_part_2.startswith("root:/"):
            for item in cmd_part_2.split("/"):
                self.path_list.append(item)
        else:
            self.path_list.append(cmd_part_2)

        if working_dict != None:
        #     print("Hi>>>>>")
            strpath = strpath + cmd_part_2 + "/"
            print("SUCCESS: REACHED ")
            # self.
            self.parent_root = self.temproot
            self.temproot = working_dict
            # print("Parent root:")
            # print(self.parent_root)
            # return working_dict

        else:
            print("ERROR: INVALID PATH  ")
        obj1.path_recorder(current_root, self.temproot)

    # Method to go one level up.
    def cd_back(self, path):
        try:
            global strpath
            if obj1.check_command(input1) == 1:
                try:
                    self.temproot = self.path_record[-2][1][0]
                except:
                    self.temproot = self.root
                del self.path_record[-1]
                strpath = strpath.split("/")[:-2]
                strpath = str(("/").join(strpath)) + "/"
                if strpath == "/":
                    strpath = "root:/"
        except:
            pass
    def path_recorder(self,pwd,temproot):
        row = [pwd], [temproot]
        self.path_record.append(row)

    # Method to take input from user again
    def live(self):
        global cmd_part_2
        global input1, cmd_part_1

        input1 = input("$ " + str(strpath))
        if obj1.check_command(input1) ==0:
            print("CANNOT RECOGNIZE INPUT")
            obj1.live()
        else:
            if input1 =="session clear":
                print("SUCCESS: CLEARED : RESET TO ROOT")
                obj1.clear_session()

            if input1.count(" ") == 0:
                cmd_part_2 = input1
                if  cmd_part_2 == "pwd":
                    switcher[cmd_part_2]()
                elif cmd_part_2 == "ls":
                    switcher[cmd_part_2](self.temproot)
                elif cmd_part_2 == "cd..":
                    switcher[cmd_part_2](self.path_list)
            elif input1.count(" ") == 1:
                cmd_part_1 = input1.split(" ")[0]
                cmd_part_2 = (input1.split(" ")[1:])
                cmd_part_2 = ''.join(cmd_part_2)
                if cmd_part_1 == "mkdir":
                    switcher[cmd_part_1](cmd_part_2)
                elif cmd_part_1 == "cd":
                    switcher[cmd_part_1](self.root,self.temproot)
                elif cmd_part_1 == "rm":
                    switcher[cmd_part_1](cmd_part_2)
                elif cmd_part_1 == "pwd":
                    switcher[cmd_part_1]()
            elif input1.split(" ")[0] in switcher:
                cmd_part_1 = input1.split(" ")[0]
                cmd_part_2 = (input1.split(" ")[1:])
                cmd_part_2 = ' '.join(cmd_part_2)

                if cmd_part_1 == "mkdir":
                    switcher[cmd_part_1](cmd_part_2)
                elif cmd_part_1 == "cd":
                    switcher[cmd_part_1](self.root,self.temproot)
                elif cmd_part_1 == "rm":
                    switcher[cmd_part_1](cmd_part_2)
                elif cmd_part_1 == "ls":
                    switcher[cmd_part_1](self.temproot)
            obj1.live()

obj1 = Linux_Traversal()
print("<Starting your Application...>")
obj1.clear_session()
switcher = {
            "mkdir": obj1.mkdir,
            "ls": obj1.ls,
            "rm": obj1.rm,
            "pwd": obj1.pwd,
            "cd": obj1.cd,
            "cd..":obj1.cd_back

        }

obj1.live()