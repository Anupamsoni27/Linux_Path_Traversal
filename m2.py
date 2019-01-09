key = path[-2]
                parent_of_key = "root"
                try:
                    parent_of_key = path[-3]
                except:
                    pass
                print("passing : " + str(key))
                print(self.parent_root)

                print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                self.temproot = self.parent_root
                if parent_of_key != "root":

                    self.parent_root = obj1.m1(self.parent_root, key)
                # print(self.parent_root)
                strpath = strpath.split("/")[:-2]
                strpath = str(("/").join(strpath)) + "/"
                print(strpath)
                self.path_list = self.path_list.pop()
                print(self.path_list)