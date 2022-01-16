#!/usr/bin/env python3

r"""

This file is part of Embroidermodder 2.

------------------------------------------------------------

    Copyright 2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE.txt for licensing terms.

------------------------------------------------------------

This file is only for metaprogramming:

    * Code style maintenence: if you do something that the
      compiler considers correct but we try not to as part
      of the house style this'll correct it.

    * Datablocks like configuration can be stored in as
      JSON and be manipulated by database software then
      converted into C structs on compilation.

    * Enums that are maintained with defines can be corrected
      here, so say you have
      
      ```
      /* enum: sequential 30 */
      #define CONSTANT_a   3
      #define CONSTANT_c     5
      #define CONSTANT_f   2
      /* end enum */
      ```
      
      is processed to:
      
      ```
      /* enum: sequential 30 */
      #define CONSTANT_a          0
      #define CONSTANT_c          1
      #define CONSTANT_f          2
      /* end enum */
      ```
      
      the comments instruct this script to do the job.
      
      Note: we don't do enums, because of the amount of
      switch statements used in the source.
      
    * Since python isn't maintained as a dependency, all the
      libraries called here are standard libraries. It should
      run fine on any system that can build the software since
      it's now a standard part of operating systems.
      
      Windows users may need to install Python as a new step.

This will run before compilation, chained within the build
scripts.

"""

import os
import json

