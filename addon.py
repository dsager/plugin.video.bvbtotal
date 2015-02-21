import xbmcaddon
import xbmcgui

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')

line1 = "Test..."
line2 = "Nur der BVB!"

xbmcgui.Dialog().ok(__addonname__, line1, line2)
