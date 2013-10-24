from os import listdir

ftype = raw_input("PARAMETER >")
if len(ftype)>0:
    tmp=listdir("output")
    color.cprint("[*] CHOOSE `%s` FLIST [ID].."%ftype,YELLOW)
    for i in range(len(tmp)):
        color.cprint("[%s] %s"%(i,tmp[i]),PURPLE)
    lf = raw_input("ID >")
    try:
        ii = int(lf)
        ff = tmp[ii]
        if len(lf)>0:
            flist = open("output/%s"%ff).readlines()
            for f in flist:
                f = f.strip("\n")
                f = f.replace("http://","")
                mm.setp(ftype,f)
                mm.exploit()
    except Exception,e:
        color.cprint("[!] ERR:%s"%e,RED)
else:
    color.cprint("[?] Ex.RURL",RED)
