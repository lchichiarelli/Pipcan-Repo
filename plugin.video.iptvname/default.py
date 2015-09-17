import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os
password=xbmcplugin.getSetting(int(sys.argv[1]), 'password')
username=xbmcplugin.getSetting(int(sys.argv[1]), 'username')
site=xbmcplugin.getSetting(int(sys.argv[1]), 'site')
firstrun=xbmcplugin.getSetting(int(sys.argv[1]), 'firstrun')
login=xbmcplugin.getSetting(int(sys.argv[1]), 'login')
record_time=xbmcplugin.getSetting(int(sys.argv[1]), 'record_time')
# Edit line below
BASE = "http://mykodi.co.uk/xstream"		
ADDON = xbmcaddon.Addon(id='plugin.video.iptvname')
AddonID = 'plugin.video.iptvname'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
event=urllib.urlopen('%s/ppvname.php'% (BASE)).read()
answers=urllib.urlopen('%s/answers.php'% (BASE)).read()
eventdescription=urllib.urlopen('%s/ppvdescription.php'% (BASE)).read()
eventon=urllib.urlopen('%s/ppvon.php'% (BASE)).read()
eventurl=urllib.urlopen('%s/ppvurl.php'% (BASE)).read()
eventtime=urllib.urlopen('%s/ppvtime.php'% (BASE)).read()
date= datetime.datetime.today().strftime('%Y-%m-%d')
dateshort= datetime.datetime.today().strftime('%d/%m')
time= datetime.datetime.today().strftime('%H:%M:%S')
version = Addon.getAddonInfo('version')
updates=urllib.urlopen('%s/version.php'%(BASE)).read()
addon_name="IPTV Manager"
ban=urllib.urlopen('%s/ip.php'% (BASE)).read()
if ban == "YES":
    dialog = xbmcgui.Dialog()
    dialog.ok("BANNED", "Sorry Seems Your IP Has Been Banned")
    xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
    xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
def CATEGORIES():
        addDir2('[B]Answers To Contact Questions[/B] - [I]Click Here[/I]','/answers.php',33,'')
        addDir('%s - [I]%s[/I]'%(event,eventdescription),'PPV',5,'%s/HD1.png'%(addonDir))
        addDir('Premier League','/channelshow.php',35,'%s/HD1.png'%(addonDir))
        addDir('Channels','/channelshow.php',34,'%s/resources/icons/10.png'%(addonDir))
        addDir('On-Demand','/catshow.php',31,'%s/resources/icons/9.png'%(addonDir))
        addDir2('Settings','settings',3,'%s/resources/icons/8.png'%(addonDir))
        addDir('Tools','Tools',23,'%s/resources/icons/8.png'%(addonDir))
        if updates <> "%s"%(version):
            addDir('Addon Infomation - [I]Update Avalible[/I]','dd',15,'%s/resources/icons/report.png'%(addonDir))
        else:
            addDir('Addon Infomation','about',15,'%s/resources/icons/report.png'%(addonDir))
        addDir2('Contact Us','about',12,'%s/resources/icons/3.png'%(addonDir))
        if login == "true":
           addDir('[COLOR gold]VIP Area[/COLOR]','/channelshowvip.php?username=%s&password=%s' % (username,password),20,'%s/resources/icons/11.png'%(addonDir))
           addDir2('[B][COLOR red]Logout[/COLOR][/B]','login',9,'%s/resources/icons/logout.png'%(addonDir))
        else:
           addDir2('[COLOR green]Login[/COLOR]','login',4,'%s/resources/icons/login.png'%(addonDir))		   
def FOOTBALL():
        addDir('[B]View Current League Table[/B]','settings',36,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 1[/B]','1',37,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 2[/B]','2',37,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 3[/B]','3',37,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 4[/B]','4',37,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 5[/B]','5',37,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 6[/B]','6',37,'%s/CTH_1.png'%(addonDir))
        addDir2('Settings','settings',3,'%s/CTH_2.png'%(addonDir))
        addDir2('Settings','settings',3,'%s/CTH_3.png'%(addonDir))
        addDir2('Settings','settings',3,'%s/CTH_4.png'%(addonDir))
        addDir2('Settings','settings',3,'%s/CTH_5.png'%(addonDir))
