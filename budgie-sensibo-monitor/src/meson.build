install_data(
    'budgie-sensibo-monitor.plugin',
    'budgie-sensibo-monitor.ui',
    install_dir: APPLET_INSTALL_DIR
)

install_data(
    'com.solus-project.budgie-sensibo-monitor.gschema.xml',
    install_dir: join_paths(datadir, 'glib-2.0', 'schemas'),
)

install_data(
    'budgie-sensibo-monitor-icon.svg',
    'budgie-sensibo-monitor-icon-on.svg',
    install_dir: PIXMAPS_DIR
)

meson.add_install_script('meson_post_install')
