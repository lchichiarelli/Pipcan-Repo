import xbmcgui,xbmcplugin
# CREATED BY C0mmand 
# GitWeb: https://github.com/C0mmand

# BT Sports UK
name1='  stream1  '
# STREAM 1 URL
link1='http://maxiptv.dyndns.org:8000/live/7Kbk8XRf61/JSYw2Hu8Rf/32.ts'

# BT Sports 2 UK
name2='  stream2  '
# STREAM 2 URL
link2='http://maxiptv.dyndns.org:8000/live/7Kbk8XRf61/JSYw2Hu8Rf/33.ts'

# TSN 1 USA
name3='  stream3  '
# STREAM 3 URL
link3='http://iptvspeedy4you.ddns.net:8000/live/volkii24@outlook.de/wZu5jOzfNo/556.ts'

# One By 4K
name4='  stream4  '
# STREAM 4 URL
link4='http://rtmp.one.by:1400/'

# NTV+ Futbol HD
name5='  stream5  '
# STREAM 5 URL
link5='http://78.30.254.27:8989/udp/239.0.0.169:4000'

# NBC Sports Network 1080P
name6='  stream6  '
# STREAM 6 URL
link6='http://tvenbcsn-i.Akamaihd.net/hls/live/218235/nbcsnx/4296k/prog.m3u8|X-Forwarded-For=209.239.112.104'

# Sky Sports Plus  IT
name7='  stream7  '
# STREAM 7 URL
link7='http://visionhd.dyndns.tv:8000/live/cam2oS6h7n/G8AH9N9wcP/24.ts'





plugin_handle = int(sys.argv[1])
# ADDON NAME
_id = 'plugin.video.easychannels'
# ICONS DIR
_icondir = "special://home/addons/" + _id + "/icons/"

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

# TO  ADD STREAM UNCOMMENT LINE                              V----ICONS
add_video_item('%s'% (link1),{ 'title': '%s'% (name1)}, '%s/1.jpg'% _icondir)
add_video_item('%s'% (link2),{ 'title': '%s'% (name2)}, '%s/2.jpg'% _icondir)
add_video_item('%s'% (link3),{ 'title': '%s'% (name3)}, '%s/3.jpg'% _icondir)
#add_video_item('%s'% (link4),{ 'title': '%s'% (name4)}, '%s/4.jpg'% _icondir)
#add_video_item('%s'% (link5),{ 'title': '%s'% (name5)}, '%s/5.jpg'% _icondir)
#add_video_item('%s'% (link6),{ 'title': '%s'% (name6)}, '%s/6.jpg'% _icondir)
#add_video_item('%s'% (link7),{ 'title': '%s'% (name7)}, '%s/7.jpg'% _icondir)
#add_video_item('%s'% (link8),{ 'title': '%s'% (name8)}, '%s/8.jpg'% _icondir)


xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")