def TABLE():
        url = 'http://m.premierleague.com/en-gb/league-table.html'
        link = OPEN_URL(url)
        match=re.compile('/en-gb/clubs/club-profile.html/(.+?)"').findall(link)
        for name in match:
                addDir('[COLOR white]%s [/COLOR]'%(name),'','','')
def FIXTURES(url):
        num = url
        url = 'http://m.premierleague.com/pa-services/api/football/mobile/competition/fandr/api/gameweek/%s.json'%(num)
        link = OPEN_URL(url)
        match=re.compile('"awayTeamScore":(.+?),"homeTeamScore":(.+?),"liveMatch":(.+?),".+?status":"(.+?)".+?"koTime":"(.+?)",".+?displayShortDate":"(.+?)","awayTeamClubURL":"(.+?)","homeTeamClubURL":"(.+?)"').findall(link)
        for s1,s2,live,name,l1,l2,l3,l4 in match:
            if name == "fulltime":
                if s1 > s2:
                    addDir('[COLOR red]%s [/COLOR][COLOR gold]%s [B]%s[/B][/COLOR][COLOR red]   Vs      [B]%s[/B] %s   %s[/COLOR]'%(name.replace('fulltime','FT: '),l3,s1,s2,l4,live.replace('false',' ')),'%s %s'%(l1,l2),'','')
                if s1 < s2:
                    addDir('[COLOR red]%s %s [B]%s[/B]   Vs      [B]%s[/B] [/COLOR][COLOR gold]%s[/COLOR]  [COLOR red]%s[/COLOR]'%(name.replace('fulltime','FT: '),l3,s1,s2,l4,live.replace('false',' ')),'%s %s'%(l1,l2),'','')
                if s1 == s2:
                    addDir('[COLOR blue]%s %s [B]%s[/B]   Vs      [B]%s[/B] %s  %s[/COLOR]'%(name.replace('fulltime','FT: '),l3,s1,s2,l4,live.replace('false',' ')),'%s %s'%(l1,l2),'','')
            else:
                if s1 == "null":
                    addDir('[COLOR red]%s[/COLOR] %s %s %s %s VS %s %s  '%(name.replace('FIXTURE',' '),l1,l2,l3,s1.replace('null',' '),s2.replace('null',' '),l4),'%s'%(live),'','')
                else:
                    if l2 == dateshort:
                        addDir('[COLOR red]%s[/COLOR] %s %s %s %s VS %s %s    %s'%(name.replace('FIXTURE',' '),l1,l2.replace('%s'%(dateshort),''),l3,s1,s2,l4,live.replace('false',' ').replace('true','[COLOR green]LIVE![/COLOR]')),'','','')
                    else:
                        addDir('[COLOR red]%s[/COLOR] %s %s %s %s VS %s %s    %s'%(l2,name.replace('FIXTURE',' '),l1,l3,s1,s2,l4,live.replace('false',' ').replace('true','[COLOR green]LIVE![/COLOR]')),'','','')
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Magic Browser")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def addon_info():
        if version == updates:
           addDir2('                                   [COLOR gold][B]IPTV MANAGER [I]%s[/I][/B][/COLOR][CR]'%(updates),'/',6,'')
           addDir2('[COLOR green]Is Up To Date[/COLOR] [%s]'%(updates),'/vodshow.php',16,'')
        else:
           addDir2('[COLOR red]Is Out Of Date[/COLOR] [%s] - [I]Click To Update[/I]'%(updates),'/vodshow.php',16,'')
        addDir('[COLOR yellow]Your Version[/COLOR] [%s]'%(version),'/vodshow.php',11,'')
        addDir2('The Developer','/vodshow.php',6,'')
