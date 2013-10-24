# -*- coding: cp936 -*-
'''
Mst=>Plugin=>Scan_ip_port
'''

class mstplugin:
    '''this is scan_ip_port's class :)'''
    infos = [
        ['插件','简单IP端口扫描单线程版'],
        ['作者','mst'],
        ['版本','1.0'],
        ['更新','20131022'],
        ['网址','http://mstoor.duapp.com']
        ]
    opts  = [
        ['RHOST','127.0.0.1','要扫描的IP'],
        ['PAYLOAD','false','不需要后攻击插件']
        ]
    ports = [
        ['21','FTP'],
        ['22','SSH'],
        ['23','TELNET'],
        ['25','SMTP'],
        ['80','HTTP'],
        ['135','SMB'],
        ['139','SMB'],
        ['443','HTTPS'],
        ['445','SMB'],
        ['1080','PROXY'],
        ['1433','MSSQL'],
        ['1723','VPN'],
        ['3306','MYSQL'],
        ['3389','MSTSC'],
        ['5432','POSTGRE'],
        ['8080','PROXY']
        ]
    def exploit(self):
        '''plugin exploit '''
        color.cprint("    %-32s %-8s %-10s %-20s"%("RHOST","PORT","STATUE","DESCRIPTION"),YELLOW)
        color.cprint("    %-32s %-8s %-10s %-20s"%("-"*32,"-"*8,"-"*10,"-"*20),GREY)
        #ths=[]
        for p in self.ports:
            port = p[0]
            desc = p[1]
            def th():
                if fuck.checkport(RHOST,port):
                    color.cprint("    %-32s %-8s %-10s %-20s"%(RHOST,port,"OPEN",desc),GREEN)
                else:
                    color.cprint("    %-32s %-8s %-10s %-20s"%(RHOST,port,"CLOSE",desc),WHITE)
            th()
        
