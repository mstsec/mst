'''
Mst=>Update=>class
update!update!!
'''
from urllib   import urlopen
from os       import path
from MstColor import *
from base64 import decodestring as de

seru = "http://mstoor.duapp.com/" #UPDATE SERVER HOST
nver = "20131023"              #NOW VERSION

class updatemst:
    '''update plugins'''
    def checkupdate(self):
        '''check if has new version'''
        color.cprint("[*] Access to the remote version..",YELLOW)
        try:
            sver = self.getver()
            sver = sver.replace("\n","")
            if int(sver) > int(nver):
                color.cprint("[i] There is a new version[%s],do u want to update?"%sver,GREEN,0)
                c = raw_input("[y/n]")
                if c.upper() == "Y":
                    color.cprint("[i] Start update...",YELLOW)
                    self.download(sver)
            else:
                color.cprint("[*] No new version[NOW:%s | SER:%s]"%(nver,sver),RED)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)
    def getver(self):
        '''get new version'''
        return urlopen(seru+"update/?do=ver").read()
    def download(self,sver):
        '''start update'''
        try:
            color.cprint("[*] Start download..",YELLOW)
            downurl = urlopen(seru+"update/?do=url").read()
            tmp     = urlopen(downurl).read()
            color.cprint("[*] Save download..",GREEN)
            newname = "mst_%s.zip"%sver
            newmst  = open(newname,"w")
            newmst.write(tmp)
            newmst.close()
            color.cprint("[*] Download OK![%s]"%newname,YELLOW)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)

class updateplu:
    '''update mst self'''
    def __init__(self,n_p_n):
        '''get now plugins num'''
        self.n=n_p_n
    def checkupdate(self):
        '''check has new plus?'''
        try:
            color.cprint("[*] Check server's plugins..",YELLOW)
            ser_plu_nums = urlopen(seru+"update/?do=pns").read()
            ln = int(self.n)
            rn = int(ser_plu_nums)
            if rn>ln:
                color.cprint("[i] Have new plugins,Down?[%s::%s]"%(ln,rn),GREEN,0)
                ok=raw_input("[y/n]")
                if ok.upper() == "Y":
                    self.download()
            else:
                color.cprint("[!] Not new plugins !(l:%s r:%s)"%(ln,rn),RED)
        except Exception,e:
            color.cprint("[!] ERR:%s"%e,RED)

    def download(self):
        '''start down plugins'''
        color.cprint("[*] Start Download..",YELLOW)
        try:
            uplist = urlopen(seru+"update/?do=list").readlines()
            listnn = len(uplist)-1
            listii = 1
            for u in uplist:
                if len(u)>5:
                    u     = u.strip("\n")
                    u     = u.split("{|MST|}")
                    purl  = u[0]
                    pname =de(u[1])
                    if pname[len(pname)-3:] != ".py":
                        pname += ".py"
                    ptype =de(u[2])
                    lfile = "plugins/%s/%s"%(ptype,pname)
                    color.cprint("[%s/%s] Download:%s::%-20s=>"%(listii,listnn,ptype,pname),CYAN,0)
                    try:
                        if path.exists(lfile):
                            color.cprint("ERR:ALREADY EXISTS!",RED)
                        else:
                            fp = open("plugins/%s/%s"%(ptype,pname),"w")
                            ok = urlopen(purl).read()
                            tmp= ok.replace("\n","")
                            fp.write(tmp)
                            fp.close()
                            color.cprint("Done !",GREEN)
                    except Exception,e:
                        color.cprint("ERR:%s"%e,RED)
                    listii += 1
            color.cprint("[*] ALL UPDATE DONE !PLEASE RESTART MST !",RED)
        except Exception,e:
            color.cprint("[!] Update Error!CODE:%s"%e,RED)
if __name__ == '__main__':
    print __doc__