def beta():
    addLink('247 ','http://mykodi.co.uk/xstream/m3u/24.m3u','http://www.flags.net/images/largeflags/ARLE0001.GIF','')
    addLink('1080p & 4K','http://mykodi.co.uk/xstream/m3u/1080p.m3u','http://www.flags.net/images/largeflags/ARLE0001.GIF','')
    addLink('Africa ','http://mykodi.co.uk/xstream/m3u/africa.m3u','http://www.flags.net/images/largeflags/ARLE0001.GIF','')
    addLink('Arabic ','http://mykodi.co.uk/xstream/m3u/Arabic.m3u','http://www.flags.net/images/largeflags/ARLE0001.GIF','')
    addLink('Adult','http://mykodi.co.uk/xstream/m3u/Adult.m3u','','')
    addLink('Albanien','http://mykodi.co.uk/xstream/m3u/Albanian.m3u','http://www.flags.net/images/largeflags/ALBA0001.GIF','')
    addLink('Argentina','http://mykodi.co.uk/xstream/m3u/arg.m3u','http://www.flags.net/images/largeflags/ARGE0001.GIF','')
    addLink('Bosnian ','http://mykodi.co.uk/xstream/m3u/Bosnian.m3u','http://www.flags.net/images/largeflags/BOHE0001.GIF','')
    addLink('BeinSports ','http://mykodi.co.uk/xstream/m3u/Beinsports.m3u','http://www.rgenerator.com/files/2014/03/workpage_tiles_0008_bein.jpg','')
    addLink('China','http://mykodi.co.uk/xstream/m3u/china.m3u','http://www.flags.net/images/largeflags/CHIN0001.GIF','')
    addLink('Canada','http://mykodi.co.uk/xstream/m3u/can.m3u','http://www.flags.net/images/largeflags/CANA0001.GIF','')
    addLink('Croatian','http://mykodi.co.uk/xstream/m3u/Croatian.m3u','http://www.flags.net/images/largeflags/CROA0001.GIF','')
    addLink('French ','http://mykodi.co.uk/xstream/m3u/French.m3u','http://www.flags.net/images/largeflags/FRAN0001.GIF','')
    addLink('Filmon','http://mykodi.co.uk/xstream/m3u/filmon.m3u','http://i1.wp.com/pmcvariety.files.wordpress.com/2014/01/filmon-x-logo.jpg?crop=163px%2C95px%2C690px%2C384px&resize=670%2C377','')
    addLink('German ','http://mykodi.co.uk/xstream/m3u/German.m3u','http://www.flags.net/images/largeflags/GERM0001.GIF','')
    addLink('Greek','http://mykodi.co.uk/xstream/m3u/Greek.m3u','','')
    addLink('Italian ','http://mykodi.co.uk/xstream/m3u/Italian.m3u','http://www.flags.net/images/largeflags/ITAL0001.GIF','')
    addLink('Indian','http://mykodi.co.uk/xstream/m3u/in.m3u','http://www.flags.net/images/largeflags/INDA0001.GIF','')
    addLink('Indonesia','http://mykodi.co.uk/xstream/m3u/Indonesia.m3u','http://www.flags.net/images/largeflags/INDA0001.GIF','')
    addLink('Iran','http://mykodi.co.uk/xstream/m3u/iran.m3u','http://www.flags.net/images/largeflags/IRAN0001.GIF','')
    addLink('Japan','http://mykodi.co.uk/xstream/m3u/Japan.m3u','http://www.flags.net/images/largeflags/IRAN0001.GIF','')
    addLink('Jamaica','http://mykodi.co.uk/xstream/m3u/jamaica.m3u','http://www.flags.net/images/largeflags/IRAN0001.GIF','')
    addLink('Korea','http://mykodi.co.uk/xstream/m3u/Korea.m3u','http://www.flags.net/images/largeflags/NETH0001.GIF','')
    addLink('Netherlands','http://mykodi.co.uk/xstream/m3u/Neatherlands.m3u','http://www.flags.net/images/largeflags/NETH0001.GIF','')
    addLink('Mexico','http://mykodi.co.uk/xstream/m3u/mexico.m3u','http://www.flags.net/images/largeflags/POLA0001.GIF','')
    addLink('Poland','http://mykodi.co.uk/xstream/m3u/poland.m3u','http://www.flags.net/images/largeflags/POLA0001.GIF','')
    addLink('Portagal','http://mykodi.co.uk/xstream/m3u/Portagal.m3u','http://www.flags.net/images/largeflags/PORT0001.GIF','')
    addLink('Radio','http://mykodi.co.uk/xstream/m3u/radio.m3u','http://www.flags.net/images/largeflags/RUSS0001.GIF','')
    addLink('Russia','http://mykodi.co.uk/xstream/m3u/Russia.m3u','http://www.flags.net/images/largeflags/RUSS0001.GIF','')
    addLink('Serbian','http://mykodi.co.uk/xstream/m3u/Serbian.m3u','http://www.flags.net/images/largeflags/SERB0001.GIF','')
    addLink('Scandinavia','http://mykodi.co.uk/xstream/m3u/Scandinaviana.m3u','','')
    addLink('Spanish ','http://mykodi.co.uk/xstream/m3u/Spanish.m3u','http://www.flags.net/images/largeflags/SPAN0001.GIF','')
    addLink('Swedish ','http://mykodi.co.uk/xstream/m3u/Swidish.m3u','http://www.flags.net/images/largeflags/SWDN0001.GIF','')
    addLink('Turkey','http://mykodi.co.uk/xstream/m3u/Turkey.m3u','http://www.flags.net/images/largeflags/RMNA0001.GIF','')
    addLink('Thailand','http://mykodi.co.uk/xstream/m3u/Thailand.m3u','http://www.flags.net/images/largeflags/RMNA0001.GIF','')
    addLink('USA','http://mykodi.co.uk/xstream/m3u/USA.m3u','http://www.flags.net/images/largeflags/UNST0001.GIF','')
    addLink('Yugoslavian','http://mykodi.co.uk/xstream/m3u/Yugoslavian.m3u','http://www.flags.net/images/largeflags/SERB0001.GIF','')
    addLink('UK ','http://mykodi.co.uk/xstream/m3u/UK.m3u','http://www.flags.net/images/largeflags/UNKG0001.GIF','')
    addLink('Sports','http://mykodi.co.uk/xstream/m3u/sports.m3u','http://www.thecurlew.co.uk/wp-content/uploads/2009/10/sky-sports-logo.jpg','')
    addLink('Unsorted','http://mykodi.co.uk/xstream/m3u/unsorted.m3u','http://www.userlogos.org/files/logos/sjdvda/UNSORTED.png','')
    addLink('Unsorted 2','http://mykodi.co.uk/xstream/m3u/random.m3u','http://www.userlogos.org/files/logos/sjdvda/UNSORTED.png','')
    addLink('VOD','http://mykodi.co.uk/xstream/m3u/VOD.m3u','http://img03.deviantart.net/1fe2/i/2014/178/d/2/vod_logo_site1_1050x500_by_effect_design-d7o8xw4.jpg','')

