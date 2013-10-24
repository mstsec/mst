'''
Mst=>Plugin=>Class
'''
from MstColor   import *
from MstExploit import *
from os         import path,system
class m:
    '''mst plugin's class'''
    def __init__(self,name):
        '''exec plugin code'''
        fp   = open(name).read()
        exec(fp)
        code = '\n'
        for t in mstplugin.opts:
            o=t[0]
            v=t[1]
            code += 'global %s\n'%o
            code += '%s="%s"\n'%(o,v)
        code += "global plugin\n"
        code += "plugin=mstplugin()\n"
        exec(fp+code)
    def info(self):
        '''display plugin infos'''
        color.cprint("PLUGIN INFOS",YELLOW)
        color.cprint("============",GREY)
        color.cprint("PARAMETER       VALUE",YELLOW)
        color.cprint("-"*15+" "+"-"*20,GREY)
        for n in plugin.infos:
            p=n[0]
            v=n[1]
            color.cprint("%-15s"%p,CYAN,0)
            color.cprint("%-s"%v,PURPLE)
    def opt(self):
        '''display plugin opts'''
        color.cprint("PLUGIN OPTS",YELLOW)
        color.cprint("===========",GREY)
        color.cprint("%-15s %-20s %-40s"%("PARAMETER","VALUE","DESCRIPTION"),YELLOW)
        color.cprint("%-15s %-20s %-40s"%("-"*15,"-"*20,"-"*40),GREY)
        for n in plugin.opts:
            p=n[0]
            v=n[1]
            d=n[2]
            color.cprint("%-15s"%p,CYAN,0)
            exec('color.cprint("%-20s"%'+"%s"%p+',PURPLE,0)')
            color.cprint("%-40s"%d,GREEN)
        if self.checkpayload(PAYLOAD) == "TRUE":
            color.cprint("PAYLOAD OPTS",YELLOW)
            color.cprint("============",GREY)
            color.cprint("%-15s %-40s"%("PARAMETER","DESCRIPTION"),YELLOW)
            color.cprint("%-15s %-40s"%("-"*15,"-"*40),GREY)
            code = open("plugins/payload/"+PAYLOAD+".py").read()
            exec(code)
            try:
                exec("global mstpayload")
            except:
                pass
            for n in mstpayload.opts:
                p=n[0]
                d=n[1]
                color.cprint("%-15s"%p,CYAN,0)
                color.cprint("%-40s"%d,PURPLE)
    def setp(self,p,v):
        '''set plugin par value'''
        p=p.upper()
        if p == 'PAYLOAD':
            if v.upper() == "FALSE":
                code  = 'global PAYLOAD;PAYLOAD="false";'
                exec(code)
                color.cprint("[*] Disabled PAYLOAD !",YELLOW)
            elif self.checkpayload(v) == 'TRUE'  and self.getopt("PAYLOAD") != "FALSE":
                color.cprint("[*] SET %s=>%s"%(p,v),YELLOW)
                code  = 'global %s\n'%p
                code += '%s="%s"'%(p,v)
                exec(code)
            else:
                color.cprint("[!] SET PAYLOAD FALSE !",RED)

        else:
            color.cprint("[*] SET %s=>%s"%(p,v),YELLOW)
            code  = 'global %s\n'%p
            code += '%s="%s"'%(p,v)
            exec(code)
    def getopt(self,opt):
        '''get plugin opt'''
        ok='FALSE'
        for n in plugin.opts:
            p=n[0]
            v=n[1]
            d=n[2]
            if opt == p:
                ok=v
        return ok.upper()

    def exploit(self):
        '''start exploit !!'''
        try:
            global fuck
            fuck=fuck()
        except:
            pass
        color.cprint("[*] Start exploit..",YELLOW)
        plugin.exploit()
    def checkpayload(self,payload):
        '''check payload exists'''
        ok='no'
        cf="plugins/payload/%s.py"%payload
        if payload == '' or payload.upper() == 'FALSE':
            ok='false'
        if path.exists(cf):
            ok='true'
        return ok.upper()


    def printp(self,pt,plu):
        '''plugin color input'''
        ptmp=plu.split("/")
        pplu=plu[len(ptmp[0])+1:]
        color.cprint("mst",GREY,0)
        color.cprint("%s["%pt,WHITE,0)
        color.cprint(pplu,RED,0)
        color.cprint("]",WHITE,0)
    def pluhelp(self):
        '''plugin help menu'''
        color.cprint('PLUGIN HELP MENU',YELLOW)
        color.cprint('================',GREY)
        color.cprint('        Command         Description',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        help            Displays the plugin menu
        back            Back to Mst Main
        cls             Clear the screen
        info            Displays the plugin info
        opts            Displays the mst options
        set             Configure the plugin parameters
        exploit         Start plugin to exploit''',CYAN)
        color.cprint('PLUGIN SET HELP',YELLOW)
        color.cprint('===============',GREY)
        color.cprint('        Command         Description',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        PAYLOAD         Set payload
        <PARAMETER>     Set parameter''',CYAN)
    def cls(self):
        '''clear the screen'''
        if  name == 'nt':
            system("cls")
        else:
            system("clear")
    def load(self):
        color.cprint("[?] USAGE::load <loadPlu>",YELLOW)
if __name__ == '__main__':
    print __doc__

