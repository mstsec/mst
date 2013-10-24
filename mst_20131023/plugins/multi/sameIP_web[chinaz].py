# -*- coding: cp936 -*-
class mstplugin:
    '''同IP网站查询::tool.chinaz.com/same版'''
    infos = [
        ['插件名称','同IP网站查询[chinaz]版'],
        ['插件作者','mst'],
        ['更新日期','2013/10/23'],
        ['作者网站','http://mstoor.duapp.com']
        ]
    opts  = [
        ['RURL','mstoor.duapp.com','要查询的目标网址'],
        ['PAYLOAD','false','不需要后攻击插件']
        ]
    def exploit(self):
        '''开始查询'''
        chinaz = 'http://tool.chinaz.com/Same/'
        value  = {'s':RURL}
        try:
            color.cprint("[*] Sending data..",YELLOW)
            tmp    = fuck.urlpost(chinaz,value).read()
            color.cprint("[+] Formate data..",YELLOW)
            tmp    = tmp.decode("utf-8")
            res    = fuck.find('.</span> <a href=[^>]+ target=_blank>',tmp)
            reslen = len(res)
            resiii = 1
            reslog = "sameIP_web[chinaz]_%s"%RURL
            for r in res:
                tmp= r[18:]
                tmp= tmp.split("'")
                ok = tmp[0]
                color.cprint("[%s/%s] %s"%(resiii,reslen,ok),GREEN)
                fuck.writelog(reslog,ok+"\n")
                resiii+=1
            color.cprint("[*] Get data Successful !LOG:output/%s.log"%reslog,CYAN)
        except Exception,e:
            color.cprint("[!] Err:%s"%e,RED)
