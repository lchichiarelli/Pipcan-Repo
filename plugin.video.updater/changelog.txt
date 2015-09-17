<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.updater"
       name="Updater"
       version="0.0.3"
       provider-name="Pipcan">
  <requires>
    <import addon="xbmc.python" version="2.1.0"/>
  </requires>
  <extension point="xbmc.python.pluginsource"
            library="default.py">
        <provides>video</provides>
  </extension>
  <extension point="xbmc.addon.metadata">
    <summary lang="en">Updater </summary>
    <language>en</language>
    <description lang="en"></description>
     <platform>all</platform>
  </extension>
</addon>
