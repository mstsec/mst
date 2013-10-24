'''
Mst=>class=>load::load plugin
Mst=>class=>plug::plugin class
'''
from MstColor  import *
from MstPlugin import *

class load:
    '''load mst plugin'''
    def start(self,plutype,pluname):
        try:
            mm=m("plugins/%s.py"%pluname)
            while 1:
                mm.printp(plutype,pluname)
                pcmd=raw_input(">")
                if   pcmd == 'back' or pcmd == 'exit':
                    break
                elif pcmd == 'help':
                    mm.pluhelp()
                elif pcmd == 'cls':
                    mm.cls()
                elif pcmd == 'info':
                    mm.info()
                elif pcmd == 'opts':
                    mm.opt()
                elif pcmd == 'exploit':
                    mm.exploit()
                elif pcmd == 'load':
                    mm.load()
                elif pcmd == 'set':
                    color.cprint("[?] USAGE:set <PARAM> <VALUE>",YELLOW)
                elif len(pcmd.split(" "))==2:
                    ptmp=pcmd.split(" ")
                    if ptmp[0] == "load":
                        if len(ptmp[0])>0 and len(ptmp[1])>0:
                            execfile("plugins/load/%s.py"%ptmp[1])
                elif len(pcmd.split(" "))==3:
                    ptmp=pcmd.split(" ")
                    if ptmp[0] == "set":
                        if len(ptmp[1])>0 and len(ptmp[2])>0:
                            mm.setp(ptmp[1],ptmp[2])
        except KeyboardInterrupt:
            color.cprint("\n[!] CTRL+C EXIT !",RED)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)


if __name__ == '__main__':
    print __doc__
else:
    load=load()
