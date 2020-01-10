%global         majorminor 1.0
%global         _gobject_introspection  1.31.1

# Turn of extras package on RHEL.
%if ! 0%{?rhel}
%bcond_without extras
%else
%bcond_with extras
%endif

Name:           gstreamer1-plugins-bad-free
Version:        1.10.4
Release:        3%{?dist}
Summary:        GStreamer streaming media framework "bad" plugins

License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/
# The source is:
# http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
# modified with gst-p-bad-cleanup.sh from SOURCE1
Source0:        gst-plugins-bad-free-%{version}.tar.xz
Source1:        gst-p-bad-cleanup.sh

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  check
BuildRequires:  gettext-devel
BuildRequires:  libXt-devel
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel >= %{_gobject_introspection}

BuildRequires:  bzip2-devel
BuildRequires:  exempi-devel
BuildRequires:  gsm-devel
BuildRequires:  jasper-devel
BuildRequires:  ladspa-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  libexif-devel
BuildRequires:  libiptcdata-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  liboil-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsndfile-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openssl-devel
BuildRequires:  orc-devel
BuildRequires:  soundtouch-devel
BuildRequires:  wavpack-devel
BuildRequires:  opus-devel
BuildRequires:  nettle-devel
BuildRequires:  libgcrypt-devel
%if 0%{?fedora}
BuildRequires:  libwayland-client-devel
%endif
BuildRequires:  gnutls-devel
BuildRequires:  libsrtp-devel
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  gtk3-devel >= 3.4

BuildRequires:  chrpath

%if %{with extras}
BuildRequires:  bluez-libs-devel >= 5.0
BuildRequires:  libbs2b-devel >= 3.1.0
## Plugins not ported
#BuildRequires:  dirac-devel
#BuildRequires:  gmyth-devel >= 0.4
BuildRequires:  fluidsynth-devel
BuildRequires:  libass-devel
BuildRequires:  libchromaprint-devel
## Plugin not ported
#BuildRequires:  libcdaudio-devel
BuildRequires:  libcurl-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  libkate-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libofa-devel
## Plugins not ported
#BuildRequires:  libmusicbrainz-devel
#BuildRequires:  libtimidity-devel
BuildRequires:  libvdpau-devel
BuildRequires:  openal-soft-devel
#BuildRequires:  opencv-devel
BuildRequires:  openjpeg-devel
BuildRequires:  schroedinger-devel
## Plugins not ported
#BuildRequires:  SDL-devel
#BuildRequires:  slv2-devel
BuildRequires:  wildmidi-devel
BuildRequires:  zbar-devel
BuildRequires:  zvbi-devel
BuildRequires:  OpenEXR-devel
%endif


%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that aren't tested well enough, or the code
is not of good enough quality.

%package gtk
Summary:         GStreamer "bad" plugins gtk plugin
Requires:        %{name} = %{version}-%{release}

%description gtk
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-gtk) contains the gtksink output plugin.


%if %{with extras}
%package extras
Summary:         Extra GStreamer "bad" plugins (less often used "bad" plugins)
Requires:        %{name} = %{version}-%{release}


%description extras
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-extras) contains
extra "bad" plugins for sources (mythtv), sinks (fbdev) and
effects (pitch) which are not used very much and require additional
libraries to be installed.


%package fluidsynth
Summary:         GStreamer "bad" plugins fluidsynth plugin
Requires:        %{name} = %{version}-%{release}
Requires:        soundfont2-default

%description fluidsynth
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-fluidsynth) contains the fluidsynth
plugin which allows playback of midi files.


%package wildmidi
Summary:         GStreamer "bad" plugins wildmidi plugin
Requires:        %{name} = %{version}-%{release}

%description wildmidi
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

gstreamer-plugins-bad contains plug-ins that aren't tested well enough,
or the code is not of good enough quality.

This package (%{name}-wildmidi) contains the wildmidi
plugin which allows playback of midi files.
%endif


%package devel
Summary:        Development files for the GStreamer media framework "bad" plug-ins
Requires:       %{name} = %{version}-%{release}
Requires:       gstreamer1-plugins-base-devel


