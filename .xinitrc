#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

# custom startup
#export XCURSOR_THEME=Breeze
export PULSE_LATENCY_MSEC=30 mscore  #fix musesocre noise with pulseaudio
export QT_STYLE_OVERRIDE=gtk2  #qt5-styleplugins required (aur)
export QT_QPA_PLATFORMTHEME=qt6gtk2  #qt6gtk2 required (aur)
# Hardware acceleration config
export LIBVA_DRIVER_NAME=iHD #for intel-media-driver
export MOZ_X11_EGL=1
export MOZ_WEBRENDER=1
# graphical authentication agent
exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# gcin input
#export GTK_IM_MODULE=gcin
#export QT_IM_MODULE=gcin
#export XMODIFIERS="@im=gcin"
#gcin &

# ibus input
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS="@im=ibus"
ibus-daemon -drxR &

# wallpaper
nitrogen --restore &
DISPLAY=":0" picom -b &
#imwheel -b 45 -g &
exec qtile start
