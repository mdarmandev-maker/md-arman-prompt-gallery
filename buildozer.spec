[app]
# (str) Title of your application
title = AI Prompt Gallery

# (str) Package name
package.name = aipromptgallery

# (str) Package domain
package.domain = org.mdarman

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 0.1

# (str) Author name
author = Md Arman

# (list) Application requirements
requirements = python3,kivy,kivymd,pillow,requests

# (str) Supported orientation (portrait/landscape)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/splash.png

# (list) Permissions
android.permissions = INTERNET

# (int) Android API level
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