%description devel
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development files for the plug-ins that
aren't tested well enough, or the code is not of good enough quality.


%prep
%setup -q -n gst-plugins-bad-%{version}


%build
%configure --disable-silent-rules --disable-fatal-warnings \
    --with-package-name="GStreamer-plugins-bad-free package" \
    --with-package-origin="http://www.redhat.com" \
    %{!?with_extras:--disable-fbdev --disable-decklink --disable-linsys \
      --disable-assrender --disable-bluez --disable-bs2b --disable-curl \
      --disable-dc1394 --disable-fluidsynth --disable-gme --disable-kate \
      --disable-modplug --disable-openexr --disable-qt --disable-schro \
      --disable-teletextdec --disable-vdpau --disable-webrtcdsp \
      --disable-wildmidi --disable-zbar --disable-wayland } \
    --enable-debug --disable-static --enable-gtk-doc --enable-experimental \
    --disable-dts --disable-faac --disable-faad --disable-nas \
    --disable-mimic --disable-libmms --disable-mpeg2enc --disable-mplex \
    --disable-neon --disable-openal --disable-rtmp --disable-xvid \
    --disable-chromaprint --disable-eglgles --disable-flite \
    --disable-ofa --disable-opencv --disable-sbc \
    --disable-spandsp --disable-uvch264 --disable-voamrwbenc \
    --disable-webp --disable-openjpeg --disable-x265
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gstreamer-bad-free.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 Richard Hughes <richard@hughsie.com> -->
<component type="codec">
  <id>gstreamer-bad-free</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - Extra</name>
  <summary>Multimedia playback for AIFF, DVB, GSM, MIDI, MXF and Opus</summary>
  <description>
    <p>
      This addon includes several additional codecs that are missing
      something - perhaps a good code review, some documentation, a set of
      tests, a real live maintainer, or some actual wide use.
      However, they might be good enough to play your media files.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <keywords>
    <keyword>AIFF</keyword>
    <keyword>DVB</keyword>
    <keyword>GSM</keyword>
    <keyword>MIDI</keyword>
    <keyword>MXF</keyword>
    <keyword>Opus</keyword>
  </keywords>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%find_lang gst-plugins-bad-%{majorminor}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Kill rpath
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstgtksink.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
%if %{with extras}
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstvdpau.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
%endif
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgstadaptivedemux-%{majorminor}.so
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgstbadvideo-%{majorminor}.so


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files -f gst-plugins-bad-%{majorminor}.lang
%license COPYING COPYING.LIB
%doc AUTHORS README REQUIREMENTS

