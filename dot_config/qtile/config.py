# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile
from qtile_extras import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.backend.wayland import InputConfig

if qtile.core.name == "wayland":
    import os, subprocess
    from libqtile import hook
    os.environ['QT_QPA_PLATFORMTHEME'] = 'gtk2'
    os.environ['GTK_IM_MODULE'] = 'fcitx'
    os.environ['QT_IM_MODULE'] = 'fcitx'
    os.environ['LIBVA_DRIVER_NAME'] = 'nvidia'
    os.environ['VDPAU_DRIVER'] = 'nvidia'
    subprocess.Popen(["/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1"])
    subprocess.Popen(["fcitx5", "-d", "-r", "-s", "4"])
    subprocess.Popen(["swayidle", "-w"])
    subprocess.Popen(["swaddle"])

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch focus between windows in current stack pane
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "j", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    # Resize focused window
    Key([mod], "l", lazy.layout.grow()),
    Key([mod], "h", lazy.layout.shrink()),
    Key([mod, "control"], "m", lazy.layout.maximize()),
    Key([mod, "shift"], "r", lazy.layout.reset()),

    # Switch focus to another screen
    Key([mod], "s", lazy.next_screen()),

    # Switch window focus to other pane(s) of stack
    Key(["mod1"], "Tab", lazy.layout.next(), desc="Switch window focus in old fashion way"),
    Key([mod], "w", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),
    Key([mod], "space", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    #Key([mod, "shift"], "space", lazy.layout.rotate(), desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(["mod1"], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Flip xmonad layout mirrored"),
    Key([mod, "control"], "space", lazy.window.toggle_floating(), desc="toggle between floating and non-floating"),
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen()),
    
    # Launch apps
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(["mod1"], "space", lazy.spawn("rofi -show combi"), desc="Launch rofi"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "c", lazy.spawn("galculator"), desc="Launch GTK calculator"),
    Key([mod], "b", lazy.spawn("brave --tls-version-min=1.3"), desc="Launch Borwser"),
    Key([mod], "e", lazy.spawn("pcmanfm-qt"), desc="Launch file manager"),
    Key([mod], "g", lazy.spawn("chromium"), desc="Launch chromium"),
    Key([mod], "f", lazy.spawn("librewolf"), desc="Launch librewolf"),
    Key([mod], "d", lazy.spawn("librewolf --private-window"), desc="Launch librewolf incognito"),
    Key([mod], "n", lazy.spawn("joplin-desktop"), desc="Launch joplin-desktop, n for note"),
    Key([mod], "a", lazy.spawn("keepassxc"), desc="Launch keepAssxc"),
 
    # Change the volume if your keyboard has special volume keys.
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
   
    # Also allow changing volume the old fashioned way.
    Key([mod], "equal", lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key([mod], "minus", lazy.spawn("amixer -c 0 -q set Master 2dB-")),

    # Control playing media using special keys, require **playerctl** installed.
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Control screen brightness
    # Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

    # Shutdown and reboot.
    Key([mod, "mod1", "control"], "Page_Down", lazy.spawn("shutdown now"), desc="Power off"),
    Key([mod, "mod1", "control"], "Page_Up", lazy.spawn("reboot"), desc="Reboot computer"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


# groups name has to be number, cuz how I define keys to switch group, qtile will crash if group name is not number.
groups = [
    Group('1', position=1, label="壹"),
    Group('2', position=2, label="貳"),
    Group('3', position=3, label="參"),
    Group('4', position=4, label="肆"),
    Group('5', position=5, label="伍"),
    Group('6', position=6, layout="monadwide", label="陸"),
    Group('7', position=7, label="柒"),
    Group('8', position=8, label="捌"),
    Group('9', position=9, label="玖")]

for i in groups:
    keys.extend([
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name)),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to focused window to group {}".format(i.name)),
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to and move focused window to group {}".format(i.name)),
            ])

layouts = [
    layout.MonadTall(new_client_position='before_current'),
    layout.Max(),
    layout.MonadWide(),
    # layout.MonadThreeCol(),
    # layout.Floating(border_focus='#00ff00'),
    # layout.Stack(autosplit=True, num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

prompt = widget.Prompt(ignore_dups_history=True) # qtile/#3379
# NB Systray is incompatible with Wayland, consider using StatusNotifier instead
if qtile.core.name == "wayland":
    systray = widget.StatusNotifier(icon_size=20)
elif qtile.core.name == "x11":
    systray = widget.Systray(icon_size=20)

widget_defaults = dict(
    font='Spline Sans Mono',
    fontsize=14,)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/Pictures/Ina'nis.jpeg",
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(disable_drag=True, highlight_method='line', this_current_screen_border='#0088e3', other_current_screen_border='#4a4a4a', hide_unused=True, inactive='#505050'),
                prompt,
                widget.WindowTabs(foreground='#ffe7d6'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("Don't touch my computer", foreground='#ff0000'),
                widget.Memory(format='Mem {MemUsed: .0f}{mm} / {MemTotal: .0f}{mm}', measure_mem='M', update_interval=2.0),
                widget.CPU(format='CPU {freq_current}GHz {load_percent}%'),
                widget.ThermalSensor(tag_sensor='Package id 0', threshold=75, update_interval=1, desc="CPU package temp"),
                widget.Clock(format='%Y-%m-%d %a %H:%M:%S'),
                systray,
                widget.Volume(), 
                widget.QuickExit(),
            ],
            24, opacity=0.9, background='#1d1f21',
        ),
    ),
    Screen(
        wallpaper="~/Pictures/enna_mugimugigo_ennaday2024.jpg",
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(disable_drag=True, highlight_method='line', this_current_screen_border='#0088e3', other_current_screen_border='#4a4a4a', hide_unused=True, inactive='#505050'),
                prompt,
                widget.WindowTabs(foreground='#ffc9a3'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("I said DON'T touch my computer", name="default"),
                widget.Clock(format='%Y-%m-%d %a %H:%M:%S'),
                widget.Volume(), 
            ],
            24, opacity=0.9, background="#1d1f21",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(wm_class='file_progress'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='galculator'),
        Match(wm_class='Browser'),
        Match(wm_class='mpv'),
        Match(title='KeePassXC - Browser Access Request'),
        Match(title='<no name>'),
    ],
    border_focus='#00ff00')

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
    "type:pointer": InputConfig(accel_profile='flat'),
}

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = "Layan-white-cursors"
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
