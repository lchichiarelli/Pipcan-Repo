# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
ADDON = xbmcaddon.Addon(id='plugin.video.msn')
AddonID = 'plugin.video.msn'
Addon = xbmcaddon.Addon(AddonID)
# Edit line below
addonDir = Addon.getAddonInfo('path').decode("utf-8")
bingurl = 'http://prod.video.msn.com/tenant/amp/entityid/'
bingimage='http://img-s-msn-com.akamaized.net/tenant/amp/entityid/AAbGK17.img'
def CATEGORIES():
            addDir('Search Bing Videos','http://www.msn.com/en-us/video/searchresults?q=',37,'')

def addSearch(searchStr):
	searchStr = searchStr
	keyboard = xbmc.Keyboard(searchStr, 'Search')
	keyboard.doModal()
	if (keyboard.isConfirmed()==False):
	  return
	searchStr=keyboard.getText()
	if len(searchStr) == 0:
	  return
	else:
	  return searchStr
def openSettings():
    ADDON.openSettings()
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def BING(url):
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr, 'Search')
        keyboard.doModal()
        searchStr=keyboard.getText()
        link = OPEN_URL('%s%s&page=1&ver=2.0.5714.29282'%(url,searchStr))
        match=re.compile('<a href="/en-us/video/watch/.+?/vi-(.+?)"  >\n <div class="imgcontainer">\n.+?<img alt="(.+?)".+?entityid/(.+?).img').findall(link)
        match2=re.compile('<a class="nexturl" href="http://www.msn.com:80/en-us/video/searchresults\?q=(.+?)&amp;page=(.+?)&.+?">(.+?)</a>').findall(link)
        for id,name,id2 in match:
            addDir2('%s'%name,'http://prod.video.msn.com/tenant/amp/entityid/%s?blobrefkey=103&$blob=1'%(id),9,'http://img-s-msn-com.akamaized.net/tenant/amp/entityid/%s.png'%id2)
        for q,page,name in match2:
            addDir('%s'%name,'http://www.msn.com:80/en-us/video/searchresults?q=%s&page=%s&ver=2.0.5714.29282'%(q,page),1000,'')
def BING2(url):
        link = OPEN_URL('%s'%(url))
        match=re.compile('<a href="/en-us/video/watch/.+?/vi-(.+?)"  >\n <div class="imgcontainer">\n.+?<img alt="(.+?)".+?entityid/(.+?).img').findall(link)
        match2=re.compile('<a class="nexturl" href="(.+?)">(.+?)</a>').findall(link)
        for id,name,id2 in match:
            addDir2('%s'%name,'http://prod.video.msn.com/tenant/amp/entityid/%s?blobrefkey=103&$blob=1'%(id),9,'http://img-s-msn-com.akamaized.net/tenant/amp/entityid/%s.png'%id2)
        for url,name in match2:
            addDir('%s'%name,url,1000,'')

def PLAYVIDEO(url,name):
    import urlresolver
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    play.play(url)
def PLAYVIDEO2(url,name):
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    play=xbmc.Player(GetPlayerCore())
    play.play(url)

	
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
elif mode==4:
        PLAYVIDEO(url,name)
elif mode==9:
        PLAYVIDEO2(url,name)
elif mode==37:
        BING(url)
elif mode==1000:
        BING2(url)




xbmcplugin.endOfDirectory(int(sys.argv[1]))
