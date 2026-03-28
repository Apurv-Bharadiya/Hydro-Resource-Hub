<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.28.0-Firenze" styleCategories="Symbology">
  <pipe>
    <provider>
      <rasterrenderer type="singlebandpseudocolor" alphaBand="-1" band="1" opacity="1">
        <rasterTransparency/>
        <rastershader>
          <colorrampshader labelPrecision="0" colorRampType="INTERPOLATED" clip="0" minimumValue="0" maximumValue="3000">
            <colorramp type="gradient" name="[source]">
              <prop k="color1" v="43,131,186,255"/>
              <prop k="color2" v="215,25,28,255"/>
              <prop k="discrete" v="0"/>
              <prop k="stops" v="0.25;171,221,164,255:0.5;255,255,191,255:0.75;253,174,97,255"/>
            </colorramp>
            <item alpha="255" value="0" label="0 m (Sea Level)" color="#2b83ba"/>
            <item alpha="255" value="750" label="750 m" color="#abdda4"/>
            <item alpha="255" value="1500" label="1500 m" color="#ffffbf"/>
            <item alpha="255" value="2250" label="2250 m" color="#fdae61"/>
            <item alpha="255" value="3000" label="3000 m (High Peaks)" color="#d7191c"/>
          </colorrampshader>
        </rastershader>
      </rasterrenderer>
    </provider>
  </pipe>
</qgis>
