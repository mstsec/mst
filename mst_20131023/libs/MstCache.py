# -*- coding: utf-8 -*-
'''
MstCache=>class
For main's some func or other~
update:2013/10/21
'''

from    MstColor   import *
from    sqlite3    import *
from    os         import listdir,system
from    random     import choice
from    MstLoad    import load
from    MstUpdate  import nver,seru

mstdb   = 'cache/mst.cache'
plugp   = 'plugins/'
p_exp   = 'exploit'
p_pay   = 'payload'
p_mul   = 'multi'
mstcs   = 'mst'

class cache:
    '''MstCache=>Class::cache'''
    def start(self):
        '''start cache'''
        color.cprint("[*] Start mst ..",GREEN)
        self.runsql("create table if not exists mst(id integer primary key,type text,path text)")
        self.runsql("delete from mst")
        self.inscache(self.getplus(p_exp),p_exp)
        self.inscache(self.getplus(p_pay),p_pay)
        self.inscache(self.getplus(p_mul),p_mul)
        self.banner()
        
    def inscache(self,c,p):
        '''insert data to cache'''
        for tmp in c:
            tmp=tmp[:len(tmp)-3]
            self.runsql('insert into mst(type,path) values("%s","%s/%s")'%(p,p,tmp))
            
    def runsql(self,sql):
        '''execute a sql'''
        conn=connect(mstdb)
        conn.execute(sql)
        conn.commit()
        conn.close()
        
    def getplus(self,path):
        '''get plugins list'''
        return listdir(plugp+path)
    
    def sql_all(self,sql):
        '''sqlite3=>cur.fetchall()'''
        conn=connect(mstdb)
        cur=conn.cursor()
        cur.execute(sql)
        tmp=cur.fetchall()
        cur.close()
        conn.close()
        return tmp
    
    def search(self,sear):
        '''search plugins'''
        sql='select * from mst where path like "%'+sear+'%"'
        result=self.sql_all(sql)
        msg="SEARCH '%s'"%sear
        color.cprint(msg,YELLOW)
        color.cprint("="*len(msg),GREY)
        self.listmst(result)
        
    def listmst(self,result):
        '''format print results'''
        color.cprint("%5s %-60s %-7s"%("ID","PATH","TYPE"),YELLOW)
        color.cprint("%5s %-60s %-7s"%("-"*5,"-"*60,"-"*7),GREY)
        for res in result:
            rid=res[0]
            rty=res[1]
            rpa=res[2]
            if len(rpa)>70:
                rpa=rpa[:68]+".."
            color.cprint("%5s %-60s %-7s"%(rid,rpa,rty),CYAN)
        color.cprint("="*74,GREY)
        color.cprint("COUNT [%s] RESULTS (*^_^*)"%len(result),GREEN)
        
    def showplus(self,p):
        '''show plugins'''
        pp=("show %s plugins"%p).upper()
        color.cprint(pp,YELLOW)
        color.cprint("="*len(pp),GREY)
        if p == 'all':
            sql='select * from mst'
        else:
            sql="select * from mst where type='%s'"%p
        self.listmst(self.sql_all(sql))

    def load(self,plugin):
        '''load plugins'''
        def getplu(pid):
            '''pid 2 pluName'''
            conn=connect(mstdb)
            cur=conn.cursor()
            cur.execute('select * from mst where id=%s'%pid)
            tmp=cur.fetchone()
            cur.close()
            conn.close()
            pat=tmp[2]
            pty=tmp[1]
            if pty == 'payload':
                return ''
            else:
                return pat
        def noload(p=0):
            '''no this plugin | plugin is payload'''
            if p == 0:
                color.cprint("[!] NO THIS PLUGIN !",RED)
            else:
                color.cprint("[!] IT'S A PAYLOAD !",RED)
        try:
            pid=int(plugin)
            if len(self.sql_all('select * from mst where id=%s'%pid))==0:
                noload()
            else:
                plu=getplu(pid)
                if len(plu)>0:
                    pt=plu.split("/")[0]
                    load.start(pt,plu)
                else:
                    noload(1)
        except:
            if len(self.sql_all('select * from mst where path="%s"'%plugin))==0:
                noload()
            else:
                pt=plugin.split("/")[0]
                load.start(pt,plugin)
                
    def getplunums(self,p):
        '''get plugins nums'''
        if p == 'all':
            return len(self.sql_all('select * from mst'))
        else:
            return len(self.sql_all('select * from mst where type="%s"'%p))

    def mainhelp(self):
        '''show mainhelp'''
        color.cprint('MST HELP MENU',YELLOW)
        color.cprint('=============',GREY)
        color.cprint('        COMMAND         DESCRIPTION',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        help            Displays the help menu
        exit            Exit the MstApp
        cls             Clear the screen
        show            List the plugins
        search          Search plugins
        use             Use the plugin
        update          Update mst|plugins''',CYAN)
        color.cprint('MST HELP::SHOW',YELLOW)
        color.cprint('==============',GREY)
        color.cprint('        COMMAND         DESCRIPTION',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        exploit         List the exploit plugins
        payload         List the payload plugins
        multi           List the multi plugins
        all             List all the plugins''',CYAN)

    def usage(self,c):
        '''mst=>usage'''
        def ius(c):
            '''def's def =.='''
            color.cprint('[?] USAGE:%s'%c,YELLOW)
        if   c == "search":
            ius('search <plugin>')
        elif c == "show":
            ius('show <exploit|payload|multi|all>')
        elif c == "use":
            ius('use <plugin|pluginID>')
        elif c == "update":
            ius('update <mst|plugins>')
                        
    def ban1(self):
        '''banner 1'''
        color.cprint('''
             ,,          ,      r22r   r::,,:iii   
             B@B       ,@@2   @B@GB@@ rB@B@B@B@B   
             @H@s      @X@s  @B           X@       
             @:,@,    @G Bs  i@B:         GB       
             @r M@   GB  @s    XB@Br      G@       
             Bs  B@ iB,  @s       sB@     MB       
             @s   BSBs   @s        2Bi    M@       
             B9   ;B@   ,BH  B@BMG@BG     @B       
             :     ,     :    ,r22i       ,:
            ''',RED)
    def ban2(self):
        color.cprint('''
                                                                    
                                   ,i77SSXrr,     ,ii               
                            7aWMMMMMMMMMMMMMMMMMMMMMMM              
                        7@MMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                       :MMMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                        WMMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                        ,MMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                         ,MMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                          @MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                          XMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           BMMMMMMMMMMMMMMMMMMMMMMMMMMr             
                           SMMMMMMMMMMMMMMMMMMMMMMMMMMM             
                           iMMMMMMMMMMMMMMMMMMMMMMMMMMMX         7; 
                            MMMMM@B8Z2SXXr;;;:,.,,. . . ,;XZBMMMMMM:
                            S7,.   ..::ii;;7XXX2ZBB@MMMMMMMMMMMMMMMi
                      .:;72aZ8B@MMMMMMMMMMMMMMMMMMMMMMMMMMBaXi.     
              BMMMMMMMMMMMMMMMMMMMMM8a22SXrr;i,:rZZZi               
              XMMMMMWB0Za2X;,:MMMMMWS          7WM.             
                 
''',BLUE)
    def ban3(self):
        color.cprint('''
                                        ,-,                     
                                   -x#######=                   
                                =########XX##+                  
                             .x#########XxXx#x=                 
                            X###########XxxXX#=-                
                          .##########X####Xxxxx=                
                          =###XXxX+xX#X##########x=-            
                          +#XxxX#######################=.       
                         -###########X++x+--;+x###########-     
                       =#########X;.  .         ;-X#########.   
                     +#########+,    ,      ,   .  ;#########   
                   -#########- .    -      -.   ..  ;+#######,  
                  =########+,      =;.    --     -  ..=#####+   
                 .########-    .; =;    ,+- .   X ;  ,.X##x     
                 +#######+ ;   -.-.    =+.    .#. = , .#x       
                 ,#######----  = ,   ;+,    .x# ,X, - ;x#       
                  .#######+--= =    ==   ;=-,, -X#===.x=##      
                     ;+X#=-x+=;-  X#+,.,+++X=-#;  ,;;x+#-.-     
                        -   ####x#==--+-., X-.X;=#+; =x#        
                       .; -+-##. -  X##=   =  .,X#+  -#,        
                        =     x   +       ,.   ;     x=         
                         ;-,, +    -;...,.       ..;-x          
                            .##=                     x          
                             +  =                   -;          
                                 +                -+.           
                                  =X+,.        ,==,   
                                           ''',CYAN)
    def ban4(self):
        color.cprint('''
                             .;+it+;+tt=:                       
                          .iYi;=YY   .IXXXI;                    
                        :IXV,     iX   t+iRBV,                  
                       IVItY  ,#; =#     ,  Y#=                 
                     .XIttIt,  Mi.XV#I ,; ,.  :i                
                     RttYI,  .   :###Y  ,;..., +:               
                    YItI=  .,,:    .           =: :::           
                    Xtt+ ...             :=Y#I .i;,,:+,         
                    RtI      ,=itYRM#########   V     I         
                    XIt  ::#################;  ;R,   =;         
                    iYI    B###BRXVYVVVVBW#X   tVItiV.          
                     VIi    +BBRVVVVVVYVVBI    ItttB:           
                  ::,.YY;     +XWMMRRRRBB;    tttiVi            
                ,+,. ,:iV=       ;iIIIII:,IM##XtiYY             
                t.    ,tXBt.       :IRMt=XR,  tIYI              
                ,+.   +titIYt;=RW#WRt;:;;M=    Vt .;::          
                 .;;=YRItittttXBX:     ,:::   ,;V,,..,+;        
                      ,iYVItttitt             ;,=      +;       
                         ,iYVItiI ,           :         t       
                            .;Ytt; ;        .,.t        =:      
                              :VtI; ...   ..,:IY        i.      
                              ;YttII=;:::;=iIIIIt      :+       
                             = ItittttIIIIIYXVYYVY=:::==        
                            :; tIttttttIYXI=,      ,,,          
                            =:  tYIIIIVI=                       
                            ,+   .,:.i,                         
                             ==     ;,                          
                              ,;;;;:                            
''',PURPLE)
    def banner(self):
        '''mst banner :)'''
        en=self.getplunums('exploit')
        pn=self.getplunums('payload')
        mn=self.getplunums('multi')
        choice([self.ban1,self.ban2,self.ban3,self.ban4])()
        print '          =[',
        color.cprint('MST::My Sec Tools',GREEN)                  
        print '        -+=[',
        color.cprint('VER::%s::%s'%(nver,seru),CYAN)                
        print '    + -- +=[',
        color.cprint('PLU::Exploits::%s Payloads::%s Multis::%s'%(en,pn,mn),YELLOW)
        
    def printmst(self):
        '''print mst..'''
        global mstcs
        color.cprint(mstcs,GREY,0)
        
    def execmd(self,cmd):
        '''run system command'''
        color.cprint('[*] EXEC:%s'%cmd,RED)
        system(cmd)
        
    def cls(self):
        '''clear'''
        if name == 'nt':
            system("cls")
        else:
            system("clear")

    def errmsg(self,msg):
        '''show error msg'''
        color.cprint("[!] Err:%s"%msg,RED)
        
    def mainexit(self):
        '''exit app'''
        color.cprint("\n[*] GoodBye :)",RED)
        exit(0)

if __name__=='__main__':
    print __doc__
else:
    cache=cache()
    #cache.start()
