import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
ADDON = xbmcaddon.Addon(id='plugin.video.firstaddon')
AddonID = 'plugin.video.firstaddon'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")


# SHOWING A VALUE THAT IS IN THE SETTINGS

def SHOWNAME(url):
#   Get The Settings V -------     V--------- With The ID myname So What Ever Is Entered In That Is Stored In The settings
#   To Have The Below Value Available To All Defined Values just copy the code line bellow and put it to line 6 and remove the blank spaces 
    myname = ADDON.getSetting(id='myname')
#    ^---- name Of Action It Can Be Anything
# Now The Below Code Can Be Written In Two Ways Like 
# 1) showText(myname,'YOUR MESSAGE HERE') OR This is if you want to display the value of username in header and nothing else
# 2) showText('%s'%(myname),'YOUR MESSAGE HERE') This is so you can enter a value ether side of %s the value %s Will Be Replaced With
# The Value myname By Default Its No Name  
    showText('%s'%(myname),'YOUR MESSAGE HERE')
# Same Can Be Applied Below If You Want To Add WELCOME The The Users Name Were You See The Text 'NAME' change it to 'WELCOME %s'%(myname)
def CATEGORIES():
       myname = ADDON.getSetting(id='myname')
       addDir2('NAME','url',4,'icon')
       addDir2('CHANGE NAME','url',5,'icon')
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################	

	
def CHANGENAME():
    dialog = xbmcgui.Dialog()
#   Shoe Dialog        V-- The Header                         V--- The Type Of Input
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM)
#   V -- If The Value Of d is Equal To '' So Empty 
    if d == '':
# The Return 
        return True
# But If d Has Anything But Empty Set The Settings myname To Entered value
    else:
         ADDON.setSetting(id='myname', value=d)
#        Set Settings myname --^           ^------- To The Value Entered In d 
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
            xbmcplugin.getSetting(int(sys.argv[1]), 'myname')
            return
        except:
            pass







def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
		
		
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
#################################################################################################################################
##############################                                ###################################################################
##############################      Read The Page             ###################################################################



def REGEX(url):
#                        V----- This Meens It Will Read The Url In The Link Item That Was Pressed
        link = OPEN_URL(url)
#                          V---- REGEX  CODE GOES HERE
        match=re.compile('  ').findall(link)
#              V---- For Every (.+?) In You REGEX You Must Give It A Name so if you have 2 and its  name and url put name,url
        for channelid in match:
#                   V -- if you want the name to appper here you could remove to ' ' and just put name or you could put %s in the middle
#                        then after the ' put %(name) so sould look like '%s'%(name)
#                           V ----- this is the mode set it to the def() you wana run see bottom 
            addDir(' ',' ',1,'','')

			
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

















                
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

















#################################################################################################################################
##############################                                ###################################################################
############################## DEFINING YOUR DEF () FUNCTIONS ###################################################################

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
#          V ----- GIVE YOU MODE A NUMBER
elif mode==1:
#        V ---- Then The Name Of A def name() you have made
        INDEX(url)
#             ^------- and witch bit you want to keep so you want it to remember the name in addDir so put name    
elif mode==4:
#        V ---- Then The Name Of A def name() you have made
        SHOWNAME(url)
#             ^------- and witch bit you want to keep so you want it to remember the name in addDir so put name    
elif mode==5:
#        V ---- Then The Name Of A def name() you have made
        CHANGENAME()
#             ^------- and witch bit you want to keep so you want it to remember the name in addDir so put name    



xbmcplugin.endOfDirectory(int(sys.argv[1]))


#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
