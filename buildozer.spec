[app]

# (str) Title of your application
title = AI Prompt Gallery

# (str) Package name
package.name = aipromptgallery

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mdarman

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf,otf

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, .buildozer, .github, .git

# (str) Application versioning
version = 0.1

# (str) Author name
author = Md Arman

# (list) Application requirements
# openssl/certifi/urllib3/chardet/idna added: 'requests' HTTPS calls
# fail on Android at runtime without these bundled explicitly.
# pyjnius added: needed for the native Android Intent used to open
# links (webbrowser.open() doesn't work on Android by itself).
requirements = python3,kivy,kivymd,pillow,requests,openssl,certifi,chardet,idna,urllib3,pyjnius

# (str) Supported orientation (portrait/landscape/all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/splash.png

# (str) Presplash background color (for new android toolchain)
android.presplash_color = #0D0D14

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK / AAB will support
android.minapi = 24

# (str) Android NDK version to use - pinned so it never conflicts
# with whatever other NDK versions happen to already be on the runner
android.ndk = 25b

# (bool) If True, then automatically accept SDK license agreements.
# Intended for automation (CI) only.
android.accept_sdk_license = True

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Whether the app allows automatic backup of its data (Android default)
android.allow_backup = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
