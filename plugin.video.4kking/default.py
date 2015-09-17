import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
addon_id='plugin.video.4kking'
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
baseurl = 'dummy'
net = Net()

BASE = "http://mykodi.co.uk/kodi"
def CATEGORIES():
        addDir('3D HD','http://mykodi.co.uk/kodi/3d.php',3,'')
        addDir('3D HD Live  -  [I]Coming Soon[/I]','http://mykodi.co.uk/kodi/3dc.php',3,'')
        addDir('4K','http://mykodi.co.uk/kodi/4k.php',3,'')
        addDir('4K Live','http://mykodi.co.uk/kodi/4kc.php',6,'')
        addDir('HD Movies','http://mykodi.co.uk/kodi/files.php',3,'')
        
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def VOD(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
                addDir('%s'%(name).replace('4k','[COLOR gold]4K[/COLOR]').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),5,'%s'%(iconimage))
def kLive(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
                addDir2('%s'%(name).replace('4k','[COLOR gold]4K[/COLOR]').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),4,'%s'%(iconimage))
def VOD2(url):
        thelink=urllib.urlopen('%s'%(url)).read()
        vidlocation=('%s'%(url))
        link = OPEN_URL(url)
        match=re.compile('<span.style="display:none;".id=".+?"><a.href="(.+?)".class="btn.btn.primary"><strong>FREE.DOWNLOAD</strong>Click.to.start.Download</a></span>').findall(link)
        for url in match:
                addDir2('[COLOR gold]Duel Audio Change To English[/COLOR]','%s'%(thelink),4,'%s'%(iconimage))				
                addDir2('Play Now','%s'%(url),4,'%s'%(iconimage))				
def RESOLVE(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    dp.update(10)
    xbmc.sleep(1000)
    dp.update(20)
    xbmc.sleep(1000)
    dp.update(30)
    xbmc.sleep(1000)
    dp.update(40)
    xbmc.sleep(1000)
    dp.update(50)
    play=xbmc.Player(GetPlayerCore())
    dp.update(60)
    url=urlresolver.HostedMediaFile(url).resolve() 
    dp.update(75)
    xbmc.sleep(1000)
    dp.update(85)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working    
        dp.update(100)
        dp.close()
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        dp.update(90)
        xbmc.sleep(1000)
        dp.update(100)
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()
     
def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('file: "(.+?)",').findall(link)
        for url in match:
                addLink(name,url,'',"")
        

                
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
        liz.setProperty('IsPlayable','true')
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 

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
        
              
params=get_params()
url=None
name=None
iconimage=None
mode=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
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
        VOD(url)
elif mode==4:
        RESOLVE(url)
elif mode==5:
        VOD2(url)
elif mode==6:
        kLive(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
