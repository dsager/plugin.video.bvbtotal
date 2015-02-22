import sys, os
import urllib
import urlparse
import xbmcgui
import xbmcplugin

sys.path.append(os.path.join('resources', 'lib'))

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
    foldernames = ['Bundesliga', 'Champions League']
    for foldername in foldernames:
        url = build_url({'mode': 'folder', 'foldername': foldername})
        li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
    foldername = args['foldername'][0]
    url = 'https://www.bvbtotal.de/static/flash/portal/player.swf?1420728388'
    li = xbmcgui.ListItem(foldername + ' Video', iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)