%{_datadir}/appdata/*.appdata.xml

# presets
%dir %{_datadir}/gstreamer-%{majorminor}/presets/
%{_datadir}/gstreamer-%{majorminor}/presets/GstFreeverb.prs

# opencv data
#%dir %{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/
#%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/fist.xml
#%{_datadir}/gst-plugins-bad/%{majorminor}/opencv_haarcascades/palm.xml

%{_libdir}/libgstadaptivedemux-%{majorminor}.so.*
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so.*
%{_libdir}/libgstbadaudio-%{majorminor}.so.*
%{_libdir}/libgstbadbase-%{majorminor}.so.*
%{_libdir}/libgstbadvideo-%{majorminor}.so.*
%{_libdir}/libgstcodecparsers-%{majorminor}.so.*
%{_libdir}/libgstgl-%{majorminor}.so.*
%{_libdir}/libgstinsertbin-%{majorminor}.so.*
%{_libdir}/libgstmpegts-%{majorminor}.so.*
%{_libdir}/libgstplayer-%{majorminor}.so.*
%{_libdir}/libgstphotography-%{majorminor}.so.*
%{_libdir}/libgsturidownloader-%{majorminor}.so.*
%if 0%{?fedora}
%{_libdir}/libgstwayland-%{majorminor}.so.*
%endif

%{_libdir}/girepository-1.0/GstGL-1.0.typelib
%{_libdir}/girepository-1.0/GstInsertBin-1.0.typelib
%{_libdir}/girepository-1.0/GstMpegts-1.0.typelib
%{_libdir}/girepository-1.0/GstPlayer-1.0.typelib

# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstaccurip.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstaiff.so
%{_libdir}/gstreamer-%{majorminor}/libgstasfmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{majorminor}/libgstautoconvert.so
%{_libdir}/gstreamer-%{majorminor}/libgstbayer.so
%{_libdir}/gstreamer-%{majorminor}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstcompositor.so
%{_libdir}/gstreamer-%{majorminor}/libgstdashdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstdataurisrc.so
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstfbdevsink.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstfestival.so
%{_libdir}/gstreamer-%{majorminor}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{majorminor}/libgstfreeverb.so
%{_libdir}/gstreamer-%{majorminor}/libgstfrei0r.so
%{_libdir}/gstreamer-%{majorminor}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{majorminor}/libgstgdp.so
%{_libdir}/gstreamer-%{majorminor}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3tag.so
%{_libdir}/gstreamer-%{majorminor}/libgstinter.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstivfparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstivtc.so
%{_libdir}/gstreamer-%{majorminor}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpegformat.so
%{_libdir}/gstreamer-%{majorminor}/libgstmidi.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstmxf.so
%{_libdir}/gstreamer-%{majorminor}/libgstnetsim.so
%{_libdir}/gstreamer-%{majorminor}/libgstpcapparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstpnm.so
%{_libdir}/gstreamer-%{majorminor}/libgstrawparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstremovesilence.so
%{_libdir}/gstreamer-%{majorminor}/libgstresindvd.so
%{_libdir}/gstreamer-%{majorminor}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{majorminor}/libgstrsvg.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtponvif.so
%{_libdir}/gstreamer-%{majorminor}/libgstsdpelem.so
%{_libdir}/gstreamer-%{majorminor}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{majorminor}/libgstshm.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmooth.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeed.so
%{_libdir}/gstreamer-%{majorminor}/libgststereo.so
%{_libdir}/gstreamer-%{majorminor}/libgstsubenc.so
%{_libdir}/gstreamer-%{majorminor}/libgsttimecode.so
%if %{with extras}
%{_libdir}/gstreamer-%{majorminor}/libgstvdpau.so
%endif
%{_libdir}/gstreamer-%{majorminor}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideosignal.so
%{_libdir}/gstreamer-%{majorminor}/libgstvmnc.so
%{_libdir}/gstreamer-%{majorminor}/libgstyadif.so
%{_libdir}/gstreamer-%{majorminor}/libgsty4mdec.so

# System (Linux) specific plugins
%{_libdir}/gstreamer-%{majorminor}/libgstdvb.so
%{_libdir}/gstreamer-%{majorminor}/libgstvcdsrc.so

# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstbz2.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtls.so
%{_libdir}/gstreamer-%{majorminor}/libgsthls.so
%{_libdir}/gstreamer-%{majorminor}/libgstgsm.so
%{_libdir}/gstreamer-%{majorminor}/libgstkmssink.so
%{_libdir}/gstreamer-%{majorminor}/libgstladspa.so
%{_libdir}/gstreamer-%{majorminor}/libgstmusepack.so
%{_libdir}/gstreamer-%{majorminor}/libgstopengl.so
%{_libdir}/gstreamer-%{majorminor}/libgstopusparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstsndfile.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{majorminor}/libgstsrtp.so
%if 0%{?fedora}
%{_libdir}/gstreamer-%{majorminor}/libgstwaylandsink.so
%endif

#debugging plugin
%{_libdir}/gstreamer-%{majorminor}/libgstdebugutilsbad.so

%files gtk
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstgtksink.so


%if %{with extras}
%files extras
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstassrender.so
%{_libdir}/gstreamer-%{majorminor}/libgstbluez.so
%{_libdir}/gstreamer-%{majorminor}/libgstbs2b.so
%{_libdir}/gstreamer-%{majorminor}/libgstchromaprint.so
%{_libdir}/gstreamer-%{majorminor}/libgstcurl.so
%{_libdir}/gstreamer-%{majorminor}/libgstdecklink.so
%{_libdir}/gstreamer-%{majorminor}/libgstgme.so
%{_libdir}/gstreamer-%{majorminor}/libgstkate.so
%{_libdir}/gstreamer-%{majorminor}/libgstmodplug.so
%{_libdir}/gstreamer-%{majorminor}/libgstofa.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenal.so
#%{_libdir}/gstreamer-%{majorminor}/libgstopencv.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenexr.so
%{_libdir}/gstreamer-%{majorminor}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstschro.so
%{_libdir}/gstreamer-%{majorminor}/libgstteletextdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstzbar.so


%files fluidsynth
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstfluidsynthmidi.so

%files wildmidi
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstwildmidi.so
%endif


%files devel
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-plugins-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gst-plugins-bad-libs-%{majorminor}

%{_datadir}/gir-1.0/GstGL-1.0.gir
%{_datadir}/gir-1.0/GstInsertBin-%{majorminor}.gir
%{_datadir}/gir-1.0/GstMpegts-%{majorminor}.gir
%{_datadir}/gir-1.0/GstPlayer-%{majorminor}.gir

%{_libdir}/libgstadaptivedemux-%{majorminor}.so
%{_libdir}/libgstbasecamerabinsrc-%{majorminor}.so
%{_libdir}/libgstbadaudio-%{majorminor}.so
%{_libdir}/libgstbadbase-%{majorminor}.so
%{_libdir}/libgstbadvideo-%{majorminor}.so
%{_libdir}/libgstcodecparsers-%{majorminor}.so
%{_libdir}/libgstgl-%{majorminor}.so
%{_libdir}/libgstinsertbin-%{majorminor}.so
%{_libdir}/libgstmpegts-%{majorminor}.so
%{_libdir}/libgstplayer-%{majorminor}.so
%{_libdir}/libgstphotography-%{majorminor}.so
%{_libdir}/libgsturidownloader-%{majorminor}.so
%if 0%{?fedora}
%{_libdir}/libgstwayland-%{majorminor}.so
%endif

%{_libdir}/gstreamer-%{majorminor}/include/gst/gl/gstglconfig.h

%{_includedir}/gstreamer-%{majorminor}/gst/audio
%{_includedir}/gstreamer-%{majorminor}/gst/base
%{_includedir}/gstreamer-%{majorminor}/gst/basecamerabinsrc
%{_includedir}/gstreamer-%{majorminor}/gst/codecparsers
%{_includedir}/gstreamer-%{majorminor}/gst/insertbin
%{_includedir}/gstreamer-%{majorminor}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{majorminor}/gst/mpegts
%{_includedir}/gstreamer-%{majorminor}/gst/player
%{_includedir}/gstreamer-%{majorminor}/gst/uridownloader
%{_includedir}/gstreamer-%{majorminor}/gst/gl
%{_includedir}/gstreamer-%{majorminor}/gst/video

# pkg-config files
%{_libdir}/pkgconfig/gstreamer-bad-audio-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-bad-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-bad-video-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-gl-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-player-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{majorminor}.pc

%changelog
* Mon Oct 09 2017 Wim Taymans <wtaymans@redhat.com> - 1.10.4-3
- Disable wayland sink plugin
- Resolves: #1488978

* Thu Mar 09 2017 Wim Taymans <wtaymans@redhat.com> - 1.10.4-2
- Disable plugins
- Fix origin
- Resolves: #1429587

* Mon Mar 06 2017 Wim Taymans <wtaymans@redhat.com> - 1.10.4-1
- Update to 1.10.4
- Remove unbuilt plugins
- Resolves: #1429587

* Wed Dec 07 2016 Wim Taymans <wtaymans@redhat.com> - 1.4.5-6
- Fix h264 and h265 buffer size checks
- Fix mpegts pat parsing and add more size checks
Resolves: rhbz#1400898

* Tue Dec 06 2016 Wim Taymans <wtaymans@redhat.com> - 1.4.5-5
- vmncdec: Sanity-check width/height before using it
Resolves: rhbz#1400898

* Thu May 26 2016 Wim Taymans <wtaymans@redhat.com> - 1.4.5-4
- rebuild for libdvdnav update
- Resolves: #1340047

* Thu Jul 30 2015 Wim Taymans <wtaymans@redhat.com> - 1.4.5-3
- Update audiomixer unit test for big endian
- add missing patch
- Resolves: #1226909

* Mon Jun 22 2015 Wim Taymans <wtaymans@redhat.com> - 1.4.5-2
- Update ORC backup file
- Resolves: #1174403

* Tue May 12 2015 Wim Taymans <wtaymans@redhat.com> - 1.4.5-1
- Update to 1.4.5
- Resolves: #1174403

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.4-2
- rebuild (openexr)

* Fri Nov 14 2014 Kalev Lember <kalevlember@gmail.com> - 1.4.4-1
- Update to 1.4.4

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 1.4.2-3
- Rebuild for new libsrtp

* Mon Sep 22 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.2-2
- Remove celt buildreq, the plugin was removed and so is celt-devel

* Mon Sep 22 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.2-1
- Update to 1.4.2.

* Fri Aug 29 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.1-1
- Update to 1.4.1.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Wim Taymans <wtaymans@redhat.com> - 1.4.0-1
- Update to 1.4.0.

* Fri Jul 11 2014 Wim Taymans <wtaymans@redhat.com> - 1.3.91-1
- Update to 1.3.91.
- Remove old libraries

* Tue Jun 17 2014 Wim Taymans <wtaymans@redhat.com> - 1.2.4-1
- Update to 1.2.4.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Hans de Goede <hdegoede@}redhat.com> - 1.2.3-3
- Put the fluidsynth plugin in its own subpackage and make it require
  soundfont2-default (rhbz#1078925)

* Wed Mar 19 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-2
- Bump (libass)

* Mon Feb 10 2014 Brian Pepple <bpepple@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3.

* Thu Feb  6 2014 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-2
- Build the srtp plugin. (#1055669)

* Fri Dec 27 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2.

* Fri Nov 15 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-4
- Build fluidsynth plugin. (#1024906)

* Thu Nov 14 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-3
- Add BR on gnutls-devel for HLS support. (#1030491)

* Mon Nov 11 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-2
- Build ladspa, libkate, and wildmidi plugins.

* Mon Nov 11 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1.

* Fri Nov  8 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.0-3
- Build gobject-introspection support. (#1028156)

* Fri Oct 04 2013 Bastien Nocera <bnocera@redhat.com> 1.2.0-2
- Build the wayland video output plugin

* Tue Sep 24 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0.

* Thu Sep 19 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.90-1
- Update to 1.1.90.

* Wed Aug 28 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.4-1
- Update to 1.1.4.

* Mon Jul 29 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3.

* Fri Jul 12 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2.

* Tue May 07 2013 Colin Walters <walters@verbum.org> - 1.0.7-2
- Move libgstdecklink to its correct place in extras; needed for RHEL

* Fri Apr 26 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7.

* Sun Mar 24 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6.
- Drop BR on PyXML.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Brian Pepple <bpepple@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Wed Dec 19 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Nov 21 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Thu Oct 25 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Sun Oct  7 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1
- Add frei0r plugin to file list.

* Mon Oct  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-3
- Enable verbose build

* Wed Sep 26 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.0-2
- Build opus plugin.

* Mon Sep 24 2012 Brian Pepple <bpepple@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0.

* Thu Sep 20 2012 Bastien Nocera <bnocera@redhat.com> 0.11.99-2
- The soundtouch-devel BR should be on, even with extras disabled

* Wed Sep 19 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.99-1
- Update to 0.11.99

* Fri Sep 14 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.94-1
- Update to 0.11.94.

* Sat Aug 18 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.93-2
- Fix permission on tarball clean-up script.
- Re-enable soundtouch-devel.
- Add COPYING.LIB to package.
- Use %%global instead of %%define.

* Wed Aug 15 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.93-1
- Update to 0.11.93.

* Fri Jul 20 2012 Brian Pepple <bpepple@fedoraproject.org> - 0.11.92-1
- Initial Fedora spec file.
