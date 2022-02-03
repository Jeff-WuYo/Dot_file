# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:

{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
    ];

  # Use the systemd-boot EFI boot loader.
  boot.loader.systemd-boot.enable = true;
  boot.loader.efi.canTouchEfiVariables = true;

  networking.hostName = "nixosvm2"; # Define your hostname.
  # networking.wireless.iwd.enable = true;  # Enables wireless support via iwd.
  # services.connman.wifi.backend = "iwd";
  # networking.networkmanager.wifi.backend = "iwd";
  # Set your time zone.
  time.timeZone = "Asia/Taipei";

  # The global useDHCP flag is deprecated, therefore explicitly set to false here.
  # Per-interface useDHCP will be mandatory in the future, so this generated config
  # replicates the default behaviour.
  networking.useDHCP = false;
  networking.interfaces.enp1s0.useDHCP = true;

  # Configure network proxy if necessary
  # networking.proxy.default = "http://user:password@proxy:port/";
  # networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Select internationalisation properties.
  i18n.defaultLocale = "en_US.UTF-8";
  console = {
    font = "Lat2-Terminus16";
    keyMap = "us";
  };

  # Enable the X11 windowing system.
  services.xserver.enable = true;
  services.xserver.autorun = true;
  #services.xserver.displayManager.sx.enable = true;
  services.xserver.windowManager.qtile.enable = true;
  services.xserver.displayManager.defaultSession = "none+qtile";
  # picom configuration
  services.picom.enable = true;
  services.picom.backend= "xrender";
  # Configure keymap in X11
  services.xserver.layout = "us";
  # services.xserver.xkbOptions = "eurosign:e";

  # Enable CUPS to print documents.
  # services.printing.enable = true;

  # Enable sound.
  sound.enable = true;
  # hardware.pulseaudio.enable = true;
  services.pipewire.enable = true;
  services.pipewire.media-session.enable = true;
  services.pipewire.alsa.enable = true;
  services.pipewire.pulse.enable = true;
  services.pipewire.socketActivation = true;
  # Bluetooth configuration.
  #hardware.bluetooth.enable = true;
  #hardware.bluetooth.package = pkgs.bluez;
  # Enable touchpad support (enabled default in most desktopManager).
  services.xserver.libinput.enable = true;

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.jvm = {
    isNormalUser = true;
    extraGroups = [ "wheel" ]; # Enable ‘sudo’ for the user.
  };
  # Security
  security.doas.enable = true;
  security.doas.extraConfig = "permit persist jvm as root";
  security.doas.wheelNeedsPassword = true;
  security.sudo.enable = false;
  security.polkit.enable = true;
  # List packages installed in system profile. To search, run:
  # $ nix search wget
  environment.systemPackages = with pkgs; [
    vim # Do not forget to add an editor to edit configuration.nix! The Nano editor is also installed by default.
    mpv
    wget
    firefox
    brave
    xdg-user-dirs
    joplin-desktop
    keepassxc
    flameshot
    youtube-dl
    #multimc
    #usbutils
    nitrogen
    pcmanfm
    alacritty
    xorg.xrandr
    xorg.xkill
    xorg.xinit
    polkit_gnome
    python39Packages.xlib
    # fonts
    noto-fonts
    noto-fonts-cjk
    noto-fonts-emoji
    # themes and icon
    lxappearance
    libsForQt5.qtstyleplugins
    libsForQt5.breeze-icons
    layan-gtk-theme
    capitaine-cursors
  ];
  # themes
  qt5.style = "gtk2";
  # Some programs need SUID wrappers, can be configured further or are
  # started in user sessions.
  # programs.mtr.enable = true;
  # programs.gnupg.agent = {
  #   enable = true;
  #   enableSSHSupport = true;
  # };

  # List services or programs that you want to enable:
  systemd.network.enable = true;
  programs.git.enable = true;
  programs.htop.enable = true;
  programs.java.enable = true;
  i18n.inputMethod.enabled = "ibus";
  i18n.inputMethod.ibus.engines = with pkgs.ibus-engines; [table-chinese];
  #services.fstrim.enable = true;
  #services.fstrim.interval = "weekly";
  # Enable the OpenSSH daemon.
  services.openssh.enable = true;

  # Open ports in the firewall.
  # networking.firewall.allowedTCPPorts = [ ... ];
  # networking.firewall.allowedUDPPorts = [ ... ];
  # Or disable the firewall altogether.
  # networking.firewall.enable = false;

  # This value determines the NixOS release from which the default
  # settings for stateful data, like file locations and database versions
  # on your system were taken. It‘s perfectly fine and recommended to leave
  # this value at the release version of the first install of this system.
  # Before changing this value read the documentation for this option
  # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
  system.stateVersion = "21.11"; # Did you read the comment?

}