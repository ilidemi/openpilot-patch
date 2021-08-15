set -e

patch /data/openpilot/selfdrive/ui/qt/widgets/setup.cc widgets_setup.cc_nice_drive.patch
patch /data/openpilot/selfdrive/version.py version.py.patch
patch /data/openpilot/selfdrive/common/version.h version.h.patch
rm /data/openpilot/selfdrive/ui/libqt_widgets.a