def process_json(a):
    r"""
    The jobs carried out by this processor are:
    
        * convert C struct data stored as JSON to C code
    """
    s = """/* This file is part of Embroidermodder 2.
 * ------------------------------------------------------------
 * Copyright 2021 The Embroidermodder Team
 * Embroidermodder 2 is Open Source Software.
 * See LICENSE.txt for licensing terms.
 * ------------------------------------------------------------
 * This file is only for data and declarations that
 * are compiled into the source.
 */

#include "embroidermodder.h"

"""

    for k in a.keys():
        if k[-4:] == "_xpm":
            s += "const char *%s[];\n" % k

    s += """
#include "icons/aligntextangle.xpm"
#include "icons/aligntextcenter.xpm"
#include "icons/aligntexthome.xpm"
#include "icons/aligntextleft.xpm"
#include "icons/aligntextright.xpm"
#include "icons/angulardimension.xpm"
#include "icons/app.xpm"
#include "icons/arc3points.xpm"
#include "icons/arccenterstartangle.xpm"
#include "icons/arccenterstartend.xpm"
#include "icons/arccenterstartlength.xpm"
#include "icons/arccontinue.xpm"
#include "icons/arcstartcenterangle.xpm"
#include "icons/arcstartcenterend.xpm"
#include "icons/arcstartcenterlength.xpm"
#include "icons/arcstartendangle.xpm"
#include "icons/arcstartenddirection.xpm"
#include "icons/arcstartendradius.xpm"
#include "icons/arc.xpm"
#include "icons/area.xpm"
#include "icons/array.xpm"
#include "icons/backview.xpm"
#include "icons/baselinedimension.xpm"
#include "icons/bean.xpm"
#include "icons/blank.xpm"
#include "icons/bottomview.xpm"
#include "icons/boundary.xpm"
#include "icons/break2points.xpm"
#include "icons/breakatpoint.xpm"
#include "icons/browser.xpm"
#include "icons/camera.xpm"
#include "icons/centermark.xpm"
#include "icons/chamfer.xpm"
#include "icons/changelog.xpm"
#include "icons/check.xpm"
#include "icons/circle2points.xpm"
#include "icons/circle3points.xpm"
#include "icons/circlecenterdiameter.xpm"
#include "icons/circlecenterradius.xpm"
#include "icons/circletantanradius.xpm"
#include "icons/circletantantan.xpm"
#include "icons/circle.xpm"
#include "icons/cloud-2.xpm"
#include "icons/cloud.xpm"
#include "icons/colorblue.xpm"
#include "icons/colorbyblock.xpm"
#include "icons/colorbylayer.xpm"
#include "icons/colorcyan.xpm"
#include "icons/colorgreen.xpm"
#include "icons/colormagenta.xpm"
#include "icons/colorother.xpm"
#include "icons/colorred.xpm"
#include "icons/colorselector.xpm"
#include "icons/colorwhite.xpm"
#include "icons/coloryellow.xpm"
#include "icons/constructionline.xpm"
#include "icons/continuedimension.xpm"
#include "icons/copyobject.xpm"
#include "icons/copy.xpm"
#include "icons/customizekeyboard.xpm"
#include "icons/customizemenus.xpm"
#include "icons/customizetoolbars.xpm"
#include "icons/customize.xpm"
#include "icons/cut.xpm"
#include "icons/date.xpm"
#include "icons/day.xpm"
#include "icons/designdetails.xpm"
#include "icons/diameterdimension.xpm"
#include "icons/dimensionedit.xpm"
#include "icons/dimensionstyle.xpm"
#include "icons/dimensiontextedit.xpm"
#include "icons/dimensionupdate.xpm"
#include "icons/distance.xpm"
#include "icons/dolphin.xpm"
#include "icons/donothing.xpm"
#include "icons/donut-2.xpm"
#include "icons/donut.xpm"
#include "icons/drawing2.xpm"
#include "icons/drawing.xpm"
#include "icons/ellipsearc.xpm"
#include "icons/ellipseaxisend.xpm"
#include "icons/ellipsecenter.xpm"
#include "icons/ellipse.xpm"
#include "icons/erase.xpm"
#include "icons/escape.xpm"
#include "icons/exit.xpm"
#include "icons/explode.xpm"
#include "icons/extend.xpm"
#include "icons/fillet.xpm"
#include "icons/findandreplace.xpm"
#include "icons/freezealllayers.xpm"
#include "icons/frontview.xpm"
#include "icons/gridsettings.xpm"
#include "icons/gridsnapsettings.xpm"
#include "icons/hatch.xpm"
#include "icons/heart-2.xpm"
#include "icons/heart.xpm"
#include "icons/help-2.xpm"
#include "icons/help.xpm"
#include "icons/hex.xpm"
#include "icons/hidealllayers.xpm"
#include "icons/histogram.xpm"
#include "icons/icon128.xpm"
#include "icons/icon16.xpm"
#include "icons/icon24.xpm"
#include "icons/icon32.xpm"
#include "icons/icon48.xpm"
#include "icons/icon64.xpm"
#include "icons/inquiry.xpm"
#include "icons/insertblock.xpm"
#include "icons/join.xpm"
#include "icons/justifytext.xpm"
#include "icons/layerprevious.xpm"
#include "icons/layerselector.xpm"
#include "icons/layers.xpm"
#include "icons/layertranslate.xpm"
#include "icons/leftview.xpm"
#include "icons/lengthen.xpm"
#include "icons/lineardimension.xpm"
#include "icons/linetypebyblock.xpm"
#include "icons/linetypebylayer.xpm"
#include "icons/linetypecenter.xpm"
#include "icons/linetypecontinuous.xpm"
#include "icons/linetypehidden.xpm"
#include "icons/linetypeother.xpm"
#include "icons/linetypeselector.xpm"
#include "icons/lineweight01.xpm"
#include "icons/lineweight02.xpm"
#include "icons/lineweight03.xpm"
#include "icons/lineweight04.xpm"
#include "icons/lineweight05.xpm"
#include "icons/lineweight06.xpm"
#include "icons/lineweight07.xpm"
#include "icons/lineweight08.xpm"
#include "icons/lineweight09.xpm"
#include "icons/lineweight10.xpm"
#include "icons/lineweight11.xpm"
#include "icons/lineweight12.xpm"
#include "icons/lineweight13.xpm"
#include "icons/lineweight14.xpm"
#include "icons/lineweight15.xpm"
#include "icons/lineweight16.xpm"
#include "icons/lineweight17.xpm"
#include "icons/lineweight18.xpm"
#include "icons/lineweight19.xpm"
#include "icons/lineweight20.xpm"
#include "icons/lineweight21.xpm"
#include "icons/lineweight22.xpm"
#include "icons/lineweight23.xpm"
#include "icons/lineweight24.xpm"
#include "icons/lineweightbyblock.xpm"
#include "icons/lineweightbylayer.xpm"
#include "icons/lineweightdefault.xpm"
#include "icons/lineweightselector.xpm"
#include "icons/lineweightsettings.xpm"
#include "icons/line.xpm"
#include "icons/list.xpm"
#include "icons/locatepoint.xpm"
#include "icons/locator-snaptoapparentintersection.xpm"
#include "icons/locator-snaptocenter.xpm"
#include "icons/locator-snaptoendpoint.xpm"
#include "icons/locator-snaptoextension.xpm"
#include "icons/locator-snaptoinsert.xpm"
#include "icons/locator-snaptointersection.xpm"
#include "icons/locator-snaptomidpoint.xpm"
#include "icons/locator-snaptonearest.xpm"
#include "icons/locator-snaptonode.xpm"
#include "icons/locator-snaptoparallel.xpm"
#include "icons/locator-snaptoperpendicular.xpm"
#include "icons/locator-snaptoquadrant.xpm"
#include "icons/locator-snaptotangent.xpm"
#include "icons/lockalllayers.xpm"
#include "icons/makeblock.xpm"
#include "icons/makelayercurrent.xpm"
#include "icons/mass.xpm"
#include "icons/mirror.xpm"
#include "icons/move.xpm"
#include "icons/multilinetext.xpm"
#include "icons/multiline.xpm"
#include "icons/namedviews.xpm"
#include "icons/neisometricview.xpm"
#include "icons/new.xpm"
#include "icons/night.xpm"
#include "icons/nopreview.xpm"
#include "icons/nwisometricview.xpm"
#include "icons/obliquedimensions.xpm"
#include "icons/offset.xpm"
#include "icons/open.xpm"
#include "icons/ordinatedimension.xpm"
#include "icons/orthosettings.xpm"
#include "icons/pandown.xpm"
#include "icons/panleft.xpm"
#include "icons/panpoint.xpm"
#include "icons/panrealtime.xpm"
#include "icons/panright.xpm"
#include "icons/panup.xpm"
#include "icons/pan.xpm"
#include "icons/paste.xpm"
#include "icons/path.xpm"
#include "icons/pickadd.xpm"
#include "icons/picknew.xpm"
#include "icons/plugin.xpm"
#include "icons/pointdivide.xpm"
#include "icons/pointmeasure.xpm"
#include "icons/pointmultiple.xpm"
#include "icons/pointsingle.xpm"
#include "icons/point.xpm"
#include "icons/polarsettings.xpm"
#include "icons/polygon.xpm"
#include "icons/polyline.xpm"
#include "icons/print.xpm"
#include "icons/pyscript.xpm"
#include "icons/qsnapsettings.xpm"
#include "icons/qtracksettings.xpm"
#include "icons/quickdimension.xpm"
#include "icons/quickleader.xpm"
#include "icons/quickselect.xpm"
#include "icons/radiusdimension.xpm"
#include "icons/ray.xpm"
#include "icons/rectangle.xpm"
#include "icons/redo.xpm"
#include "icons/region.xpm"
#include "icons/render.xpm"
#include "icons/rgb.xpm"
#include "icons/rightview.xpm"
#include "icons/rotate.xpm"
#include "icons/rulersettings.xpm"
#include "icons/sandbox.xpm"
#include "icons/satin.xpm"
#include "icons/saveas.xpm"
#include "icons/save.xpm"
#include "icons/scale.xpm"
#include "icons/seisometricview.xpm"
#include "icons/settingsdialog-2.xpm"
#include "icons/settingsdialog.xpm"
#include "icons/shade2dwireframe.xpm"
#include "icons/shade3dwireframe.xpm"
#include "icons/shadeflatedges.xpm"
#include "icons/shadeflat.xpm"
#include "icons/shadehidden.xpm"
#include "icons/shadesmoothedges.xpm"
#include "icons/shadesmooth.xpm"
#include "icons/shade.xpm"
#include "icons/showalllayers.xpm"
#include "icons/singlelinetext.xpm"
#include "icons/sketch-2.xpm"
#include "icons/sketch.xpm"
#include "icons/snapfrom.xpm"
#include "icons/snaptoapparentintersection.xpm"
#include "icons/snaptocenter.xpm"
#include "icons/snaptoendpoint.xpm"
#include "icons/snaptoextension.xpm"
#include "icons/snaptoinsert.xpm"
#include "icons/snaptointersection.xpm"
#include "icons/snaptomidpoint.xpm"
#include "icons/snaptonearest.xpm"
#include "icons/snaptonode.xpm"
#include "icons/snaptonone.xpm"
#include "icons/snaptoparallel.xpm"
#include "icons/snaptoperpendicular.xpm"
#include "icons/snaptoquadrant.xpm"
#include "icons/snaptotangent.xpm"
#include "icons/snowflake-2.xpm"
#include "icons/snowflake.xpm"
#include "icons/solidbox.xpm"
#include "icons/solidcheck.xpm"
#include "icons/solidclean.xpm"
#include "icons/solidcoloredges.xpm"
#include "icons/solidcolorfaces.xpm"
#include "icons/solidcone.xpm"
#include "icons/solidcopyedges.xpm"
#include "icons/solidcopyfaces.xpm"
#include "icons/solidcylinder.xpm"
#include "icons/soliddeletefaces.xpm"
#include "icons/solidextrudefaces.xpm"
#include "icons/solidextrude.xpm"
#include "icons/solidimprint.xpm"
#include "icons/solidinterfere.xpm"
#include "icons/solidintersect.xpm"
#include "icons/solidmovefaces.xpm"
#include "icons/solidoffsetfaces.xpm"
#include "icons/solidrevolve.xpm"
#include "icons/solidrotatefaces.xpm"
#include "icons/solidsection.xpm"
#include "icons/solidsediting.xpm"
#include "icons/solidseparate.xpm"
#include "icons/solidsetupdrawing.xpm"
#include "icons/solidsetupprofile.xpm"
#include "icons/solidsetupview.xpm"
#include "icons/solidsetup.xpm"
#include "icons/solidshell.xpm"
#include "icons/solidslice.xpm"
#include "icons/solidsphere.xpm"
#include "icons/solidsubtract.xpm"
#include "icons/solids.xpm"
#include "icons/solidtaperfaces.xpm"
#include "icons/solidtorus.xpm"
#include "icons/solidunion.xpm"
#include "icons/solidwedge.xpm"
#include "icons/spline.xpm"
#include "icons/star.xpm"
#include "icons/stretch.xpm"
#include "icons/stub.xpm"
#include "icons/surface2dsolid.xpm"
#include "icons/surface3dface.xpm"
#include "icons/surface3dmesh.xpm"
#include "icons/surfacebox.xpm"
#include "icons/surfacecone.xpm"
#include "icons/surfacecylinder.xpm"
#include "icons/surfacedish.xpm"
#include "icons/surfacedome.xpm"
#include "icons/surfaceedgesurface.xpm"
#include "icons/surfaceedge.xpm"
#include "icons/surfacepyramid.xpm"
#include "icons/surfacerevolvedsurface.xpm"
#include "icons/surfaceruledsurface.xpm"
#include "icons/surfacesphere.xpm"
#include "icons/surfaces.xpm"
#include "icons/surfacetabulatedsurface.xpm"
#include "icons/surfacetorus.xpm"
#include "icons/surfacewedge.xpm"
#include "icons/swisometricview.xpm"
#include "icons/temptrackingpoint.xpm"
#include "icons/textbold.xpm"
#include "icons/textitalic.xpm"
#include "icons/textoverline.xpm"
#include "icons/textstrikeout.xpm"
#include "icons/textunderline.xpm"
#include "icons/text.xpm"
#include "icons/thawalllayers.xpm"
#include "icons/theme.xpm"
#include "icons/tipoftheday-2.xpm"
#include "icons/tipoftheday.xpm"
#include "icons/tolerance.xpm"
#include "icons/topview.xpm"
#include "icons/trim.xpm"
#include "icons/undo.xpm"
#include "icons/units.xpm"
#include "icons/unlockalllayers.xpm"
#include "icons/view.xpm"
#include "icons/whatsthis.xpm"
#include "icons/wideflange.xpm"
#include "icons/windowcascade.xpm"
#include "icons/windowcloseall.xpm"
#include "icons/windowclose.xpm"
#include "icons/windownext.xpm"
#include "icons/windowprevious.xpm"
#include "icons/windowtile.xpm"
#include "icons/world.xpm"
#include "icons/zoomall.xpm"
#include "icons/zoomcenter.xpm"
#include "icons/zoomdynamic.xpm"
#include "icons/zoomextents.xpm"
#include "icons/zoomin.xpm"
#include "icons/zoomout.xpm"
#include "icons/zoomprevious.xpm"
#include "icons/zoomrealtime.xpm"
#include "icons/zoomscale.xpm"
#include "icons/zoomselected.xpm"
#include "icons/zoomwindow.xpm"
#include "icons/zoom.xpm"

const char* _appName_ = "Embroidermodder";
const char* _appVer_ = "v2.0 alpha";
int exitApp = 0;

const char **icons[] = {
    (const char**)_3dviews_xpm,
    (const char**)about_xpm,
    (const char**)aligneddimension_xpm,
    (const char**)aligntextangle_xpm,
    (const char**)aligntextcenter_xpm,
    (const char**)aligntexthome_xpm,
    (const char**)aligntextleft_xpm,
    (const char**)aligntextright_xpm,
    (const char**)aligntext_xpm,
    (const char**)angulardimension_xpm,
    (const char**)app_xpm,
    (const char**)arc3points_xpm,
    (const char**)arccenterstartangle_xpm,
    (const char**)arccenterstartend_xpm,
    (const char**)arccenterstartlength_xpm,
    (const char**)arccontinue_xpm,
    (const char**)arcstartcenterangle_xpm,
    (const char**)arcstartcenterend_xpm,
    (const char**)arcstartcenterlength_xpm,
    (const char**)arcstartendangle_xpm,
    (const char**)arcstartenddirection_xpm,
    (const char**)arcstartendradius_xpm,
    (const char**)arc_xpm,
    (const char**)area_xpm,
    (const char**)array_xpm,
    (const char**)backview_xpm,
    (const char**)baselinedimension_xpm,
    (const char**)bean_xpm,
    (const char**)blank_xpm,
    (const char**)bottomview_xpm,
    (const char**)boundary_xpm,
    (const char**)break2points_xpm,
    (const char**)breakatpoint_xpm,
    (const char**)browser_xpm,
    (const char**)camera_xpm,
    (const char**)centermark_xpm,
    (const char**)chamfer_xpm,
    (const char**)changelog_xpm,
    (const char**)check_xpm,
    (const char**)circle2points_xpm,
    (const char**)circle3points_xpm,
    (const char**)circlecenterdiameter_xpm,
    (const char**)circlecenterradius_xpm,
    (const char**)circletantanradius_xpm,
    (const char**)circletantantan_xpm,
    (const char**)circle_xpm,
    (const char**)cloud_2_xpm,
    (const char**)cloud_xpm,
    (const char**)colorblue_xpm,
    (const char**)colorbyblock_xpm,
    (const char**)colorbylayer_xpm,
    (const char**)colorcyan_xpm,
    (const char**)colorgreen_xpm,
    (const char**)colormagenta_xpm,
    (const char**)colorother_xpm,
    (const char**)colorred_xpm,
    (const char**)colorselector_xpm,
    (const char**)colorwhite_xpm,
    (const char**)coloryellow_xpm,
    (const char**)constructionline_xpm,
    (const char**)continuedimension_xpm,
    (const char**)copyobject_xpm,
    (const char**)copy_xpm,
    (const char**)customizekeyboard_xpm,
    (const char**)customizemenus_xpm,
    (const char**)customizetoolbars_xpm,
    (const char**)customize_xpm,
    (const char**)cut_xpm,
    (const char**)date_xpm,
    (const char**)day_xpm,
    (const char**)designdetails_xpm,
    (const char**)diameterdimension_xpm,
    (const char**)dimensionedit_xpm,
    (const char**)dimensionstyle_xpm,
    (const char**)dimensiontextedit_xpm,
    (const char**)dimensionupdate_xpm,
    (const char**)distance_xpm,
    (const char**)dolphin_xpm,
    (const char**)donothing_xpm,
    (const char**)donut_2_xpm,
    (const char**)donut_xpm,
    (const char**)drawing2_xpm,
    (const char**)drawing_xpm,
    (const char**)ellipsearc_xpm,
    (const char**)ellipseaxisend_xpm,
    (const char**)ellipsecenter_xpm,
    (const char**)ellipse_xpm,
    (const char**)erase_xpm,
    (const char**)escape_xpm,
    (const char**)exit_xpm,
    (const char**)explode_xpm,
    (const char**)extend_xpm,
    (const char**)fillet_xpm,
    (const char**)findandreplace_xpm,
    (const char**)freezealllayers_xpm,
    (const char**)frontview_xpm,
    (const char**)gridsettings_xpm,
    (const char**)gridsnapsettings_xpm,
    (const char**)hatch_xpm,
    (const char**)heart_2_xpm,
    (const char**)heart_xpm,
    (const char**)help_2_xpm,
    (const char**)help_xpm,
    (const char**)hex_xpm,
    (const char**)hidealllayers_xpm,
    (const char**)histogram_xpm,
    (const char**)icon128_xpm,
    (const char**)icon16_xpm,
    (const char**)icon24_xpm,
    (const char**)icon32_xpm,
    (const char**)icon48_xpm,
    (const char**)icon64_xpm,
    (const char**)inquiry_xpm,
    (const char**)insertblock_xpm,
    (const char**)join_xpm,
    (const char**)justifytext_xpm,
    (const char**)layerprevious_xpm,
    (const char**)layerselector_xpm,
    (const char**)layers_xpm,
    (const char**)layertranslate_xpm,
    (const char**)leftview_xpm,
    (const char**)lengthen_xpm,
    (const char**)lineardimension_xpm,
    (const char**)linetypebyblock_xpm,
    (const char**)linetypebylayer_xpm,
    (const char**)linetypecenter_xpm,
    (const char**)linetypecontinuous_xpm,
    (const char**)linetypehidden_xpm,
    (const char**)linetypeother_xpm,
    (const char**)linetypeselector_xpm,
    (const char**)lineweight01_xpm,
    (const char**)lineweight02_xpm,
    (const char**)lineweight03_xpm,
    (const char**)lineweight04_xpm,
    (const char**)lineweight05_xpm,
    (const char**)lineweight06_xpm,
    (const char**)lineweight07_xpm,
    (const char**)lineweight08_xpm,
    (const char**)lineweight09_xpm,
    (const char**)lineweight10_xpm,
    (const char**)lineweight11_xpm,
    (const char**)lineweight12_xpm,
    (const char**)lineweight13_xpm,
    (const char**)lineweight14_xpm,
    (const char**)lineweight15_xpm,
    (const char**)lineweight16_xpm,
    (const char**)lineweight17_xpm,
    (const char**)lineweight18_xpm,
    (const char**)lineweight19_xpm,
    (const char**)lineweight20_xpm,
    (const char**)lineweight21_xpm,
    (const char**)lineweight22_xpm,
    (const char**)lineweight23_xpm,
    (const char**)lineweight24_xpm,
    (const char**)lineweightbyblock_xpm,
    (const char**)lineweightbylayer_xpm,
    (const char**)lineweightdefault_xpm,
    (const char**)lineweightselector_xpm,
    (const char**)lineweightsettings_xpm,
    (const char**)line_xpm,
    (const char**)list_xpm,
    (const char**)locatepoint_xpm,
    (const char**)locator_snaptoapparentintersection_xpm,
    (const char**)locator_snaptocenter_xpm,
    (const char**)locator_snaptoendpoint_xpm,
    (const char**)locator_snaptoextension_xpm,
    (const char**)locator_snaptoinsert_xpm,
    (const char**)locator_snaptointersection_xpm,
    (const char**)locator_snaptomidpoint_xpm,
    (const char**)locator_snaptonearest_xpm,
    (const char**)locator_snaptonode_xpm,
    (const char**)locator_snaptoparallel_xpm,
    (const char**)locator_snaptoperpendicular_xpm,
    (const char**)locator_snaptoquadrant_xpm,
    (const char**)locator_snaptotangent_xpm,
    (const char**)lockalllayers_xpm,
    (const char**)makeblock_xpm,
    (const char**)makelayercurrent_xpm,
    (const char**)mass_xpm,
    (const char**)mirror_xpm,
    (const char**)move_xpm,
    (const char**)multilinetext_xpm,
    (const char**)multiline_xpm,
    (const char**)namedviews_xpm,
    (const char**)neisometricview_xpm,
    (const char**)new_xpm,
    (const char**)night_xpm,
    (const char**)nopreview_xpm,
    (const char**)nwisometricview_xpm,
    (const char**)obliquedimensions_xpm,
    (const char**)offset_xpm,
    (const char**)open_xpm,
    (const char**)ordinatedimension_xpm,
    (const char**)orthosettings_xpm,
    (const char**)pandown_xpm,
    (const char**)panleft_xpm,
    (const char**)panpoint_xpm,
    (const char**)panrealtime_xpm,
    (const char**)panright_xpm,
    (const char**)panup_xpm,
    (const char**)pan_xpm,
    (const char**)paste_xpm,
    (const char**)path_xpm,
    (const char**)pickadd_xpm,
    (const char**)picknew_xpm,
    (const char**)plugin_xpm,
    (const char**)pointdivide_xpm,
    (const char**)pointmeasure_xpm,
    (const char**)pointmultiple_xpm,
    (const char**)pointsingle_xpm,
    (const char**)point_xpm,
    (const char**)polarsettings_xpm,
    (const char**)polygon_xpm,
    (const char**)polyline_xpm,
    (const char**)print_xpm,
    (const char**)pyscript_xpm,
    (const char**)qsnapsettings_xpm,
    (const char**)qtracksettings_xpm,
    (const char**)quickdimension_xpm,
    (const char**)quickleader_xpm,
    (const char**)quickselect_xpm,
    (const char**)radiusdimension_xpm,
    (const char**)ray_xpm,
    (const char**)rectangle_xpm,
    (const char**)redo_xpm,
    (const char**)region_xpm,
    (const char**)render_xpm,
    (const char**)rgb_xpm,
    (const char**)rightview_xpm,
    (const char**)rotate_xpm,
    (const char**)rulersettings_xpm,
    (const char**)sandbox_xpm,
    (const char**)satin_xpm,
    (const char**)saveas_xpm,
    (const char**)save_xpm,
    (const char**)scale_xpm,
    (const char**)seisometricview_xpm,
    (const char**)settingsdialog_2_xpm,
    (const char**)settingsdialog_xpm,
    (const char**)shade2dwireframe_xpm,
    (const char**)shade3dwireframe_xpm,
    (const char**)shadeflatedges_xpm,
    (const char**)shadeflat_xpm,
    (const char**)shadehidden_xpm,
    (const char**)shadesmoothedges_xpm,
    (const char**)shadesmooth_xpm,
    (const char**)shade_xpm,
    (const char**)showalllayers_xpm,
    (const char**)singlelinetext_xpm,
    (const char**)sketch_2_xpm,
    (const char**)sketch_xpm,
    (const char**)snapfrom_xpm,
    (const char**)snaptoapparentintersection_xpm,
    (const char**)snaptocenter_xpm,
    (const char**)snaptoendpoint_xpm,
    (const char**)snaptoextension_xpm,
    (const char**)snaptoinsert_xpm,
    (const char**)snaptointersection_xpm,
    (const char**)snaptomidpoint_xpm,
    (const char**)snaptonearest_xpm,
    (const char**)snaptonode_xpm,
    (const char**)snaptonone_xpm,
    (const char**)snaptoparallel_xpm,
    (const char**)snaptoperpendicular_xpm,
    (const char**)snaptoquadrant_xpm,
    (const char**)snaptotangent_xpm,
    (const char**)snowflake_2_xpm,
    (const char**)snowflake_xpm,
    (const char**)solidbox_xpm,
    (const char**)solidcheck_xpm,
    (const char**)solidclean_xpm,
    (const char**)solidcoloredges_xpm,
    (const char**)solidcolorfaces_xpm,
    (const char**)solidcone_xpm,
    (const char**)solidcopyedges_xpm,
    (const char**)solidcopyfaces_xpm,
    (const char**)solidcylinder_xpm,
    (const char**)soliddeletefaces_xpm,
    (const char**)solidextrudefaces_xpm,
    (const char**)solidextrude_xpm,
    (const char**)solidimprint_xpm,
    (const char**)solidinterfere_xpm,
    (const char**)solidintersect_xpm,
    (const char**)solidmovefaces_xpm,
    (const char**)solidoffsetfaces_xpm,
    (const char**)solidrevolve_xpm,
    (const char**)solidrotatefaces_xpm,
    (const char**)solidsection_xpm,
    (const char**)solidsediting_xpm,
    (const char**)solidseparate_xpm,
    (const char**)solidsetupdrawing_xpm,
    (const char**)solidsetupprofile_xpm,
    (const char**)solidsetupview_xpm,
    (const char**)solidsetup_xpm,
    (const char**)solidshell_xpm,
    (const char**)solidslice_xpm,
    (const char**)solidsphere_xpm,
    (const char**)solidsubtract_xpm,
    (const char**)solids_xpm,
    (const char**)solidtaperfaces_xpm,
    (const char**)solidtorus_xpm,
    (const char**)solidunion_xpm,
    (const char**)solidwedge_xpm,
    (const char**)spline_xpm,
    (const char**)star_xpm,
    (const char**)stretch_xpm,
    (const char**)stub_xpm,
    (const char**)surface2dsolid_xpm,
    (const char**)surface3dface_xpm,
    (const char**)surface3dmesh_xpm,
    (const char**)surfacebox_xpm,
    (const char**)surfacecone_xpm,
    (const char**)surfacecylinder_xpm,
    (const char**)surfacedish_xpm,
    (const char**)surfacedome_xpm,
    (const char**)surfaceedgesurface_xpm,
    (const char**)surfaceedge_xpm,
    (const char**)surfacepyramid_xpm,
    (const char**)surfacerevolvedsurface_xpm,
    (const char**)surfaceruledsurface_xpm,
    (const char**)surfacesphere_xpm,
    (const char**)surfaces_xpm,
    (const char**)surfacetabulatedsurface_xpm,
    (const char**)surfacetorus_xpm,
    (const char**)surfacewedge_xpm,
    (const char**)swisometricview_xpm,
    (const char**)temptrackingpoint_xpm,
    (const char**)textbold_xpm,
    (const char**)textitalic_xpm,
    (const char**)textoverline_xpm,
    (const char**)textstrikeout_xpm,
    (const char**)textunderline_xpm,
    (const char**)text_xpm,
    (const char**)thawalllayers_xpm,
    (const char**)theme_xpm,
    (const char**)tipoftheday_2_xpm,
    (const char**)tipoftheday_xpm,
    (const char**)tolerance_xpm,
    (const char**)topview_xpm,
    (const char**)trim_xpm,
    (const char**)undo_xpm,
    (const char**)units_xpm,
    (const char**)unlockalllayers_xpm,
    (const char**)view_xpm,
    (const char**)whatsthis_xpm,
    (const char**)wideflange_xpm,
    (const char**)windowcascade_xpm,
    (const char**)windowcloseall_xpm,
    (const char**)windowclose_xpm,
    (const char**)windownext_xpm,
    (const char**)windowprevious_xpm,
    (const char**)windowtile_xpm,
    (const char**)world_xpm,
    (const char**)zoomall_xpm,
    (const char**)zoomcenter_xpm,
    (const char**)zoomdynamic_xpm,
    (const char**)zoomextents_xpm,
    (const char**)zoomin_xpm,
    (const char**)zoomout_xpm,
    (const char**)zoomprevious_xpm,
    (const char**)zoomrealtime_xpm,
    (const char**)zoomscale_xpm,
    (const char**)zoomselected_xpm,
    (const char**)zoomwindow_xpm,
    (const char**)zoom_xpm
};

int file_toolbar[] = {
    ACTION_new,
    ACTION_open,
    ACTION_save,
    ACTION_saveas,
    ACTION_print,
    ACTION_designdetails,
    -1,
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_help,
    -2
};

int edit_toolbar[] = {
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
};

int view_toolbar[] = {
    ACTION_day,
    ACTION_night,
    -2
};

int pan_toolbar[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
};

int icon_toolbar[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
};

int help_toolbar[] = {
    ACTION_help,
    -1,
    ACTION_changelog,
    -1,
    ACTION_about,
    -1,
    ACTION_whatsthis,
    -2
};

int zoom_toolbar[] = {
    ACTION_zoomwindow,
    ACTION_zoomdynamic,
    ACTION_zoomscale,
    -1,
    ACTION_zoomcenter,
    ACTION_zoomin,
    ACTION_zoomout,
    -1,
    ACTION_zoomselected,
    ACTION_zoomall,
    ACTION_zoomextents,
    -2
};

int layer_toolbar[] = {
    -2
};

int text_toolbar[] = {
    -2
};

int properties_toolbar[] = {
    -2
};

int *toolbars[] = {
    file_toolbar,
    edit_toolbar,
    view_toolbar,
    zoom_toolbar,
    pan_toolbar,
    icon_toolbar,
    help_toolbar,
    layer_toolbar,
    text_toolbar,
    properties_toolbar
};


int file_menu[] = {
    ACTION_new,
    ACTION_open,
    ACTION_save,
    ACTION_saveas,
    ACTION_print,
    ACTION_designdetails,
    -1,
    ACTION_help,
    -1,
    ACTION_exit,
    -2
};

int edit_menu[] = {
    ACTION_undo,
    ACTION_redo,
    -1,
    ACTION_cut,
    ACTION_copy,
    ACTION_paste,
    -2
};

int view_menu[] = {
    ACTION_day,
    ACTION_night,
    -2
};

int pan_menu[] = {
    ACTION_panrealtime,
    ACTION_panpoint,
    -1,
    ACTION_panleft,
    ACTION_panright,
    ACTION_panup,
    ACTION_pandown,
    -2
};

int icon_menu[] = {
    ACTION_icon16,
    ACTION_icon24,
    ACTION_icon32,
    ACTION_icon48,
    ACTION_icon64,
    ACTION_icon128,
    -2
};

int help_menu[] = {
    ACTION_help,
    -1,
    ACTION_changelog,
    -1,
    ACTION_tipoftheday,
    -1,
    ACTION_about,
    -1,
    ACTION_whatsthis,
    -2
};

int zoom_menu[] = {
    ACTION_zoomwindow,
    ACTION_zoomdynamic,
    ACTION_zoomscale,
    -1,
    ACTION_zoomcenter,
    ACTION_zoomin,
    ACTION_zoomout,
    -1,
    ACTION_zoomselected,
    ACTION_zoomall,
    ACTION_zoomextents,
    -2
};

int settings_menu[] = {
    ACTION_settingsdialog,
    -1,
    -2
};

int recent_menu[] = {
    -1,
    -2
};

int window_menu[] = {
    -1,
    -2
};

int *menus[] = {
    file_menu,
    edit_menu,
    view_menu,
    settings_menu,
    window_menu,
    help_menu,
    recent_menu,
    zoom_menu,
    pan_menu
};

const char *toolbar_label[] = {
    "File",
    "Edit",
    "View",
    "Zoom",
    "Pan",
    "Icon",
    "Help",
    "Layer",
    "Text",
    "Properties"
};

const char *menu_label[] = {
    "&File",
    "&Edit",
    "&View",
    "&Settings",
    "&Window",
    "&Help",
    "Open &Recent",
    "&Zoom",
    "&Pan"
};

const char *status_bar_label[] = {
    "SNAP",
    "GRID",
    "RULER",
    "ORTHO",
    "POLAR",
    "QSNAP",
    "QTRACK",
    "LWT"
};

const char *folders[] = {
    "",
    "commands",
    "help",
    "icons",
    "images",
    "samples",
    "translations"
};

const char *settings_tab_label[] = {
    "General",
    "Files/Path",
    "Display",
    "Open/Save",
    "Printing",
    "Snap",
    "Grid/Ruler",
    "Ortho/Polar",
    "QuickSnap",
    "QuickTrack",
    "LineWeight",
    "Selection"
};

float symbol_scale = 0.01;

/* Symbols use the SVG path syntax.
 *
 * In theory, we could combine the icons and symbols systems,
 * since they could be rendered once and stored as icons in Qt.
 * (Or as textures in FreeGLUT.)
 *
 * Also we want to render the patterns themselves using SVG
 * syntax, so it would save on repeated work overall.
 */
const char *symbol_list[] = {
    /* 0 */ "icon 0",
    /* 1 */ "M 5 100 L 45 100 M 0 25 L 25 0 L 25 100",
    /* 2 */ "icon 2",
    /* 3 */ "icon 3",
    /* 4 */ "M 50 100 L 50 0 L 0 50 L 50 50",
    /* 5 */ "icon 5",
    /* 6 */ "icon 6",
    /* 7 */ "M 0 0 L 50 0 L 25 75 L 25 100",
    /* 8 */ "icon 8",
    /* 9 */ "icon 9",
    /* - */ "M 0 50 L 50 50",
    /* ' */ "M 25 100 L 25 25",
    /* " */ "M 10 0 L 10 25 M 40 0 L 40 25"
};

#if 0
path_symbol icon_zero[] = {
    /* path.addEllipse(QPointF(x+0.25*xScale, y-0.50*yScale), 0.25*xScale, 0.50*yScale);*/
    M 0 -0.75
    L 0 -0.25
    A 0 -0.5 0.5 0.5 180.0 180.0
    L 0.5, -0.75
    A 0 -1.0, 0.5, 0.5, 0.0, 180.0
};

path_symbol icon_two[] = {
    {PATHS_MOVETO, 0 -0.75
    A {0.45, 1.00, 0.50, 180.00, -216.87
    L 0 0.0
    L {0.50, 0.0
};

path_symbol icon_three[] = {
    {PATHS_ARCMOVETO, 0 -0.50, 0.50, 0.50, 195.00
    A 0 -0.50, 0.50, 195.00, 255.00
    A 0 -0.50, 0.50, 270.00, 255.00
};

path_symbol icon_five[] = {
    M 50 0 L 0 0 L 0 50 L 25 50 A 0.0, -0.5 0.5 0.5 90.0 -180.0 L 0 0
};

path_symbol icon_six[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
    M 0 75 L 0 25
    path.arcTo(x+0.00*xScale, y-1.00*yScale, 0.50*xScale, 0.50*yScale, 180.00, -140.00);
};

path_symbol icon_eight[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.25*yScale), 0.25*xScale, 0.25*yScale);
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
};

path_symbol icon_nine[] = {
    path.addEllipse(QPointF(x+0.25*xScale, y-0.75*yScale), 0.25*xScale, 0.25*yScale);
    M 0.50*xScale, y-0.75*yScale);
    L x+0.50*xScale, y-0.25*yScale);
    path.arcTo(x+0.00*xScale, y-0.50*yScale, 0.50*xScale, 0.50*yScale, 0.00, -140.00);
};

#endif

action action_list[] = {
    {
        /* 0 */
        OBJ_TYPE_NULL,
        icon_donothing,
        "donothing",
        "&Do Nothing",
        "Does nothing.",
        "\\0",
        doNothing
    },
    {
        /* 1 */
        OBJ_TYPE_NULL,
        icon_new,
        "new",
        "&New",
        "Create a new file.",
        "Ctrl+N",
        newFile
    },
    {
        /* 2 */
        OBJ_TYPE_NULL,
        icon_open,
        "open",
        "&Open",
        "Open an existing file.",
        "Ctrl+O",
        openFile
    },
    {
        /* 3 */
        OBJ_TYPE_NULL,
        icon_save,
        "save",
        "&Save",
        "Save the design to disk.",
        "Ctrl+S",
        saveFile
    },
    {
        /* 4 */
        OBJ_TYPE_NULL,
        icon_saveas,
        "saveas",
        "Save &As",
        "Save the design under a new name.",
        "Ctrl+Shift+S",
        saveAsFile
    },
    {
        /* 5 */
        OBJ_TYPE_NULL,
        icon_print,
        "print",
        "&Print",
        "Print the design.",
        "Ctrl+P",
        main_print
    },
    {
        /* 6 */
        OBJ_TYPE_NULL,
        icon_designdetails,
        "designdetails",
        "&Details",
        "Details of the current design.",
        "Ctrl+D",
        designDetails
    },
    {
        /* 7 */
        OBJ_TYPE_NULL,
        icon_exit,
        "exit",
        "E&xit",
        "Exit the application.",
        "Ctrl+Q",
        main_exit
    },
    {
        /* 8 */
        OBJ_TYPE_NULL,
        icon_cut,
        "cut",
        "Cu&t",
        "Cut the current selection's contents to the clipboard.",
        "Ctrl+X",
        main_cut
    },
    {
        /* 9 */
        OBJ_TYPE_NULL,
        icon_copy,
        "copy",
        "&Copy",
        "Copy the current selection's contents to the clipboard.",
        "Ctrl+C",
        main_copy
    },
    {
        /* 10 */
        OBJ_TYPE_NULL,
        icon_paste,
        "paste",
        "&Paste",
        "Paste the clipboard's contents into the current selection.",
        "Ctrl+V",
        main_paste
    },
    {
        /* 11 */
        OBJ_TYPE_NULL,
        icon_undo,
        "undo",
        "&Undo",
        "Reverses the most recent action.",
        "Ctrl+Z",
        main_undo
    },
    {
        /* 12 */
        OBJ_TYPE_NULL,
        icon_redo,
        "redo",
        "&Redo",
        "Reverses the effects of the previous undo action.",
        "Ctrl+Shift+Z",
        main_redo
    },
    {
        /* 13 */
        OBJ_TYPE_NULL,
        icon_windowclose,
        "windowclose",
        "Cl&ose",
        "Close the active window.",
        "\\0",
        windowClose
    },
    {
        /* 14 */
        OBJ_TYPE_NULL,
        icon_windowcloseall,
        "windowcloseall",
        "Close &All",
        "Close all the windows.",
        "\\0",
        windowCloseAll
    },
    {
        /* 15 */
        OBJ_TYPE_NULL,
        icon_windowcascade,
        "windowcascade",
        "&Cascade",
        "Cascade the windows.",
        "\\0",
        windowCascade
    },
    {
        /* 16 */
        OBJ_TYPE_NULL,
        icon_windowtile,
        "windowtile",
        "&Tile",
        "Tile the windows.",
        "\\0",
        windowTile
    },
    {
        OBJ_TYPE_NULL,
        icon_windownext,
        "windownext",
        "Ne&xt",
        "Move the focus to the next window.",
        "\\0",
        windowNext
    },
    {
        OBJ_TYPE_NULL,
        icon_windowprevious,
        "windowprevious",
        "Pre&vious",
        "Move the focus to the previous window.",
        "\\0",
        windowPrevious
    },
    {
        OBJ_TYPE_NULL,
        icon_help,
        "help",
        "&Help",
        "Displays help.",
        "F1",
        main_help
    },
    {
        OBJ_TYPE_NULL,
        icon_changelog,
        "changelog",
        "&Changelog",
        "Describes new features in this product.",
        "\\0",
        changelog
    },
    {
        OBJ_TYPE_NULL,
        icon_tipoftheday,
        "tipoftheday",
        "&Tip Of The Day",
        "Displays a dialog with useful tips",
        "\\0",
        tipOfTheDay
    },
    {
        OBJ_TYPE_NULL,
        icon_about,
        "about",
        "&About Embroidermodder 2",
        "Displays information about this product.",
        "F2",
        main_about
    },
    {
        OBJ_TYPE_NULL,
        icon_whatsthis,
        "whatsthis",
        "&What's This?",
        "What's This? Context Help!",
        "\\0",
        whatsthisContextHelp
    },
    {
        OBJ_TYPE_NULL,
        icon_icon16,
        "icon16",
        "Icon&16",
        "Sets the toolbar icon size to 16x16.",
        "\\0",
        icon16
    },
    {
        OBJ_TYPE_NULL,
        icon_icon24,
        "icon24",
        "Icon&24",
        "Sets the toolbar icon size to 24x24.",
        "\\0",
        icon24
    },
    {
        OBJ_TYPE_NULL,
        icon_icon32,
        "icon32",
        "Icon&32",
        "Sets the toolbar icon size to 32x32.",
        "\\0",
        icon32
    },
    {
        OBJ_TYPE_NULL,
        icon_icon48,
        "icon48",
        "Icon&48",
        "Sets the toolbar icon size to 48x48.",
        "\\0",
        icon48
    },
    {
        OBJ_TYPE_NULL,
        icon_icon64,
        "icon64",
        "Icon&64",
        "Sets the toolbar icon size to 64x64.",
        "\\0",
        icon64
    },
    {
        OBJ_TYPE_NULL,
        icon_icon128,
        "icon128",
        "Icon12&8",
        "Sets the toolbar icon size to 128x128.",
        "\\0",
        icon128
    },
    {
        OBJ_TYPE_NULL,
        icon_settingsdialog,
        "settingsdialog",
        "&Settings",
        "Configure settings specific to this product.",
        "\\0",
        settingsDialog
    },
    {
        OBJ_TYPE_NULL,
       icon_makelayercurrent,
       "makelayercurrent",
       "&Make Layer Active",
       "Makes the layer of a selected object the active layer",
        "\\0",
        makeLayerCurrent
    },
    {
        OBJ_TYPE_NULL,
        icon_layers,
        "layers",
        "&Layers",
        "Manages layers and layer properties:  LAYER",
        "\\0",
        layerManager
    },
    {
        OBJ_TYPE_NULL,
        icon_layerselector,
        "layerselector",
        "&Layer Selector",
        "Dropdown selector for changing the current layer",
        "\\0",
        layerSelector
    },
    {
        OBJ_TYPE_NULL,
        icon_layerprevious,
        "layerprevious",
        "&Layer Previous",
        "Restores the previous layer settings:  LAYERP",
        "\\0",
        layerPrevious
    },
    {
        OBJ_TYPE_NULL,
        icon_colorselector,
        "colorselector",
        "&Color Selector",
        "Dropdown selector for changing the current thread color",
        "\\0",
        colorSelector
    },
    {
        OBJ_TYPE_NULL,
        icon_linetypeselector,
        "linetypeselector",
        "&Stitchtype Selector",
        "Dropdown selector for changing the current stitch type",
        "\\0",
        lineTypeSelector
    },
    {
        OBJ_TYPE_NULL,
        icon_lineweightselector,
        "lineweightselector",
        "&Threadweight Selector",
        "Dropdown selector for changing the current thread weight",
        "\\0",
        lineWeightSelector
    },
    {
        OBJ_TYPE_NULL,
        icon_hidealllayers,
        "hidealllayers",
        "&Hide All Layers",
        "Turns the visibility off for all layers in the current drawing:  HIDEALL",
        "\\0",
        hideAllLayers
    },
    {
        OBJ_TYPE_NULL,
        icon_showalllayers,
        "showalllayers",
        "&Show All Layers",
        "Turns the visibility on for all layers in the current drawing:  SHOWALL",
        "\\0",
        showAllLayers
    },
    {
        OBJ_TYPE_NULL,
        icon_freezealllayers,
        "freezealllayers",
        "&Freeze All Layers",
        "Freezes all layers in the current drawing:  FREEZEALL",
        "\\0",
        freezeAllLayers
    },
    {
        OBJ_TYPE_NULL,
        icon_thawalllayers,
        "thawalllayers",
        "&Thaw All Layers",
        "Thaws all layers in the current drawing:  THAWALL",
        "\\0",
        thawAllLayers
    },
    {
        OBJ_TYPE_NULL,
        icon_lockalllayers,
        "lockalllayers",
        "&Lock All Layers",
        "Locks all layers in the current drawing:  LOCKALL",
        "\\0",
        lockAllLayers
    },
    {
        OBJ_TYPE_NULL,
        icon_unlockalllayers,
        "unlockalllayers",
        "&Unlock All Layers",
        "Unlocks all layers in the current drawing:  UNLOCKALL",
        "\\0",
        unlockAllLayers
    },
    {
        OBJ_TYPE_NULL,
        icon_textbold,
        "textbold",
        "&Bold Text",
        "Sets text to be bold.",
        "\\0",
        textBold
    },
    {
        OBJ_TYPE_NULL,
        icon_textitalic,
        "textitalic",
        "&Italic Text",
        "Sets text to be italic.",
        "\\0",
        textItalic
    },
    {
        OBJ_TYPE_NULL,
        icon_textoverline,
        "textunderline",
        "&Underline Text",
        "Sets text to be underlined.",
        "\\0",
        textOverline
    },
    {
        OBJ_TYPE_NULL,
        icon_textstrikeout,
        "textstrikeout",
        "&StrikeOut Text",
        "Sets text to be striked out.",
        "\\0",
        textStrikeout
    },
    {
        OBJ_TYPE_NULL,
        icon_textoverline,
        "textoverline",
        "&Overline Text",
        "Sets text to be overlined.",
        "\\0",
        textOverline
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomrealtime,
        "zoomrealtime",
        "Zoom &Realtime",
        "Zooms to increase or decrease the apparent size of objects in the current viewport.",
        "\\0",
        zoomRealtime
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomprevious,
        "zoomprevious",
        "Zoom &Previous",
        "Zooms to display the previous view.",
        "\\0",
        zoomPrevious
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomwindow,
        "zoomwindow",
        "Zoom &Window",
        "Zooms to display an area specified by a rectangular window.",
        "\\0",
        zoomWindow
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomdynamic,
        "zoomdynamic",
        "Zoom &Dynamic",
        "Zooms to display the generated portion of the drawing.",
        "\\0",
        zoomDynamic
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomscale,
        "zoomscale",
        "Zoom &Scale",
        "Zooms the display using a specified scale factor.",
        "\\0",
        zoomScale
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomcenter,
        "zoomcenter",
        "Zoom &Center",
        "Zooms to display a view specified by a center point and magnification or height.",
        "\\0",
        zoomCenter
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomin,
        "zoomin",
        "Zoom &In",
        "Zooms to increase the apparent size of objects.",
        "\\0",
        zoomIn
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomout,
        "zoomout",
        "Zoom &Out",
        "Zooms to decrease the apparent size of objects.",
        "\\0",
        zoomOut
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomselected,
        "zoomselected",
        "Zoom Selec&ted",
        "Zooms to display the selected objects.",
        "\\0",
        zoomSelected
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomall,
        "zoomall",
        "Zoom &All",
        "Zooms to display the drawing extents or the grid limits.",
        "\\0",
        zoomAll
    },
    {
        OBJ_TYPE_NULL,
        icon_zoomextents,
        "zoomextents",
        "Zoom &Extents",
        "Zooms to display the drawing extents.",
        "\\0",
        zoomExtents
    },
    {
        OBJ_TYPE_NULL,
        icon_panrealtime,
        "panrealtime",
        "&Pan Realtime",
        "Moves the view in the current viewport.",
        "\\0",
        panrealtime
    },
    {
        OBJ_TYPE_NULL,
        icon_panpoint,
        "panpoint",
        "&Pan Point",
        "Moves the view by the specified distance.",
        "\\0",
        panpoint
    },
    {
        OBJ_TYPE_NULL,
        icon_panleft,
        "panleft",
        "&Pan Left",
        "Moves the view to the left.",
        "\\0",
        panLeft
    },
    {
        OBJ_TYPE_NULL,
        icon_panright,
        "panright",
        "&Pan Right",
        "Moves the view to the right.",
        "\\0",
        panRight
    },
    {
        OBJ_TYPE_NULL,
        icon_panup,
        "panup",
        "&Pan Up",
        "Moves the view up.",
        "\\0",
        panUp
    },
    {
        OBJ_TYPE_NULL,
        icon_pandown,
        "pandown",
        "&Pan Down",
        "Moves the view down.",
        "\\0",
        panDown
    },
    {
        OBJ_TYPE_NULL,
        icon_day,
        "day",
        "&Day",
        "Updates the current view using day vision settings.",
        "\\0",
        dayVision
    },
    {
        OBJ_TYPE_NULL,
        icon_night,
        "night",
        "&Night",
        "Updates the current view using night vision settings.",
        "\\0",
        nightVision
    },
    {
        OBJ_TYPE_NULL,
        icon_circle,
        "circle",
        "&Circle",
        "Creates a circle:  CIRCLE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_line,
        "line",
        "&Line",
        "Creates straight line segments:  LINE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_distance,
        "distance",
        "&Distance",
        "Measures the distance and angle between two points:  DIST",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_dolphin,
        "dolphin",
        "&Dolphin",
        "Creates a dolphin:  DOLPHIN",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_ellipse,
        "ellipse",
        "&Ellipse",
        "Creates a ellipse:  ELLIPSE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_erase,
        "delete",
        "D&elete",
        "Removes objects from a drawing:  DELETE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_heart,
        "heart",
        "&Heart",
        "Creates a heart:  HEART",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_locatepoint,
        "locatepoint",
        "&Locate Point",
        "Displays the coordinate values of a location:  ID",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_donothing,
        "trebleclef",
        "TrebleClef",
        "Creates a treble clef:  TREBLECLEF",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_path,
        "path",
        "&Path",
        "Creates a 2D path:  PATH",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_donothing,
        "platform",
        "&Platform",
        "List which platform is in use:  PLATFORM",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_point,
        "point",
        "&Point",
        "Creates multiple points:  POINT",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_polygon,
        "polygon",
        "Pol&ygon",
        "Creates a regular polygon:  POLYGON",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_polyline,
        "polyline",
        "&Polyline",
        "Creates a 2D polyline:  PLINE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_quickleader,
        "quickleader",
        "&QuickLeader",
        "Creates a leader and annotation:  QUICKLEADER",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_rectangle,
        "rectangle",
        "&Rectangle",
        "Creates a rectangular polyline: RECTANGLE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_rgb,
        "rgb",
        "&RGB",
        "Updates the current view colors:  RGB",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_move,
        "move",
        "&Move",
        "Displaces objects a specified distance in a specified direction: MOVE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_rotate,
        "rotate",
        "&Rotate",
        "Rotates objects about a base point:  ROTATE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_sandbox,
        "sandbox",
        "Sandbox",
        "A sandbox to play in:  SANDBOX",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_scale,
        "scale",
        "Sca&le",
        "Enlarges or reduces objects proportionally in the X, Y, and Z directions:  SCALE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_donothing,
        "selectall",
        "&Select All",
        "Selects all objects:  SELECTALL",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_singlelinetext,
        "singlelinetext",
        "&Single Line Text",
        "Creates single-line text objects:  TEXT",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_snowflake,
        "snowflake",
        "&Snowflake",
        "Creates a snowflake:  SNOWFLAKE",
        "\\0",
        doNothing
    },
    {
        OBJ_TYPE_NULL,
        icon_star,
        "star",
        "&Star",
        "Creates a star:  STAR",
        "\\0",
        doNothing
    },
    {
        /* end symbol */
        OBJ_TYPE_NULL,
        icon_donothing,
        "\\0",
        "\\0",
        "\\0",
        "\\0",
        doNothing
    }
};

/* New for toolbars: modify and draw. Inquiry toolbar?
 *
 * TODO: associate the property editor with the function callbacks using
 * a function pointer.
 */

/* property_editor_row property_editors[] = { */
/*
QGroupBox* PropertyEditor::createGroupBoxGeometryCircle()
{
    groupBoxGeometryCircle = new QGroupBox(tr("Geometry"), this);

    toolButtonCircleCenterX = createToolButton("blank", tr("Center X"));
    toolButtonCircleCenterY = createToolButton("blank", tr("Center Y"));
    toolButtonCircleRadius = createToolButton("blank", tr("Radius"));
    toolButtonCircleDiameter = createToolButton("blank", tr("Diameter"));
    toolButtonCircleArea = createToolButton("blank", tr("Area"));
    toolButtonCircleCircumference = createToolButton("blank", tr("Circumference"));

    lineEditCircleCenterX = createLineEdit("double", 0);
    lineEditCircleCenterY = createLineEdit("double", 0);
    lineEditCircleRadius = createLineEdit("double", 0);
    lineEditCircleDiameter = createLineEdit("double", 0);
    lineEditCircleArea = createLineEdit("double", 0);
    lineEditCircleCircumference = createLineEdit("double", 0);

    mapSignal(lineEditCircleCenterX, "lineEditCircleCenterX", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleCenterY, "lineEditCircleCenterY", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleRadius, "lineEditCircleRadius", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleDiameter, "lineEditCircleDiameter", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleArea, "lineEditCircleArea", OBJ_TYPE_CIRCLE);
    mapSignal(lineEditCircleCircumference, "lineEditCircleCircumference", OBJ_TYPE_CIRCLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonCircleCenterX, lineEditCircleCenterX);
    formLayout->addRow(toolButtonCircleCenterY, lineEditCircleCenterY);
    formLayout->addRow(toolButtonCircleRadius, lineEditCircleRadius);
    formLayout->addRow(toolButtonCircleDiameter, lineEditCircleDiameter);
    formLayout->addRow(toolButtonCircleArea, lineEditCircleArea);
    formLayout->addRow(toolButtonCircleCircumference, lineEditCircleCircumference);
    groupBoxGeometryCircle->setLayout(formLayout);

    return groupBoxGeometryCircle;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryImage()
{
    groupBoxGeometryImage = new QGroupBox(tr("Geometry"), this);

    toolButtonImageX = createToolButton("blank", tr("Position X"));
    toolButtonImageY = createToolButton("blank", tr("Position Y"));
    toolButtonImageWidth = createToolButton("blank", tr("Width"));
    toolButtonImageHeight = createToolButton("blank", tr("Height"));

    lineEditImageX = createLineEdit("double", 0);
    lineEditImageY = createLineEdit("double", 0);
    lineEditImageWidth = createLineEdit("double", 0);
    lineEditImageHeight = createLineEdit("double", 0);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonImageX, lineEditImageX);
    formLayout->addRow(toolButtonImageY, lineEditImageY);
    formLayout->addRow(toolButtonImageWidth, lineEditImageWidth);
    formLayout->addRow(toolButtonImageHeight, lineEditImageHeight);
    groupBoxGeometryImage->setLayout(formLayout);

    return groupBoxGeometryImage;
}

QGroupBox* PropertyEditor::createGroupBoxMiscImage()
{
    groupBoxMiscImage = new QGroupBox(tr("Misc"), this);

    toolButtonImageName = createToolButton("blank", tr("Name"));
    toolButtonImagePath = createToolButton("blank", tr("Path"));

    lineEditImageName = createLineEdit("double", 1);
    lineEditImagePath = createLineEdit("double", 1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonImageName, lineEditImageName);
    formLayout->addRow(toolButtonImagePath, lineEditImagePath);
    groupBoxMiscImage->setLayout(formLayout);

    return groupBoxMiscImage;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryInfiniteLine()
{
    groupBoxGeometryInfiniteLine = new QGroupBox(tr("Geometry"), this);

    toolButtonInfiniteLineX1 = createToolButton("blank", tr("Start X"));
    toolButtonInfiniteLineY1 = createToolButton("blank", tr("Start Y"));
    toolButtonInfiniteLineX2 = createToolButton("blank", tr("2nd X"));
    toolButtonInfiniteLineY2 = createToolButton("blank", tr("2nd Y"));
    toolButtonInfiniteLineVectorX = createToolButton("blank", tr("Vector X"));
    toolButtonInfiniteLineVectorY = createToolButton("blank", tr("Vector Y"));

    lineEditInfiniteLineX1 = createLineEdit("double", 0);
    lineEditInfiniteLineY1 = createLineEdit("double", 0);
    lineEditInfiniteLineX2 = createLineEdit("double", 0);
    lineEditInfiniteLineY2 = createLineEdit("double", 0);
    lineEditInfiniteLineVectorX = createLineEdit("double", 1);
    lineEditInfiniteLineVectorY = createLineEdit("double", 1);

    //TODO: mapSignal for infinite lines

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonInfiniteLineX1, lineEditInfiniteLineX1);
    formLayout->addRow(toolButtonInfiniteLineY1, lineEditInfiniteLineY1);
    formLayout->addRow(toolButtonInfiniteLineX2, lineEditInfiniteLineX2);
    formLayout->addRow(toolButtonInfiniteLineY2, lineEditInfiniteLineY2);
    formLayout->addRow(toolButtonInfiniteLineVectorX, lineEditInfiniteLineVectorX);
    formLayout->addRow(toolButtonInfiniteLineVectorY, lineEditInfiniteLineVectorY);
    groupBoxGeometryInfiniteLine->setLayout(formLayout);

    return groupBoxGeometryInfiniteLine;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryLine()
{
    groupBoxGeometryLine = new QGroupBox(tr("Geometry"), this);

    toolButtonLineStartX = createToolButton("blank", tr("Start X"));
    toolButtonLineStartY = createToolButton("blank", tr("Start Y"));
    toolButtonLineEndX = createToolButton("blank", tr("End X"));
    toolButtonLineEndY = createToolButton("blank", tr("End Y"));
    toolButtonLineDeltaX = createToolButton("blank", tr("Delta X"));
    toolButtonLineDeltaY = createToolButton("blank", tr("Delta Y"));
    toolButtonLineAngle = createToolButton("blank", tr("Angle"));
    toolButtonLineLength = createToolButton("blank", tr("Length"));

    lineEditLineStartX = createLineEdit("double", 0);
    lineEditLineStartY = createLineEdit("double", 0);
    lineEditLineEndX = createLineEdit("double", 0);
    lineEditLineEndY = createLineEdit("double", 0);
    lineEditLineDeltaX = createLineEdit("double", 1);
    lineEditLineDeltaY = createLineEdit("double", 1);
    lineEditLineAngle = createLineEdit("double", 1);
    lineEditLineLength = createLineEdit("double", 1);

    mapSignal(lineEditLineStartX, "lineEditLineStartX", OBJ_TYPE_LINE);
    mapSignal(lineEditLineStartY, "lineEditLineStartY", OBJ_TYPE_LINE);
    mapSignal(lineEditLineEndX, "lineEditLineEndX", OBJ_TYPE_LINE);
    mapSignal(lineEditLineEndY, "lineEditLineEndY", OBJ_TYPE_LINE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonLineStartX, lineEditLineStartX);
    formLayout->addRow(toolButtonLineStartY, lineEditLineStartY);
    formLayout->addRow(toolButtonLineEndX, lineEditLineEndX);
    formLayout->addRow(toolButtonLineEndY, lineEditLineEndY);
    formLayout->addRow(toolButtonLineDeltaX, lineEditLineDeltaX);
    formLayout->addRow(toolButtonLineDeltaY, lineEditLineDeltaY);
    formLayout->addRow(toolButtonLineAngle, lineEditLineAngle);
    formLayout->addRow(toolButtonLineLength, lineEditLineLength);
    groupBoxGeometryLine->setLayout(formLayout);

    return groupBoxGeometryLine;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryPath()
{
    groupBoxGeometryPath = new QGroupBox(tr("Geometry"), this);

    toolButtonPathVertexNum = createToolButton("blank", tr("Vertex #"));
    toolButtonPathVertexX = createToolButton("blank", tr("Vertex X"));
    toolButtonPathVertexY = createToolButton("blank", tr("Vertex Y"));
    toolButtonPathArea = createToolButton("blank", tr("Area"));
    toolButtonPathLength = createToolButton("blank", tr("Length"));

    comboBoxPathVertexNum = createComboBox(0);
    lineEditPathVertexX = createLineEdit("double", 0);
    lineEditPathVertexY = createLineEdit("double", 0);
    lineEditPathArea = createLineEdit("double", 1);
    lineEditPathLength = createLineEdit("double", 1);

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPathVertexNum, comboBoxPathVertexNum);
    formLayout->addRow(toolButtonPathVertexX, lineEditPathVertexX);
    formLayout->addRow(toolButtonPathVertexY, lineEditPathVertexY);
    formLayout->addRow(toolButtonPathArea, lineEditPathArea);
    formLayout->addRow(toolButtonPathLength, lineEditPathLength);
    groupBoxGeometryPath->setLayout(formLayout);

    return groupBoxGeometryPath;
}

QGroupBox* PropertyEditor::createGroupBoxMiscPath()
{
    groupBoxMiscPath = new QGroupBox(tr("Misc"), this);

    toolButtonPathClosed = createToolButton("blank", tr("Closed"));

    comboBoxPathClosed = createComboBox(0);

    //TODO: mapSignal for paths

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPathClosed, comboBoxPathClosed);
    groupBoxMiscPath->setLayout(formLayout);

    return groupBoxMiscPath;
}


QGroupBox* PropertyEditor::createGroupBoxGeometryPolygon()
{
    groupBoxGeometryPolygon = new QGroupBox(tr("Geometry"), this);

    {
        OBJ_TYPE_POLYGON, POLYGON_CENTER_X,
        0, "blank", "Center X", LINE_EDIT_MODE, "lineEditPolygonCenterX"
    },
    {
        OBJ_TYPE_POLYGON, POLYGON_CENTER_Y,
        0, "blank", "Center Y", LINE_EDIT_MODE, "lineEditPolygonCenterY"
    },
    {
        OBJ_TYPE_POLYGON, POLYGON_VERTEX_RADIUS,
        0, "blank", "Vertex Radius", LINE_EDIT_MODE, "lineEditPolygonVertexRadius"
    }

    toolButtonPolygonRadiusSide = createToolButton("blank", tr("Side Radius"));
    toolButtonPolygonDiameterVertex = createToolButton("blank", tr("Vertex Diameter"));
    toolButtonPolygonDiameterSide = createToolButton("blank", tr("Side Diameter"));
    toolButtonPolygonInteriorAngle = createToolButton("blank", tr("Interior Angle"));

    lineEditPolygonRadiusSide = createLineEdit("double", 0);
    lineEditPolygonDiameterVertex = createLineEdit("double", 0);
    lineEditPolygonDiameterSide = createLineEdit("double", 0);
    lineEditPolygonInteriorAngle = createLineEdit("double", 1);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonPolygonRadiusSide, lineEditPolygonRadiusSide);
    formLayout->addRow(toolButtonPolygonDiameterVertex, lineEditPolygonDiameterVertex);
    formLayout->addRow(toolButtonPolygonDiameterSide, lineEditPolygonDiameterSide);
    formLayout->addRow(toolButtonPolygonInteriorAngle, lineEditPolygonInteriorAngle);
    groupBoxGeometryPolygon->setLayout(formLayout);

    return groupBoxGeometryPolygon;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryPolyline()
{
    groupBoxGeometryPolyline = new QGroupBox(tr("Geometry"), this);

    toolButtonPolylineVertexNum = createToolButton("blank", tr("Vertex #"));
    toolButtonPolylineVertexX = createToolButton("blank", tr("Vertex X"));
    toolButtonPolylineVertexY = createToolButton("blank", tr("Vertex Y"));
    toolButtonPolylineArea = createToolButton("blank", tr("Area"));
    toolButtonPolylineLength = createToolButton("blank", tr("Length"));

    comboBoxPolylineVertexNum = createComboBox(0);
    lineEditPolylineVertexX = createLineEdit("double", 0);
    lineEditPolylineVertexY = createLineEdit("double", 0);
    lineEditPolylineArea = createLineEdit("double", 1);
    lineEditPolylineLength = createLineEdit("double", 1);

    //TODO: mapSignal for polylines

    QFormLayout* formLayout = new QFormLayout(this);
    "comboBoxPolylineVertexNum"
    "lineEditPolylineVertexX"
    "lineEditPolylineVertexY"
    "lineEditPolylineArea"
    "lineEditPolylineLength"
    groupBoxGeometryPolyline->setLayout(formLayout);

    return groupBoxGeometryPolyline;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryRay()
{
    toolButtonRayX2 = createToolButton();
    toolButtonRayY2 = createToolButton("blank", tr("2nd Y"));
    toolButtonRayVectorX = createToolButton("blank", tr("Vector X"));
    toolButtonRayVectorY = createToolButton("blank", tr("Vector Y"));

    "blank", "Start X", 0, "lineEditRayX1"
    "blank", "Start Y", 0, "lineEditRayY1"
    "blank", "2nd X", 0, "lineEditRayX2"
    "blank", "2nd Y", 0, "lineEditRayY2"
    "blank", "Vector X", 1, "lineEditRayVectorX"
    1, "lineEditRayVectorY"
}

QGroupBox* PropertyEditor::createGroupBoxGeometryTextMulti()
{
    groupBoxGeometryTextMulti = new QGroupBox(tr("Geometry"), this);

    toolButtonTextMultiX = createToolButton("blank", tr("Position X"));
    toolButtonTextMultiY = createToolButton("blank", tr("Position Y"));

    lineEditTextMultiX = createLineEdit("double", 0);
    lineEditTextMultiY = createLineEdit("double", 0);


    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextMultiX, lineEditTextMultiX);
    formLayout->addRow(toolButtonTextMultiY, lineEditTextMultiY);
    groupBoxGeometryTextMulti->setLayout(formLayout);

    return groupBoxGeometryTextMulti;
}

QGroupBox* PropertyEditor::createGroupBoxTextTextSingle()
{
    groupBoxTextTextSingle = new QGroupBox(tr("Text"), this);

    {
        "blank",
        "Contents",
        "toolButtonTextSingleContents"
    },
    toolButtonTextSingleFont = createToolButton("blank", tr("Font"));
    toolButtonTextSingleJustify = createToolButton("blank", tr("Justify"));
    toolButtonTextSingleHeight = createToolButton("blank", tr("Height"));
    toolButtonTextSingleRotation = createToolButton("blank", tr("Rotation"));

    lineEditTextSingleContents = createLineEdit("string", 0);
    comboBoxTextSingleFont = createFontComboBox(0);
    comboBoxTextSingleJustify = createComboBox(0);
    lineEditTextSingleHeight = createLineEdit("double", 0);
    lineEditTextSingleRotation = createLineEdit("double", 0);

    mapSignal(lineEditTextSingleContents, "lineEditTextSingleContents", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleFont, "comboBoxTextSingleFont", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleJustify, "comboBoxTextSingleJustify", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleHeight, "lineEditTextSingleHeight", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleRotation, "lineEditTextSingleRotation", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleContents, lineEditTextSingleContents);
    formLayout->addRow(toolButtonTextSingleFont, comboBoxTextSingleFont);
    formLayout->addRow(toolButtonTextSingleJustify, comboBoxTextSingleJustify);
    formLayout->addRow(toolButtonTextSingleHeight, lineEditTextSingleHeight);
    formLayout->addRow(toolButtonTextSingleRotation, lineEditTextSingleRotation);
    groupBoxTextTextSingle->setLayout(formLayout);

    return groupBoxTextTextSingle;
}

QGroupBox* PropertyEditor::createGroupBoxGeometryTextSingle()
{
    groupBoxGeometryTextSingle = new QGroupBox(tr("Geometry"), this);

    toolButtonTextSingleX = createToolButton("blank", tr("Position X"));
    toolButtonTextSingleY = createToolButton("blank", tr("Position Y"));

    lineEditTextSingleX = createLineEdit("double", 0);
    lineEditTextSingleY = createLineEdit("double", 0);

    mapSignal(lineEditTextSingleX, "lineEditTextSingleX", OBJ_TYPE_TEXTSINGLE);
    mapSignal(lineEditTextSingleY, "lineEditTextSingleY", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleX, lineEditTextSingleX);
    formLayout->addRow(toolButtonTextSingleY, lineEditTextSingleY);
    groupBoxGeometryTextSingle->setLayout(formLayout);

    return groupBoxGeometryTextSingle;
}

QGroupBox* PropertyEditor::createGroupBoxMiscTextSingle()
{
    groupBoxMiscTextSingle = new QGroupBox(tr("Misc"), this);

    toolButtonTextSingleBackward = createToolButton("blank", tr("Backward"));
    toolButtonTextSingleUpsideDown = createToolButton("blank", tr("UpsideDown"));

    comboBoxTextSingleBackward = createComboBox(0);
    comboBoxTextSingleUpsideDown = createComboBox(0);

    mapSignal(comboBoxTextSingleBackward, "comboBoxTextSingleBackward", OBJ_TYPE_TEXTSINGLE);
    mapSignal(comboBoxTextSingleUpsideDown, "comboBoxTextSingleUpsideDown", OBJ_TYPE_TEXTSINGLE);

    QFormLayout* formLayout = new QFormLayout(this);
    formLayout->addRow(toolButtonTextSingleBackward, comboBoxTextSingleBackward);
    formLayout->addRow(toolButtonTextSingleUpsideDown, comboBoxTextSingleUpsideDown);
    groupBoxMiscTextSingle->setLayout(formLayout);

    return groupBoxMiscTextSingle;
}

*/
#if 0
    {
        /* 0 */
        OBJ_TYPE_ARC, ARC_CENTER_X,
        0, "blank", "Center X", LINE_EDIT_DOUBLE, "lineEditArcCenterX"
    },
    {
        /* 1 */
        OBJ_TYPE_ARC, ARC_CENTER_Y,
        0, "blank", "Center Y", LINE_EDIT_DOUBLE, "lineEditArcCenterY"
    },
    {
        /* 2 */
        OBJ_TYPE_ARC, ARC_RADIUS,
        0, "blank", "Radius", LINE_EDIT_DOUBLE, "lineEditArcRadius"
    },
    {
        /* 3 */
        OBJ_TYPE_ARC, ARC_START_ANGLE,
        0, "blank", "Start Angle", LINE_EDIT_DOUBLE, "lineEditArcStartAngle"
    },
    {
        /* 4 */
        OBJ_TYPE_ARC, ARC_END_ANGLE,
        0, "blank", "End Angle", LINE_EDIT_DOUBLE, "lineEditArcEndAngle"
    },
    {
        /* 5 */
        OBJ_TYPE_ARC, ARC_START_X,
        1, "blank", "Start X", LINE_EDIT_DOUBLE, "lineEditArcStartX"
    },
    {
        /* 6 */
        OBJ_TYPE_ARC, ARC_START_Y,
        1, "blank", "Start Y", LINE_EDIT_DOUBLE, "lineEditArcStartY"
    },
    {
        /* 7 */
        OBJ_TYPE_ARC, ARC_END_X,
        1, "blank", "End X", LINE_EDIT_DOUBLE, "lineEditArcEndX"
    },
    {
        /* 8 */
        OBJ_TYPE_ARC, ARC_END_Y,
        1, "blank", "End Y", LINE_EDIT_DOUBLE, "lineEditArcEndY"
    },
    {
        /* 9 */
        OBJ_TYPE_ARC, ARC_AREA,
        1, "blank", "Area", LINE_EDIT_DOUBLE, "lineEditArcArea"
    },
/*        ARC_LENGTH, 1, "blank", "ArcLength");
    create_lineedit_row(formLayout, ARC_CHORD, 1, "blank", "ArcChord");
    create_lineedit_row(formLayout, ARC_INC_ANGLE, 1, "blank", "ArcIncludedAngle");
    ARC_CLOCKWISE, "int", 1, "blank", "Clockwise", */
    {
        /* 9 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_CENTER_X,
        0, "blank", "Center X", LINE_EDIT_DOUBLE, "lineEditEllipseCenterX"
    },
    {
        /* 10 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_CENTER_Y,
        0, "blank", "Center Y", LINE_EDIT_DOUBLE, "lineEditEllipseCenterY"
    },
    {
        /* 11 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_RADIUS_MAJOR,
        0, "blank", "Radius Major", LINE_EDIT_DOUBLE, "lineEditEllipseRadiusMajor"
    },
    {
        /* 12 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_RADIUS_MINOR,
        0, "blank", "Radius Minor", LINE_EDIT_DOUBLE, "lineEditEllipseRadiusMinor"
    },
    {
        /* 13 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_DIAMETER_MAJOR,
        0, "blank", "Diameter Major", LINE_EDIT_DOUBLE, "lineEditEllipseDiameterMajor"
    },
    {
        /* 14 */
        OBJ_TYPE_ELLIPSE, ELLIPSE_DIAMETER_MINOR,
        0, "blank", "Diameter Minor", LINE_EDIT_DOUBLE, "lineEditEllipseDiameterMinor"
    },
    {
        /* 15 */
        OBJ_TYPE_BLOCK, BLOCK_X,
        0, "blank", "Position X", LINE_EDIT_DOUBLE, "lineEditBlockX"
    },
    {
        /* 16 */
        OBJ_TYPE_BLOCK, BLOCK_Y,
        0, "blank", "Position Y", LINE_EDIT_DOUBLE, "lineEditBlockY"
    },
    {
        /* 17 */
        OBJ_TYPE_POINT, POINT_X,
        0, "blank", "Position X", LINE_EDIT_DOUBLE, "lineEditPointX"
    },
    {
        /* 18 */
        OBJ_TYPE_POINT, POINT_Y,
        0, "blank", "Position Y", LINE_EDIT_DOUBLE, "lineEditPointY"
    },
    {
        /* 19 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X1,
        0, "blank", "Corner 1 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner1X"
    },
    {
        /* 20 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y1,
        0, "blank", "Corner 1 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner1Y"
    },
    {
        /* 21 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X2,
        0, "blank", "Corner 2 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner2X"
    },
    {
        /* 22 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y2,
        0, "blank", "Corner 2 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner2Y"
    },
    {
        /* 23 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X3,
        0, "blank", "Corner 3 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner3X"
    },
    {
        /* 24 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y3,
        0, "blank", "Corner 3 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner3Y"
    },
    {
        /* 25 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_X4,
        0, "blank", "Corner 4 X", LINE_EDIT_DOUBLE, "lineEditRectangleCorner4X"
    },
    {
        /* 26 */
        OBJ_TYPE_RECTANGLE, RECT_CORNER_Y4,
        0, "blank", "Corner 4 Y", LINE_EDIT_DOUBLE, "lineEditRectangleCorner4Y"
    },
    {
        /* 27 */
        OBJ_TYPE_RECTANGLE, RECT_WIDTH,
        0, "blank", "Width", LINE_EDIT_DOUBLE, "lineEditRectangleWidth"
    },
    {
        /* 28 */
        OBJ_TYPE_RECTANGLE, RECT_HEIGHT,
        0, "blank", "Height", LINE_EDIT_DOUBLE, "lineEditRectangleHeight"
    },
    {
        /* 29 */
        OBJ_TYPE_RECTANGLE, RECT_AREA,
        1, "blank", "Area", LINE_EDIT_DOUBLE, "lineEditRectangleArea"
    },
    {
        /* END */
        OBJ_TYPE_UNKNOWN, 0,
        "NULL", 0, "NULL", "NULL", 0, "NULL"
    }
};
#endif

"""
    for k in a.keys():
        s += a[k]["schema"]+k+"[] = {\n"
        for i in a[k]["data"]:
            s += "    \"%s\",\n" % i
        s += "};\n\n"
    return s


