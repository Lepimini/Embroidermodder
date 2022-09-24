/* 
 *  Embroidermodder 2.
 *
 *  ------------------------------------------------------------
 *
 *  Copyright 2013-2022 The Embroidermodder Team
 *  Embroidermodder 2 is Open Source Software.
 *  See LICENSE for licensing terms.
 *
 *  ------------------------------------------------------------
 *
 *  Strings that don't need to be easily editable.
 */

#include "em2.h"

Property circle_geometry_properties[] = {
    {"Circle", PERMISSIONS_SYSTEM, DATA_TYPE_TITLE},
    {"Geometry", PERMISSIONS_SYSTEM, DATA_TYPE_GROUP_BOX},
    {"Center X", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Center Y", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Radius", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Diameter", PERMISSIONS_SYSTEM, DATA_TYPE_DOUBLE},
    {"Area", PERMISSIONS_SYSTEM, DATA_TYPE_DOUBLE},
    {"Circumference", PERMISSIONS_SYSTEM, DATA_TYPE_DOUBLE},
    {"END", PERMISSIONS_SYSTEM, DATA_TYPE_END_MARKER}
};

Property ellipse_properties[] = {
    {"Ellipse", PERMISSIONS_SYSTEM, DATA_TYPE_TITLE},
    {"Geometry", PERMISSIONS_SYSTEM, DATA_TYPE_GROUP_BOX},
    {"Center X", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Center Y", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Radius Major", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Radius Minor", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Diameter Major", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Diameter Minor", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"END", PERMISSIONS_SYSTEM, DATA_TYPE_END_MARKER}
};

Property image_properties[] = {
    {"Image", PERMISSIONS_SYSTEM, DATA_TYPE_TITLE},
    {"Geometry", PERMISSIONS_SYSTEM, DATA_TYPE_GROUP_BOX},
    {"Position X", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Position Y", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Width", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Height", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Misc", PERMISSIONS_SYSTEM, DATA_TYPE_GROUP_BOX},
    {"Name", PERMISSIONS_USER, DATA_TYPE_STRING},
    {"Path", PERMISSIONS_USER, DATA_TYPE_STRING},
    {"END", PERMISSIONS_SYSTEM, DATA_TYPE_END_MARKER}
};

Property infinite_line_properties[] = {
    {"Infinite Line", PERMISSIONS_SYSTEM, DATA_TYPE_TITLE},
    {"Geometry", PERMISSIONS_SYSTEM, DATA_TYPE_GROUP_BOX},
    {"Position X1", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Position Y1", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Position X2", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Position Y2", PERMISSIONS_USER, DATA_TYPE_DOUBLE},
    {"Vector X", PERMISSIONS_SYSTEM, DATA_TYPE_DOUBLE},
    {"Vector Y", PERMISSIONS_SYSTEM, DATA_TYPE_DOUBLE},
    {"END", PERMISSIONS_SYSTEM, DATA_TYPE_END_MARKER}
};

/*
Arc
Geometry
Center X,double,user
Center Y,double,user
Radius,double,user
Start Angle,double,user
End Angle,double,user
Start X,double,system
Start Y,double,system
End X,double,system
End Y,double,system
Area,double,system
Length,double,system
Chord,double,system
Included Angle,double,system
END,END,END
*/

char *settings_tabs[MAX_STRING_LENGTH] = {
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
    "Selection",
    "END"
};

/* "Rect"
 * "GroupBox" "Geometry"
 */
char *geometry_rect_properties[MAX_STRING_LENGTH] = {
    "Corner X1,double,user",
    "Corner Y1,double,user",
    "Corner X2,double,user",
    "Corner Y2,double,user",
    "Corner X3,double,user",
    "Corner Y3,double,user",
    "Corner X4,double,user",
    "Corner Y4,double,user",
    "Height,double,user",
    "Width,double,user",
    "Area,double,system",
    "END"
};

char *arc_properties[MAX_STRING_LENGTH] = {
    "Center X,double,user",
    "Center Y,double,user",
    "Radius,double,user",
    "Start Angle,double,user",
    "End Angle,double,user",
    "Start X,double,system",
    "Start Y,double,system",
    "End X,double,system",
    "End Y,double,system",
    "Area,double,system",
    "Length,double,system",
    "Chord,double,system",
    "Included Angle,double,system",
    "END"
};

char *details_labels[MAX_STRING_LENGTH] = {
    "Total Stitches:",
    "Real Stitches:",
    "Jump Stitches:",
    "Trim Stitches:",
    "Total Colors:",
    "Color Changes:",
    "Left:",
    "Top:",
    "Right:",
    "Bottom:",
    "Width:",
    "Height:",
    "END"
};

char *statusbar_labels[MAX_STRING_LENGTH] = {
    "SNAP",
    "GRID",
    "RULER",
    "ORTHO",
    "POLAR",
    "QSNAP",
    "QTRACK",
    "LWT",
    "END"
};

