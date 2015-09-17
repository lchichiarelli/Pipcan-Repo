import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
addon_id='plugin.video.guiadvanced'

############################################-----V READING THE SETTINGS V-----##########################################################

#V------- Give Your Setting A Name               V----------- The Name Of The ID In The /resources/settings.xml
myname=xbmcplugin.getSetting(int(sys.argv[1]), 'myname')

###########################################################################################################################################


def CATEGORIES():
        addDir2('[COLOR yellow]-------------------- ADVANCED -----------------[/COLOR]','2',3,'2')
        addDir2('SHOW MY USERNAME IN OK DIALOG %s'%myname,'2',4,'2')
        addDir2('PERCENTAGE','2',5,'2')
        addDir2('SELECT','2',6,'2')
        addDir2('DATE ENTER','2',7,'2')
        addDir2('NOTIFICATION INFO','2',8,'2')
        addDir2('NOTIFICATION WARNING','2',9,'2')
        addDir2('NOTIFICATION ERROR','2',10	,'2')
        addDir2('SLIDE OUT FROM SIDE','2',11,'2')
        addDir2('INPUT PASSWORD','2',12,'2')
        addDir2('INPUT TIME','2',13,'2')
        addDir2('INPUT IP ADDRESS','2',14,'2')
        addDir2('INPUT DATE','2',15,'2')
        addDir2('INPUT NUMERIC ','2',16,'2')
        addDir2('INPUT ALPHANUM ','2',17,'2')
        addDir2('[COLOR yellow]-------------------- MORE EXAMPLES SOON -----------------[/COLOR]','2',3,'2')

#    V----- Name Of Your Function It Can Be Anything		
def OK():
    showText("HEADER(%d),%(myname)","Ok we named or settings at the top myname so myname is equal to xbmcplugin.getSetting(int(sys.argv[1]), 'name') so what ever txt that is in the settings see resources/settings.xml  so by default its No Name now were we put the words myname some were it will display the txt now we want to have txt either side of users name so you need to put %s anywhere were you want the txt to be displayed so if we put the txt Your Name Is %s it will read Your Name Is No Name now we also need to define what %s equals to do the after the end 'you want to put % (myname) this means % is equal to myname so now it should read 'Your Name Is %s'% (myname)")
#    V----- Name Of Your Function		
#                  V----- This Is Your Header For Your Ok Dialog Box	
#    Ok we named or settings at the top myname so myname is equal to xbmcplugin.getSetting(int(sys.argv[1]), 'name') so what ever txt that
#    is in the settings see resources/settings.xml  so by default its No Name now were we put the words myname some were it will display
#    the txt now we want to have txt either side of users name so you need to put %s anywhere were you want the txt to be displayed so if
#    we put the txt Your Name Is %s it will read Your Name Is No Name now we also need to define what %s equals to do the after the end '
#    you want to put % (myname) this means % is equal to myname so now it should read 'Your Name Is %s'% (myname))

###########################################################################################################################################
def SIDEWINDOW():
    showText('HEADER','YOUR MESSAGE HERE')
###########################################################################################################################################
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
###########################################################################################################################################
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
###########################################################################################################################################
def YESNO():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Ok Or Close','', "",'Close','Ok'):
        dialog.ok("You Pressed ok", " You Pressed ok")
    else:
        dialog.ok("You Pressed Close", " You Pressed Close	")	

###########################################################################################################################################
def SELECT():
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Choose a playlist', ['%s'%(myname), 'Playlist #2', 'Playlist #3'])
###########################################################################################################################################
def DATE():
    dialog = xbmcgui.Dialog()
    d = dialog.numeric(1, 'Enter date of birth')
###########################################################################################################################################
def TIME():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter Time', type=xbmcgui.INPUT_TIME)
###########################################################################################################################################
def PASSWORD():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
###########################################################################################################################################
def DATE():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_DATE)
###########################################################################################################################################
def IPADDRESS():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_IPADDRESS)
###########################################################################################################################################
def NUMERIC():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_NUMERIC)
###########################################################################################################################################
def ALPHANUM():
    dialog = xbmcgui.Dialog()
    d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM)
###########################################################################################################################################
def NOTE():
    dialog = xbmcgui.Dialog()
    dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_INFO, 5000)
###########################################################################################################################################
def NOTEw():
    dialog = xbmcgui.Dialog()
    dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_WARNING, 5000)
###########################################################################################################################################
def NOTEe():
    dialog = xbmcgui.Dialog()
    dialog.notification('Movie Trailers', 'Finding Nemo download finished.', xbmcgui.NOTIFICATION_ERROR, 5000)
###########################################################################################################################################
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

###########################################################################################################################################
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
###########################################################################################################################################
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
###########################################################################################################################################
        
              
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
    YESNO()
elif mode==4:
    OK()
elif mode==5:
    PERCENT()
elif mode==6:
    SELECT()
elif mode==7:
    DATE()
elif mode==8:
    NOTE()
elif mode==9:
    NOTEw()
elif mode==10:
    NOTEe()
elif mode==11:
    SIDEWINDOW()
elif mode==12:
    PASSWORD()
elif mode==13:
    TIME()
elif mode==14:
    IPADDRESS()
elif mode==15:
    DATE()
elif mode==16:
    NUMERIC()
elif mode==17:
    ALPHANUM()
elif mode==18:
    PLAY()


xbmcplugin.endOfDirectory(int(sys.argv[1]))
