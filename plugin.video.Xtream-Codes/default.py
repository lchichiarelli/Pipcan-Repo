# All Coding Done By Pipcan See http://mykodi.co.uk or facebook http://facebook.co.uk/kodicontrol or skype:pipcan2015
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
# V-- Reads The /resources/settings.xml This I The Username --V
usern=xbmcplugin.getSetting(int(sys.argv[1]), 'usern')
# V-- Reads The /resources/settings.xml This I The Password --V
passw=xbmcplugin.getSetting(int(sys.argv[1]), 'passw')
# V-- Reads The /resources/settings.xml This I The Website --V
site=xbmcplugin.getSetting(int(sys.argv[1]), 'site')
# V-- Reads The /resources/settings.xml This I The PORT --V
port=xbmcplugin.getSetting(int(sys.argv[1]), 'port')
# V-- Reads The /resources/settings.xml This I The Type --V
type=xbmcplugin.getSetting(int(sys.argv[1]), 'type')
# V-- This Is For Web Login Successful Hide The Login Button 
active=xbmcplugin.getSetting(int(sys.argv[1]), 'active')
source=xbmcplugin.getSetting(int(sys.argv[1]), 'source')
# V-- This Is For Web Login Successful Hide The Login Button 
source2 = ('http://infadroid.tk/epg/guia.xml')
'''                          V----The Addon Name----V'''
ADDON = xbmcaddon.Addon(id='plugin.video.Xtream-Codes')
'''        V----The Addon Name----V'''
AddonID = 'plugin.video.Xtream-Codes'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
#Created By Pipcan.
fetch_url = ""
date= datetime.datetime.today().strftime('%Y%m')
time= datetime.datetime.today().strftime('%H%M%S')
def CATEGORIES():
#       V-----------------V This is a function that when a user logges in to reveal bellow directorys
        if active =="true":
            addDir('[COLOR yellow]LOGGED IN AS:[/COLOR]  %s'%(usern),'%s:%s/panel_api.php?username=%s&password=%s'%(site,port,usern,passw),6	,'')
            addDir('My Account','%s:%s/panel_api.php?username=%s&password=%s'%(site,port,usern,passw),6,'')
            addDir('Live','%s:%s/panel_api.php?username=%s&password=%s'%(site,port,usern,passw),5,'')
            addDir('Video On-Demand','%s:%s/panel_api.php?username=%s&password=%s'%(site,port,usern,passw),4,'')
            addDir2('Settings','settings',7,'')
#       V---V If User Not Logged In Show Login Button
        else:
            addDir('Click To Login','%s:%s/panel_api.php?username=%s&password=%s'%(site,port,usern,passw),3,'')

def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Magic Browser")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def VOD(url):
        vidlocation=('%s:%s/movie/%s/%s/'%(site,port,usern,passw))
        link = OPEN_URL(url)
        match=re.compile('{"name":"(.+?)","stream_id":"(.+?)".+?container_extension":"(.+?)","stream_icon":"(.+?)",".+?"epg_data":.+?plot":(.+?)",".+?releasedate":"(.+?)"').findall(link)
        for name,streamid,container,iconimage,plot,year in match:
                addLink3('[COLOR yellow]%s[/COLOR]%s'%(name,year),'%s%s.%s'%(vidlocation,streamid,container),'','%s'%(iconimage).replace("\/","/"),'','%s'%(plot))				
def EPG(name,url):
        epglocation=xbmcplugin.getSetting(int(sys.argv[1]), 'file')
        addLink(' %s  [I]Click To Watch[/I]'%(name),'%s'%(url),'','')
        addLink(' [COLOR green]Programme Ended[/COLOR] - [COLOR red]Programme Not Started[/COLOR]','','','')
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        if source == "Downloaded":
            epglocation2 = 'file:///%s'%(epglocation)
        else:
            epglocation2 = ('%s'%(source2))
        link = OPEN_URL(epglocation2)
        match = re.compile('start="%s10(.+?)\s.+?".+?channel="%s">.+?\n.+?<title lang=".+?">(.+?)</title>.+?\n.+?<desc lang=".+?">(.+?)<'%(date,name)).findall(link)
        for start,prog,desc in match:
                if start > "%s"%(time):
                    addLink3('%s - [COLOR red]%s[/COLOR] '%(start,prog),'','','','','%s'%(desc))
                else:
                    addLink3('%s - [COLOR green]%s[/COLOR] '%(start,prog),'','','','','%s'%(desc))			
        addLink('zzz[COLOR blue]END OF LISTINGS[/COLOR]','','','')