def channelsort():
    addDir('[B]Search[/B]','/browse.php?q=',1,'%s/resources/icons/search.png'%(addonDir))
    addDir('Show All Channels','/channelshow.php',1,'%s/resources/icons/10.png'%(addonDir))
    addDir('Show categories','/channelshow.php',18,'%s/resources/icons/10.png'%(addonDir))
    addDir('[COLOR gold][B]Channels BETA[/B][/COLOR]','beta',34,'%s/resources/icons/search.png'%(addonDir))
    addDir('Show Countries','/channelshow.php',19,'%s/resources/icons/10.png'%(addonDir))
def myaccount():
    addDir('[B][COLOR yellow]Your Account %s[/COLOR][/B]'%(username),'/browse.php?q=',1,'%s/resources/icons/search.png'%(addonDir))
    addDir('[B]Channels[/B]','/channelshowvip.php?username=%s&password=%s' % (username,password),1,'%s/resources/icons/11.png'%(addonDir))
    addDir('[B]Chat Room[/B]','/chat.php',99,'%s/resources/icons/11.png'%(addonDir))
    addDir('[B]On Demand[/B]','/vipondemand.php',31,'%s/resources/icons/11.png'%(addonDir))

def cat():
        count=urllib.urlopen('%s/count.php?cat=business'%(BASE)).read()
        count2=urllib.urlopen('%s/count.php?cat=educational'%(BASE)).read()
        addDir('[B]EDUCATIONAL[/B] - [I] %s Streams Avalible [/I]'%(count2),'/channelca.php?cat=educational',1,'%s/resources/icons/educational.png'%(addonDir))
        count11=urllib.urlopen('%s/count.php?cat=entertainment'%(BASE)).read()
        addDir('[B]ENTERTAINMENT[/B] - [I] %s Streams Avalible [/I]'%(count11),'/channelca.php?cat=entertainment',1,'%s/resources/icons/entertainment.png'%(addonDir))
        count3=urllib.urlopen('%s/count.php?cat=kids'%(BASE)).read()
        addDir('[B]KIDS[/B] - [I] %s Streams Avalible [/I]'%(count3),'/channelca.php?cat=kids',1,'%s/resources/icons/kids.png'%(addonDir))
        count4=urllib.urlopen('%s/count.php?cat=lifestyle'%(BASE)).read()
        addDir('[B]LIFESTYLE[/B] - [I] %s Streams Avalible [/I]'%(count4),'/channelca.php?cat=lifestyle',1,'%s/resources/icons/lifestyle.png'%(addonDir))
        count5=urllib.urlopen('%s/count.php?cat=movies'%(BASE)).read()
        addDir('[B]MOVIES[/B] - [I] %s Streams Avalible [/I]'%(count5),'/channelca.php?cat=movies',1,'%s/resources/icons/movies.png'%(addonDir))
        count6=urllib.urlopen('%s/count.php?cat=music'%(BASE)).read()
        addDir('[B]MUSIC[/B] - [I] %s Streams Avalible [/I]'%(count6),'/channelca.php?cat=music',1,'%s/resources/icons/Music.png'%(addonDir))
        count7=urllib.urlopen('%s/count.php?cat=religious'%(BASE)).read()
        addDir('[B]RELIGOUS[/B] - [I] %s Streams Avalible [/I]'%(count7),'/channelca.php?cat=religious',1,'%s/resources/icons/religious.png'%(addonDir))
        count8=urllib.urlopen('%s/count.php?cat=shopping'%(BASE)).read()
        addDir('[B]SHOPPING[/B] - [I] %s Streams Avalible [/I]'%(count8),'/channelca.php?cat=shopping',1,'%s/resources/icons/shopping.png'%(addonDir))
        count9=urllib.urlopen('%s/count.php?cat=sports'%(BASE)).read()
        addDir('[B]SPORTS[/B] - [I] %s Streams Avalible [/I]'%(count9),'/channelca.php?cat=sports',1,'%s/resources/icons/sports.png'%(addonDir))
        count10=urllib.urlopen('%s/count.php?cat=weather'%(BASE)).read()
        addDir('[B]WEATHER[/B] - [I] %s Streams Avalible [/I]'%(count10),'/channelca.php?cat=weather',1,'%s/resources/icons/weather.png'%(addonDir))