def process_c_code(s):
    r"""
    The jobs carried out by this processor are:
    
        * check indentation is always a multiple of 4
    """
    return s

    
def process_cplusplus_code(s):
    r"""
    The jobs carried out by this processor are:
    
        * check indentation is always a multiple of 4
    """
    return s


def process_header(s):
    r"""
    The jobs carried out by this processor are:
    
        * correct define blocks
        * report the number of functions that are within
          classes: to aid the de-object orientation process
    """
    return s


for fname in os.listdir("src"):
    if "." not in fname:
        continue
    if ".ico" in fname:
        continue
    if ".icns" in fname:
        continue
    print(fname)

    # configuration to code
    if fname[-5:] == ".json":
        f = open("src/"+fname, "r")
        s = f.read()
        f.close()
        a = json.loads(s)
        with open("src/"+fname, "w") as f:
            f.write(json.dumps(a, indent=4))
        with open("src/"+fname[:-5]+".c", "w") as f:
            f.write(process_json(a))
        continue

    # in place editing
    s = ""
    with open("src/"+fname, "r") as f:
        s = f.read()
    if fname[-2:] == ".c":
        s = process_c_code(s)
    if fname[-2:] == ".h":
        s = process_header(s)
    if fname[-4:] == ".cpp":
        s = process_cplusplus_code(s)
    with open("src/"+fname, "w") as f:
        f.write(s)


