#Created By Pipcan
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
#                             V----- Name Of Folder Your Addon Is In 
ADDON = xbmcaddon.Addon(id='plugin.video.projectdroidupdate')
#             V----- Name Of Folder Your Addon Is In 
username=xbmcplugin.getSetting(int(sys.argv[1]), 'username')
password=xbmcplugin.getSetting(int(sys.argv[1]), 'password')
AddonID = 'plugin.video.projectdroidupdate'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
#                                     V------ Addons Directory
HOME       =  xbmc.translatePath('special://home/')
HOME3       =  xbmc.translatePath('special://home/userdata/')
#                                                     V---- Userdata Directory
userdata       =  xbmc.translatePath('special://home/userdata/addon_data/')
# Below Is Were You Default.py Should Be So If You Make Changes Just Upload To That Location And It Will Download When Update List Is Hit
BASE=("http://projectdroid.esy.es/kodi")
firstrun=xbmcplugin.getSetting(int(sys.argv[1]), 'firstrun')
login=xbmcplugin.getSetting(int(sys.argv[1]), 'login')
addon_name="Project Android Updater"

def CATEGORIES():#V--start bold   V ---- Name        V-- End Bold                      Location Of Zip ----V                 V---Image
        if login == "false":
            addDir2('[B]Login[/B] - [I]Click To Login[/I]','login',8,'')
        else:
            addDir('[B]Enter[/B] - [I]Enter Installer[/I]','terms',7,'')
#                          V----- Color Of Text
def SIGNIN():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("%s"%(addon_name), 'Do you Wish To Sign In','', "",'Dont Have An Account','Sign In'):
        email=Search('username')
        ADDON.setSetting('username',email)
        password=Search('Password')
        ADDON.setSetting('password',password)
        logincheck=urllib.urlopen('%s/check.php?username=%s&password=%s'%(BASE,email,password)).read()
        if logincheck == "wrong":
            dialog.ok("Error", "Wrong Username And Password")
            return
        if logincheck == "correct":
            dialog.ok("Login Successful !", " Thank You")
            ADDON.setSetting('login','true')
            xbmc.executebuiltin('Container.Refresh')
    else:
        dialog.ok("Get An Account", "Head Over To http://mykodi.co.uk And Sign Up ")
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
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
def UpdateMe(url):
    dialog = xbmcgui.Dialog()
#      Yes No Dialog Exit If No
    if dialog.yesno("Update", 'Do you Wish To Install Addon','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('Grab A Tea Could Be A whiles')
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
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Magic Browser")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
def DOWNLOADS():
        url = '%s/files.php?username=%s&password=%s'%(BASE,username,password)
        link = OPEN_URL(url)
        match=re.compile('File:(.+?)"').findall(link)
        for url in match:
                addDir2('[COLOR white]Update Now [/COLOR]','%s'%(url),3,'')		
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
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
def TERMS():
    termscon=urllib.urlopen('http://localhost/amember/terms.php').read()
    xbmc.sleep(1000)
    showText('Terms And Conditions','%s'%(termscon))
    xbmc.sleep(5000)
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Do You accept", 'Do You Accept The Terms','', "",'Close','Yes'):
        ADDON.setSetting('firstrun','true')
        xbmc.sleep(1000)
        xbmc.executebuiltin('Container.refresh')
    else:
        return
def YESNO():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Do You accept", 'Do You Accept The Terms','', "",'Close','Logout'):
        ADDON.setSetting('firstrun','True')
        xbmc.executebuiltin('Container.Refresh')
    else:
        return
def UpdateMeaddon(url):
    dialog = xbmcgui.Dialog()
    if dialo.yesno("Update", 'Do you Wish To Install Addon','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        print "DOWNLOAD CANCELLED" # need to get this part working
        url = "%s/guisettings.xml"%(BASE)
        localfile = os.path.join(HOME3,"addon.xml")
        urllib.urlretrieve(url,localfile)
        url = "%s/profiles.xml"%(BASE)
        localfile = os.path.join(HOME3,"addon.xml")
        urllib.urlretrieve(url,localfile)
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
        zin.extractall(HOME)
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
        termscon=urllib.urlopen('http://localhost/amember/terms.php').read()
        if firstrun == "false":
				TERMS()
        else:
            CATEGORIES()

elif mode==2:
    UpdateMeuserdata(url)
elif mode==3:
    UpdateMe(url)
elif mode==4:
    Refresh()
elif mode==5:
    UpdateMeaddon(url)
elif mode==6:
    TERMS()
elif mode==7:
    DOWNLOADS()
elif mode==8:
    SIGNIN()


xbmcplugin.endOfDirectory(int(sys.argv[1]))