def countrys():
        addDir('Argentina','/channelcon.php?flag=ar',1,'%s/resources/icons/flags/Argentina-Flag-256.png'%(addonDir))
        addDir('Arabic','/channelcon.php?flag=ab',1,'%s/resources/icons/flags/aruba.png'%(addonDir))
        addDir('Africa','/channelcon.php?flag=af',1,'%s/resources/icons/flags/south-africa.png'%(addonDir))
        addDir('BELGUIM','/channelcon.php?flag=be',1,'%s/resources/icons/flags/Belgium-Flag-256.png'%(addonDir))
        addDir('BRAZIL','/channelcon.php?flag=br',1,'%s/resources/icons/flags/Brazil-Flag-256.png'%(addonDir))
        addDir('CANADA','/channelcon.php?flag=ca',1,'%s/resources/icons/flags/Canada-Flag-256.png'%(addonDir))
        addDir('CZECH','/channelcon.php?flag=cz',1,'%s/resources/icons/flags/czechia.png'%(addonDir))
        addDir('CHINA','/channelcon.php?flag=cn',1,'%s/resources/icons/flags/China-Flag-256.png'%(addonDir))
        addDir('FRANCE','/channelcon.php?flag=fr',1,'%s/resources/icons/flags/France-Flag-256.png'%(addonDir))
        addDir('ITALY','/channelcon.php?flag=it',1,'%s/resources/icons/flags/Italy-Flag-256.png'%(addonDir))
        addDir('GERMANY','/channelcon.php?flag=de',1,'%s/resources/icons/flags/Italy-Flag-256.png'%(addonDir))
        addDir('INDONISIA','/channelcon.php?flag=id',1,'%s/resources/icons/flags/indonesia.png'%(addonDir))
        addDir('INDIA','/channelcon.php?flag=in',1,'%s/resources/icons/flags/weather.png'%(addonDir))
        addDir('JAPAN','/channelcon.php?flag=jp',1,'%s/resources/icons/flags/japanflag-256.png'%(addonDir))
        addDir('KOREAN','/channelcon.php?flag=ko',1,'%s/resources/icons/flags/Korea-Flag-256.png'%(addonDir))
        addDir('PAKISTAN','/channelcon.php?flag=pk',1,'%s/resources/icons/flags/pakistan.png'%(addonDir))
        addDir('PORTUGAL','/channelcon.php?flag=pg',1,'%s/resources/icons/flags/portugal.png'%(addonDir))
        addDir('RUSSIA','/channelcon.php?flag=rs',1,'%s/resources/icons/flags/russia.png'%(addonDir))
        addDir('SPANISH','/channelcon.php?flag=sp',1,'%s/resources/icons/flags/spainflag-256.png'%(addonDir))
        addDir('THIA','/channelcon.php?flag=th',1,'%s/resources/icons/flags/Thailandflag-256.png'%(addonDir))
        addDir('TURKEY','/channelcon.php?flag=tk',1,'%s/resources/icons/flags/Turkey-Flag-256.png'%(addonDir))
        addDir('UNITED KINGDOM','/channelcon.php?flag=uk',1,'%s/resources/icons/flags/United-Kingdom-flag-256.png'%(addonDir))
        addDir('USA','/channelcon.php?flag=us',1,'%s/resources/icons/flags/United-States-Flag-256.png'%(addonDir))
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
def UpdateMe():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("Update", 'Do you Wish To update','', "",'Close','Yes'):
        dp = xbmcgui.DialogProgress()
        dp.create('UPDATING')
        dp.update(20)
        dialog = xbmcgui.Dialog()
        dp = xbmcgui.DialogProgress()
        dp.create('Downloading Zip')
        dp.update(60)
        import zipfile 
        print "DOWNLOAD CANCELLED"
        url = "%s/addonfiles/plugin.video.iptvname%s.zip"%(BASE,updates)
        localfile = os.path.join(addonDir,"resources/plugin.video.iptvname%s.zip"%(updates))
        urllib.urlretrieve(url,localfile)
        dp.update(70)
        zin = zipfile.ZipFile(localfile, 'r')
        zin.extractall(addonDir)
        url = "%s/changelog.php"%(BASE)
        localfile = os.path.join(addonDir,"changelog.txt")
        urllib.urlretrieve(url,localfile)
        url = "%s/addonxml.php"%(BASE)
        localfile = os.path.join(addonDir,"addon.xml")
        urllib.urlretrieve(url,localfile)
        dp.update(90)
        xbmc.executebuiltin("UpdateLocalAddons")
        xbmc.executebuiltin("UpdateAddonRepos")
        dp.update(100)
        dp.close()
        dialog.ok("All Done", " Update Is Complete")
        xbmc.executebuiltin('Container.Refresh')
    else:
        return
