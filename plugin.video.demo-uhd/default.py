import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os


#LiveLeak.com- by Oneadvent 2012.
BASE = "http://www.liveleak.com/"
def CATEGORIES():
        link = OPEN_URL('http://demo-uhd3d.com/categorie.php')
        match=re.compile('<li><a href=\'http:\/\/demo-uhd3d.com\/categorie\.php\?tag=(.+?)\'>(.+?)<\/a>').findall(link)
        for url,name in match:
            addDir(name,'http://demo-uhd3d.com/categorie.php?tag=%s'%url,3,url)
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
def MEDIAITEMS(url):
        link = OPEN_URL(url)
        match=re.compile('href=\'(.+?)\' title=\'(.+?)\'><img src=\'images\/vignettes\/(.+?)vignette.jpg\'').findall(link)
        for id,name,image in match:
            addDir2('%s'%(name),'http://demo-uhd3d.com/%s'%(id),4,'http://demo-uhd3d.com/images/captures/%slarge.jpg'%image)
def PLAYVIDEO(url,name):
        dialog = xbmcgui.Dialog()
        link = OPEN_URL(url)
        match=re.compile('\'\/files\/(.+?)\.ts\'').findall(link)
        match2=re.compile('\'\/files\/(.+?)\.mvk\'').findall(link)
        match3=re.compile('\'\/files\/(.+?)\.mp4\'').findall(link)
        match4=re.compile('\'\/files\/(.+?)\.zip\'').findall(link)
        for url in match:
            play=xbmc.Player(GetPlayerCore())
            dp = xbmcgui.DialogProgress()
            dp.create('Opening ','Opening %s '%(name))
            dp.update(10)
            play.play('http://demo-uhd3d.com/files/%s.ts'%url)
            dp.update(100)
            dp.close()
        for url in match2:
            play=xbmc.Player(GetPlayerCore())
            dp = xbmcgui.DialogProgress()
            dp.create('Opening ','Opening %s '%(name))
            dp.update(10)
            play.play('http://demo-uhd3d.com/files/%s.mvk'%url)
            dp.update(100)
            dp.close()
        for url in match3:
            play=xbmc.Player(GetPlayerCore())
            dp = xbmcgui.DialogProgress()
            dp.create('Opening ','Opening %s '%(name))
            dp.update(10)
            play.play('http://demo-uhd3d.com/files/%s.mp4'%url)
            dp.update(100)
            dp.close()
        for url in match4:
            if dialog.yesno("Download", 'Do you Wish To Download','', "",'No','Yes'):
                ADDON = xbmcaddon.Addon(id='plugin.video.demo-uhd')
                AddonID = 'plugin.video.demo-uhd'
                Addon = xbmcaddon.Addon(AddonID)
                addonDir = Addon.getAddonInfo('path').decode("utf-8")
                play=xbmc.Player(GetPlayerCore())
                dp = xbmcgui.DialogProgress()
                dp.create('UPDATING')
                import zipfile 
                url = "http://demo-uhd3d.com/files/%s.zip"%(url)
                localfile = os.path.join(addonDir,'hello.zip')
                urllib.urlretrieve(url,localfile,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
                if dp.iscanceled(): 
                    percent = 100
                    dp.update(percent)
                    print "DOWNLOAD CANCELLED" # need to get this part working
                    dp.close()
                zin = zipfile.ZipFile(localfile, 'r')
                zin.extractall(addonDir)
                dp.update(100)
                dp.close()
            else:
                return
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
        percent = 100
        dp.update(percent)
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
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
        MEDIAITEMS(url)
elif mode==4:
        PLAYVIDEO(url,name)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