def LIVE(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s:%s/live/%s/%s/'%(site,port,usern,passw))
        link = OPEN_URL(url)
        match=re.compile('{"name":"(.+?)","stream_id":"(.+?)".+?"live":"1".+?icon":"(.+?)"').findall(link)
        for name,url,iconimage in match:
                addLink('%s'%(name),'%s/%s.ts'%(vidlocation,url,),'%s'%(iconimage).replace("\/","/"),'')        

def ACCOUNT(url):
        addDir2('[COLOR green]Download EPG[/COLOR]','%s'%(source2),9,'')
        link = OPEN_URL(url)
        match=re.compile('"username":"(.+?)"').findall(link)
        match1=re.compile('"status":"(.+?)"').findall(link)
        match2=re.compile('"exp_date":"(.+?)"').findall(link)
        match3=re.compile('"active_cons":"(.+?)"').findall(link)
        match4=re.compile('"created_at":"(.+?)"').findall(link)
        match5=re.compile('"max_connections":"(.+?)"').findall(link)
        match6=re.compile('"allowed_output_formats":(.+?)}').findall(link)
        for url in match:
                addDir2('[COLOR green]ACCOUNT INFOMATION[/COLOR]','','','')
                addDir2('[COLOR yellow]Username:                       [/COLOR][I]%s[/I]'%(url),'','','')
        for url in match1:
                addDir2('[COLOR yellow]Status:                            [/COLOR][I]%s[/I]'%(url),'','','')
        for url in match4:
                addDir2('[COLOR yellow]Created:                        [/COLOR][I]%s[/I]'%(url),'','','')
        for url in match2:
                addDir2('[COLOR yellow]Expires:                         [/COLOR][I]%s[/I]'%(url),'','','')
        for url in match3:
                addDir2('[COLOR yellow]Active Connection:          [/COLOR][I]%s[/I]'%(url),'','','')
        for url in match5:
                addDir2('[COLOR yellow]Max Connection:           [/COLOR][I]%s[/I]'%(url),'','','')
        for url in match6:
                addDir2('[COLOR yellow]Avalible Formats:          [/COLOR][I]%s[/I]'%(url),'','','')
# This Funtion Is For Opening The Settings Panel
def openSettings():
    ADDON.openSettings()

def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("Getting EPG","Downloading")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
def GRABEPG(url):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Download EPG", 'Do you Wish To Download EPG','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading EPG')
        url = ("%s"%(source2))
        localfile = os.path.join(addonDir,"resources/epg.xml")
        urllib.urlretrieve(url,localfile,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
    else:
        return	
def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('file: "(.+?)",').findall(link)
        for url in match:
                addLink(name,url,'',"")
        
def SIGNIN():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Get Your Login Info Ready", 'Do you Wish To Sign In','', "",'Cancel','Sign In'):
        email=Search('username')
        ADDON.setSetting('usern',email)
        xbmc.executebuiltin('Container.Refresh')
        password=Search('Password')
        ADDON.setSetting('passw',password)
        xbmc.executebuiltin('Container.Refresh')
        login=urllib.urlopen('%s:%s/panel_api.php?username=%s&password=%s'%(site,port,email,password)).read()
        if login == '{"user_info":{"auth":0}}':
            dialog.ok("Error!", "Details Were Incorrect!")
            return
        else:
            xbmc.executebuiltin('Container.Refresh')
            dialog.ok("Success!", " Thank You %s  Enjoy!"%(usern))
            ADDON.setSetting('active','True')

            return
    else:
        return
def Search(name):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Please Enter '+str(name))
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')
            if search_entered == 0:
                return False          
        return search_entered
        if search_entered == None:
            return False   

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage,urlType):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        menu=[]
        menu.append(('[COLOR yellow]EPG[/COLOR]','Container.update(%s?mode=8&name=%s&url=%s)'% (sys.argv[0],name,url)))
        liz.setProperty('IsPlayable','true')
        liz.addContextMenuItems(items=menu, replaceItems=True)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addSearch():
	searchStr = ''
	keyboard = xbmc.Keyboard(searchStr, 'Search')
	keyboard.doModal()
	if (keyboard.isConfirmed()==False):
	  return
	searchStr=keyboard.getText()
	if len(searchStr) == 0:
	  return
	else:
	  return searchStr
	  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
def addLink3(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
    print ""+url
    INDEX(url)

elif mode==2:
    print ""+url
    addSearch()

elif mode==3:
    SIGNIN()

elif mode==4:
    VOD(url)

elif mode==5:
    LIVE(url)

elif mode==6:
    ACCOUNT(url)

elif mode==7:
        openSettings()
elif mode==8:
    name=name.replace('%20',' ')
    EPG(name,url)
elif mode==9:
    GRABEPG(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