def INDEX4(url):
	if url=="/browse.php?q=":
	  searchString = addSearch()
	  url="/browse.php?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,iconimage,name in match:
	      addDir(name,url,32,iconimage)

def INDEX5(url):
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('Name: "(.+?)", file: "(.+?)", Image: "(.+?)",').findall(link)
	  for name,url,iconimage in match:
	      addDir2(name,url,8,"")
def INDEX2(url):
	addDir2('[I]Refresh[/I]','/channelcon.php?flag=us',22,'%s/resources/icons/flags/United-States-Flag-256.png'%(addonDir))
	addDir2('[B]Click To Post Message[/B]','%s'%(username),21,'%s/resources/icons/flags/United-States-Flag-256.png'%(addonDir))
	if url=="/browse.php?q=":
	  searchString = addSearch()
	  url="/browse.php?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
	        addLink(name,url,thumbnail,"")
          match=re.compile('src="http://www.youtube.com/embed/(.+?)?rel=0').findall(link)
          for url in match:
	    youtubeurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
	    addLink(name,youtubeurl,thumbnail,"")
	  match=re.compile('FILMON: "(.+?)",').findall(link)
	  for url in match:
	        addLink(name,url,thumbnail,"")
	  match=re.compile('FILMON: "(.+?)",').findall(link)
	  for url in match:
	        addLink(name,url,thumbnail,"")
def INDEX(url):
	if url=="/browse.php?q=":
	  searchString = addSearch()
	  url="/browse.php?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,iconimage,name in match:
	      addDir(name,url,30,iconimage)

def INDEX3(name,url):
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Kodi (Kodi; U; kodi; en-GB;) kodi')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
	      addLink(name,url,'',"")
