set -e

patch /data/openpilot/selfdrive/ui/qt/widgets/setup.cc widgets_setup.cc_remove_ad.patch
rm /data/openpilot/selfdrive/ui/libqt_widgets.a