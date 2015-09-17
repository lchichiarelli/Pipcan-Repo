import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,datetime
AddonID = 'plugin.video.musicvideos'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
HOME       =  xbmc.translatePath('special://home/addons/%s/channels.txt'%(AddonID))
def CATEGORIES():
        addDir('SKY','http://liriklagump3.info',4,'')
def CATS(url):
        link = OPEN_URL(url)
        match=re.compile('<a class=colr href=(.+?)>(.+?)</a>').findall(link)
        for url,name in match:
            addDir('[COLOR yellow]%s[/COLOR]'%(name),'http://liriklagump3.info%s'%(url),5,'')

def CATS2(url):
        link = OPEN_URL(url)
        match=re.compile('<img width=100 src=(.+?)\salt="(.+?)" title=".+?">').findall(link)
        for image,name in match:
            addDir('[COLOR yellow]%s[/COLOR]'%(name),'',4,image)

def PLAYVIDEO(url,channelno):
    link = OPEN_URL('file:///%s/channels.txt'%(addonDir))
    match = re.findall('%s":".+?":"(.+?)"'%(channelno), link)
    for url in match:
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Opening ','Opening %s '%(channelno))
        dp.update(10)
        play.play(url)
        dp.update(100)
        dp.close()
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
def PLAYVIDEO2(url,name):
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Opening ','Opening %s '%(name))
        dp.update(10)
        play.play(url)
        dp.update(100)
        dp.close()
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("Iptv Manager","Downloading")
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
			
def RESOLVE(url): 
    import urlresolver
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    try: play.play(url)
    except: pass
    try: ADDON.resolve_url(url) 
    except: pass 
def RESOLVE2(url): 
    play=xbmc.Player(GetPlayerCore())
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    dp.update(10)
    play.play(url)
    dp.update(100)
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

def addLink(name,url,iconimage,plot):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
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
def addDir3(name,url,mode,iconimage,channelno):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&channelno="+urllib.quote_plus(channelno)
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
def addDir4(name,url,mode,iconimage,channelno):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&channelno="+urllib.quote_plus(channelno)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
def addDir5(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
               
params=get_params()
url=None
name=None
iconimage=None
mode=None
plot=None
channelno=None
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
        plot=urllib.unquote_plus(params["plot"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        channelno=urllib.unquote_plus(params["channelno"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Plot: "+str(plot)
print "channelno: "+str(channelno)
print "IconImage: "+str(iconimage)
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        INDEX(url)
        
elif mode==2:
        print ""+url
        addSearch()

elif mode==4:
          CATS(url)
elif mode==5:
          CATS2(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