def vod(url):
	if url=="browse?q=":
	  searchString = addSearch()
	  url="browse?q="+searchString
	after = url
	url = BASE + url
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        match=re.compile('<a href="(.+?)"><img class="thumbnail_image" src="(.+?)" alt="(.+?)"').findall(link)
        for url,thumbnail,name in match:
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  match=re.compile('file: "(.+?)",').findall(link)
	  for url in match:
                addDir2(name,url,8,thumbnail)
def SIGNIN():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("%s"%(addon_name), 'Do you Wish To Sign In','', "",'Dont Have An Account','Sign In'):
        email=Search('username')
        ADDON.setSetting('username',email)
        password=Search('Password')
        ADDON.setSetting('password',password)
        logincheck=urllib.urlopen('%s/logincheck.php?username=%s&password=%s'%(BASE,email,password)).read()
        if logincheck == "wrong":
            dialog.ok("Error", "Wrong Username And Password")
            return
        if logincheck == "correct":
            fullname=urllib.urlopen('%s/username.php?username=%s'%(BASE,email)).read()
            dialog.ok("Login Successful !", " Thank You For Login In %s Enjoy The VIP Channels"%(fullname))
            ADDON.setSetting('login','true')
            xbmc.executebuiltin('Container.Refresh')
    else:
        dialog.ok("Get An Account", "Head Over To http://mykodi.co.uk And Sign Up ")
        return
def PPV():
    dialog = xbmcgui.Dialog()
    if eventon=="0":
        dialog.ok("Not Started", "Sorry The Event Has Not Started")
    else:
        if dialog.yesno("%s"%(event), '%s'%(eventdescription),'', "",'Set Reminder','WATCH NOW'):
            addLink('[COLOR yellow][B]Play[/B][/COLOR]','%s'%(eventurl),'',"")
        else:
            ADDON.setSetting('event',event)
            ADDON.setSetting('record_date',date)
            ADDON.setSetting('record_time',eventtime)
def about():
    showText('Sign UP At http://mykodi.co.uk/xstream/board At Join The Group At http://facebook.com/kodicontrol ')
def quest():
    showText('Answers To Your Questions','%s'%(answers))
def help(url):
    showText('Help Infomation','%s'%(url))
def LOGOUT():
    dialog = xbmcgui.Dialog()
    if dialog.yesno("XstreamSports", 'Do you Wish To Logout','', "",'Close','Logout'):
        ADDON.setSetting('username','')
        ADDON.setSetting('password','')
        ADDON.setSetting('firstrun','true')
        dialog.ok("Logged Out", "You Are Now Logged Out")
        ADDON.setSetting('login','false')
        xbmc.executebuiltin('Container.Refresh')
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
def openSettings():
    ADDON.openSettings()	
def contact():
    dialog = xbmcgui.Dialog()	
    ret = dialog.select('Choose a Department', ['Send Us A Message', 'Account Problems', 'Other Help','Request'])
    message=Search('Message')
    if dialog.yesno("[B]Do You Want To Send[/B]", '[B]Message:[/B]%s'%(message).replace('%20',' '),'', "",'Scrap','Send'):
        sendurl=urllib.urlopen('%s/user.php?user=%s&dep=%s&message=%s'.replace(' ','%20')%(BASE,username,ret,message)).read()
        dialog.ok("Message Send", "Your Message Has Been Sent")
    else:
	    return
def chat(url):
    dialog = xbmcgui.Dialog()
    message=Search('Message')
    if dialog.yesno("[B]Do You Want To Send[/B]", '[B]Message:[/B]%s'%(message).replace('%20',' '),'', "",'Scrap','Send'):
        sendurl=urllib.urlopen('%s/chat2.php?user=%s&time=%s&message=%s'.replace(' ','%20')%(BASE,url,time,message)).read()
        dialog.ok("Message Send", "Your Message Has Been Sent")
        xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('Container.Refresh')
        return
    else:
	    return
def refresh():
        xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('Container.Refresh')
