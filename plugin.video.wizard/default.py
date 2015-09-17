#Created By Pipcan
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
#                             V----- Name Of Folder Your Addon Is In 
ADDON = xbmcaddon.Addon(id='plugin.video.wizard')
#             V----- Name Of Folder Your Addon Is In 
AddonID = 'plugin.video.wizard'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
#                                     V------ Addons Directory
HOME       =  xbmc.translatePath('special://home/addons/')
#                                                     V---- Userdata Directory
userdata       =  xbmc.translatePath('special://home/userdata/addon_data/')
# Below Is Were You Default.py Should Be So If You Make Changes Just Upload To That Location And It Will Download When Update List Is Hit
BASE=("http://mykodi.co.uk/wizard")
                                                                
def CATEGORIES():#V--start bold   V ---- Name        V-- End Bold                      Location Of Zip ----V                 V---Image
        addDir2('[B]Example Install To Addons Folder[/B] - [I]Click To Install[/I]','http://mykodi.co.uk/downloadtest.zip',3,'')
        addDir2('[B]Example Install To User Data[/B] - [I]Click To Install[/I]','http://mykodi.co.uk/downloadtest.zip',2,'')
        addDir2('[B]Example Install To plugin.video.wizard[/B] - [I]Click To Install[/I]','http://mykodi.co.uk/downloadtest.zip',5,'')
#                          V----- Color Of Text
        addDir2('[COLOR green][B]Update List[/B][/COLOR]','Refresh',4,'')

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
def UpdateMe(url):
    dialog = xbmcgui.Dialog()
#      Yes No Dialog Exit If No
    if dialog.yesno("Update", 'Do you Wish To Install Addon','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
#      Change Progress To 20%
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
#                    V------- Show Text In Head Before Percentage
        dp.create('Downloading Zip')
#      Change Progress To 60%
        dp.update(60)
#      Import The Python Program That Is Used For Zips
        import zipfile 
#      Location Of The Zip To Download It Will Be Defined In The adddir2 url
        url = ("%s"%(url))
#               As Defined In Top ---V       V-------  Where To Store The File When Downloaded
        localfile = os.path.join(addonDir,"resources/addons.zip")
#      Fetch File
        urllib.urlretrieve(url,localfile)
        zin = zipfile.ZipFile(localfile, 'r')
#        Unzip File To HOME As Defined At Top
        zin.extractall(HOME)
#      Change Progress To 70%
        dp.update(70)
#           Update Addon
        xbmc.executebuiltin("UpdateLocalAddons")
#           Refresh Addon Repo
        xbmc.executebuiltin("UpdateAddonRepos")
#      Change Progress To 100%
        dp.update(100)
        dp.close()
# Finished Dialog    V----Header   V---Body
        dialog.ok("All Done", " Update Is Complete")
    else:
#  If No Is Pressed
        return                
def UpdateMeuserdata(url):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To Install Addon','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading Zip')
        dp.update(60)
        import zipfile 
        url = ("%s"%(url))
        localfile = os.path.join(addonDir,"resources/addons.zip")
        urllib.urlretrieve(url,localfile)
        zin = zipfile.ZipFile(localfile, 'r')
        zin.extractall(userdata)
        dp.update(70)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
    else:
        return                
def UpdateMeaddon(url):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To Install Addon','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading Zip')
        dp.update(60)
        import zipfile 
        url = ("%s"%(url))
        localfile = os.path.join(addonDir,"resources/addons.zip")
        urllib.urlretrieve(url,localfile)
        zin = zipfile.ZipFile(localfile, 'r')
        zin.extractall(addonDir)
        dp.update(70)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
    else:
        return                

def Refresh():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To update','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Refreshing List')
        dp.update(60)
#                               V----- See Top
        url = "%s/default.py"%(BASE)
#                                           V----- copy New Default To Current
        localfile = os.path.join(addonDir,"default.py")
        urllib.urlretrieve(url,localfile)
        dp.update(90)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
#                               V----- Refesh Page
        xbmc.executebuiltin('Container.Refresh')
    else:
        return
                
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

elif mode==2:
    UpdateMeuserdata(url)
elif mode==3:
    UpdateMe(url)
elif mode==4:
    Refresh()
elif mode==5:
    UpdateMeaddon(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
