[app]
title = StockCtrl Scanner
package.name = stockctrlscanner
package.domain = org.stockctrl

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0.0
requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app]
android.permissions = INTERNET
android.api = 31
android.minapi = 21

# Windows specific (optional)
windows.package_name = stockctrlscanner