def report(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("[B]Do You Want To Send[/B]", '[B]Message:[/B]%s'%(name).replace('%20',' '),'', "",'Scrap','Send'):
        sendurl=urllib.urlopen('%s/user.php?user=%s&dep=4&message=%s[%s]'.replace(' ','%20')%(BASE,username,url,time)).read()
        dialog.ok("Message Send", "Your Message Has Been Sent")
    else:
	    return

def PlayStreamWithResolver(url): 
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

def notify(addonId, message, timeShown=5000):
    addon = xbmcaddon.Addon(addonId)
    xbmc.executebuiltin('Notification(<p class="rbm_timing">(.+?)</p></li>, %s, %d, %s)' % (addon.getAddonInfo('name'), message, timeShown, addon.getAddonInfo('icon')))                
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
        liz=xbmcgui.ListItem(name, url, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        menu=[]
        menu.append(('Refresh', 'Container.Refresh'))        
        menu.append(('[COLOR red]Open With Proxy[/COLOR]','Container.Update(%s?&url=%s&mode=25)'% (sys.argv[0],url)))
        menu.append(('[COLOR red]Report Link[/COLOR]','Container.Update(%s?mode=14&name=%s&url=%s)'% (sys.argv[0],name,url)))
        liz.addContextMenuItems(items=menu, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok
def refresh():
        dialog = xbmcgui.Dialog()
        xbmc.executebuiltin('Container.Refresh')
        xbmc.executebuiltin('UpdateAddonRepos')
        dialog.ok("Refreshing", "You Repos Have Been Updated")
def resolver_settings():
    urlresolver.openSettings()
def MYIP():
    myip=urllib.urlopen('%s/tools.php?tools=ip'% (BASE)).read()
    dialog = xbmcgui.Dialog()
    dialog.ok("Your Ip", "You IP Is [COLOR yellow]%s[/COLOR]"%(myip))
def playF4mLink(url):
    play=xbmc.Player(GetPlayerCore())
    play.play('plugin://plugin.video.f4mTester/?url=%s&mode=play'%(url).replace(".m3u8",".f4m"))
def tools():
    	addDir2('Refresh Repos','/',22,'')	   
    	addDir2('Whats My IP','/',24,'')	   
    	addDir2('URLResolver Settings','/',25,'')
def addSearch():
	searchStr = ''
	keyboard = xbmc.Keyboard(searchStr, 'Search')
	keyboard.doModal()
	if (keyboard.isConfirmed()==False):
	  return
	searchStr=keyboard.getText()
	if (keyboard.isConfirmed()==None):
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
def chooseOne(url):
        possibleChoices = []
        possibleChoices.append((url))        
        dialog = xbmcgui.Dialog()
        ndex = dialog.select("Do you think this will work?", possibleChoices)
        choice = possibleChoices[ndex]
        xbmc.choiceLabel.setLabel("Choice: " + str(choice))
def addLink1(name,url):
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Choose a playlist', ['%s'%(url), '%s'%(url), 'Proxy', 'Cancel'])
    if (ret == 0):
        play=xbmc.Player(GetPlayerCore())
        play.play(url)
    if (ret == 1):
        play=xbmc.Player(GetPlayerCore())
        play.play(url)
    if (ret == 2):
        play=xbmc.Player(GetPlayerCore())
        play.play('plugin://plugin.video.f4mTester/?url=%s&mode=play'%(url).replace(".m3u8",".f4m"))
    if (ret == 3):
        return True      
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
        openSettings()
elif mode==4:
        SIGNIN()
elif mode==5:
        PPV()
elif mode==6:
        about()
elif mode==7:
        help(url)
elif mode==8:
       PlayStreamWithResolver(url)
elif mode==9:
       LOGOUT(	)
elif mode==11:
       vod(url)
elif mode==12:
    contact()
elif mode==13:
    sent()
elif mode==14:
    report(url,name)
elif mode==15:
    addon_info()
elif mode==16:
    UpdateMe()
    sys.exit()
elif mode==17:
    channelsort()
elif mode==18:
    cat()
elif mode==19:
    countrys()
elif mode==20:
    myaccount()
elif mode==21:
    chat(url)
elif mode==22:
    refresh()
elif mode==23:
     tools()
elif mode==24:
     MYIP()
elif mode==25:
     playF4mLink(url)
elif mode==26:
     addLink2(name,url,iconimage)
elif mode==27:
     chooseOne(url)

elif mode==29:
    addLink1(name,url)
elif mode==30:
    INDEX3(name,url)
elif mode==31:
    INDEX4(url)
elif mode==32:
    INDEX5(url)
elif mode==33:
        quest()
elif mode==34:
        beta()
elif mode==35:
        FOOTBALL()
elif mode==36:
        TABLE()
elif mode==37:
        FIXTURES(url)

elif mode==99:
        INDEX2(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))