import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
passw=xbmcplugin.getSetting(int(sys.argv[1]), 'passw')
ADDON = xbmcaddon.Addon(id='plugin.video.password')
AddonID = 'plugin.video.password'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
#                             V-----------  where youu extracted Your PHP.zip Files
BASE = "http://mykodi.co.uk/password"
check=urllib.urlopen('%s/hidden.php?password=%s'% (BASE,passw)).read()
playlist=urllib.urlopen('%s/playlist.php?password=%s'% (BASE,passw)).read()

def CATEGORIES():
        if check == "Wrong":
            addDir2('Sorry Password Wrong','updates',4,'')
        else:
            addLink('Channels','%s'%(playlist),'','')
def PASSWORD():
        searchString = addSearch()
        ADDON.setSetting('passw',searchString)
        xbmc.executebuiltin('Container.refresh')
                       
             
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


def addSearch():
	searchStr = ''
	keyboard = xbmc.Keyboard(searchStr, 'Enter Password')
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
    UpdateMe()
elif mode==4:
    PASSWORD()



xbmcplugin.endOfDirectory(int(sys.argv[1]))
