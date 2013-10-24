# -*- coding: cp936 -*-
'''
Mst=>multi=>plugin
'''
class mstplugin:
    '''crack sub_domain'''
    infos = [
        ['插件','爆破二级域名辅助工具'],
        ['作者','mst'],
        ['更新','2013/10/21'],
        ['网址','http://mstoor.duapp.com']
        ]
    opts  = [
        ['DOMAIN','google.com','要爆破的顶级域名'],
        ['SUBDIC','dicts/sub_domain.lst','爆破二级域名的字典路径'],
        ['PAYLOAD','false','不需要后攻击插件']
        ]
    def exploit(self):
        dicts=open(SUBDIC).readlines()
        color.cprint("SCANN %s =>SUB DOMAINS"%DOMAIN.upper(),YELLOW)
        color.cprint("===================="+"="*len(DOMAIN),GREY)
        color.cprint("%-35s %-25s %-10s"%("FULL DOMAIN","RESULT","SCHEDULE"),YELLOW)
        color.cprint("%-35s %-25s %-10s"%("-"*35,"-"*25,"-"*10),GREY)
        ll = len(dicts)
        li = 1
        for dic in dicts:
            sub    = dic.strip("\n")
            domain = sub+"."+DOMAIN
            try:
                res = fuck.urltoip(domain)
                log="%-35s %-25s %-10s"%(domain,res,"%s/%s"%(li,ll))
                color.cprint(log,GREEN)
                fuck.writelog('sub_domain_%s'%DOMAIN,log)
            except:
                color.cprint("%-35s %-25s %-10s"%(domain,"ERROR","%s/%s"%(li,ll)),RED)
            li += 1
        color.cprint("[*] ALL SCAN DONE ! SAVE TO output/sub_domain_%s.log!"%DOMAIN,YELLOW)
