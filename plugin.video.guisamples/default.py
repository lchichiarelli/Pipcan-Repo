import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
addon_id='plugin.video.guisamples'
###########################################################    STEP 1   ################################################################
def CATEGORIES():
        addDir2('[COLOR yellow]-------------------- BASIC -----------------[/COLOR]','2',3,'2')
        addDir2('YES NO DIALOG','2',3,'2')# <-------- ITEM 1
        addDir2('OK DIALOG','2',4,'2')#     <-------- ITEM 2
        addDir2('PERCENTAGE','2',5,'2')#    <-------- ITEM 3
        addDir2('SELECT','2',6,'2')#        <-------- ITEM 4
        addDir2('DATE ENTER','2',7,'2')#    <-------- ITEM 5
        addDir2('NOTIFICATION INFO','2',8,'2')# <---- ITEM 6
        addDir2('NOTIFICATION WARNING','2',9,'2')#<-- ITEM 7
        addDir2('NOTIFICATION ERROR','2',10	,'2')#<-- ITEM 8
        addDir2('SLIDE OUT FROM SIDE','2',11,'2')#<-- ITEM 9
        addDir2('INPUT PASSWORD','2',12,'2')# <------ ITEM 10
        addDir2('INPUT TIME','2',13,'2')#   <-------- ITEM 11
        addDir2('INPUT IP ADDRESS','2',14,'2')# <---- ITEM 12
        addDir2('INPUT DATE','2',15,'2')#  <--------- ITEM 13
        addDir2('INPUT NUMERIC ','2',16,'2')# <------ ITEM 14
        addDir2('INPUT ALPHANUM ','2',17,'2')# <----- ITEM 15

#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 9 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def SIDEWINDOW():
    showText('HEADER','YOUR MESSAGE HERE')
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
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 1 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def YESNO():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Ok Or Close','', "",'Close','Ok'):
        dialog.ok("You Pressed ok", " You Pressed ok")
    else:
        dialog.ok("You Pressed Close", " You Pressed Close	")	
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 2 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def OK():
    dialog = xbmcgui.Dialog()
    dialog.ok("OK Dialog", "OK Dialog")
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 4 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def SELECT():
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Choose a playlist', ['Playlist #1', 'Playlist #2', 'Playlist #3'])
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 5 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def DATE():
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(1, 'Enter date of birth')
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 11 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def TIME():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter Time', type=xbmcgui.INPUT_TIME)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 10 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def PASSWORD():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
###########################################################################################################################################
def DATE():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_DATE)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 12 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def IPADDRESS():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_IPADDRESS)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 15 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def NUMERIC():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_NUMERIC)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 14 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

def ALPHANUM():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 6 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

def NOTE():
    dialog = xbmcgui.Dialog()
    dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_INFO, 5000)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 7 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

def NOTEw():
    dialog = xbmcgui.Dialog()
    dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_WARNING, 5000)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 8 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def NOTEe():
    dialog = xbmcgui.Dialog()
    dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_ERROR, 5000)
###########################################################################################################################################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV---- ITEM 3 ----VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
def PERCENT():
    dp = xbmcgui.DialogProgress()
    dp.create('Head','Body')
    dp.update(10)
    xbmc.sleep(100)
    dp.update(20)
    xbmc.sleep(100)
    dp.update(30)
    xbmc.sleep(100)
    dp.update(40)
    xbmc.sleep(100)
    dp.update(50)
    xbmc.sleep(100)
    dp.update(60)
    xbmc.sleep(100)
    dp.update(70)
    xbmc.sleep(100)
    dp.update(80)
    xbmc.sleep(100)
    dp.update(90)
    xbmc.sleep(100)
    dp.update(100)
    dp.close()
###########################################################################################################################################
############################################# FOR ITEMS 1 - 15 ##############################################################################

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


################################################# FOR ITEMS 1 - 15  #####################################################################
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
################################################# FOR ITEMS 1 - 15 IS NOT A FOLDER #####################################################################
        
              
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
######################################################FOR ITEMS 1-15 DISPLAYS THE START LIST ########################################################################

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
###################################################### FOR ITEMS 1 ########################################################################
elif mode==3:
    YESNO()
###################################################### FOR ITEMS 2 ########################################################################
elif mode==4:
    OK()
######################################################FOR ITEMS 3 ########################################################################
elif mode==5:
    PERCENT()
######################################################FOR ITEMS 4 ########################################################################
elif mode==6:
    SELECT()
######################################################FOR ITEMS 5 ########################################################################
elif mode==7:
    DATE()
######################################################FOR ITEMS 6 ########################################################################
elif mode==8:
    NOTE()
######################################################FOR ITEMS 7 ########################################################################
elif mode==9:
    NOTEw()
######################################################FOR ITEMS 8 ########################################################################
elif mode==10:
    NOTEe()
######################################################FOR ITEMS 9 ########################################################################
elif mode==11:
    SIDEWINDOW()
######################################################FOR ITEMS 10 ########################################################################
elif mode==12:
    PASSWORD()
######################################################FOR ITEMS 11 ########################################################################
elif mode==13:
    TIME()
######################################################FOR ITEMS 12 ########################################################################
elif mode==14:
    IPADDRESS()
######################################################FOR ITEMS 13 ########################################################################
elif mode==15:
    DATE()
######################################################FOR ITEMS 14 ########################################################################
elif mode==16:
    NUMERIC()
######################################################FOR ITEMS 15 ########################################################################
elif mode==17:
    ALPHANUM()


######################################################FOR ITEMS 1-15 END ########################################################################

xbmcplugin.endOfDirectory(int(sys.argv[1]))
