;
; Embroidermodder 2.
;
; ------------------------------------------------------------
;
; Copyright 2013-2022 The Embroidermodder Team
; Embroidermodder 2 is Open Source Software.
; See LICENSE for licensing terms.
;
; ------------------------------------------------------------
;
; Object Properties


(define (obj-names)
  (vector
    "Null"
    "Unknown"
    "Base"
    "Arc"
    "Block"
    "Circle"
    "Aligned Dimension"
    "Angular Dimension"
    "Arc Length Dimension"
    "Diameter Dimension"
    "Leader Dimension"
    "Linear Dimension"
    "Ordinate Dimension"
    "Radius Dimension"
    "Ellipse"
    "Elliptical Arc"
    "Rubber"
    "Grid"
    "Hatch"
    "Image"
    "Infinite Line"
    "Line"
    "Path"
    "Point"
    "Polygon"
    "Polyline"
    "Ray"
    "Rectangle"
    "Slot"
    "Spline"
    "Multi Line Text"
    "Single Line Text"
    "Unknown"
    "END"
  )
)

(define (text-single-properties)
  (vector
    "Text"
    "Text Single"
    "Contents" "string" "user"
    "Font" "dropdown" "user"
    "Justify" "dropdown" "user"
    "Height" "double" "system"
    "Rotation" "double" "system"
    "Backward" "int" "user"
    "Upside Down" "int" "user"
    "Position X" "double" "system"
    "Position Y" "double" "system"
    "END" "END" "END"
  )
)

(define (block-properties)
  (vector
    "Block"
    "Block"
    "Position X" "double" "system"
    "Position Y" "double" "system"
    "END" "END" "END"
  )
)

(define (line-properties)
  (vector
    "Line"
    "Line"
    "Start X" "double" "user"
    "Start Y" "double" "user"
    "End X" "double" "user"
    "End Y" "double" "user"
    "Delta X" "double" "system"
    "Delta Y" "double" "system"
    "Angle" "double" "system"
    "Length" "double" "system"
    "END" "END" "END"
  )
)

(define (polygon-properties)
  (vector
    "Polygon"
    "Polygon"
    "Center X" "double" "user"
    "Center Y" "double" "user"
    "Radius Vertex" "double" "system"
    "Radius Side" "double" "system"
    "Diameter Vertex" "double" "system"
    "Diameter Side" "double" "system"
    "Interior Angle" "double" "system"
    "END" "END" "END"
  )
)

(define (point_properties)
  (vector
    "Point"
    "Point"
    "Point X" "double" "user"
    "Point Y" "double" "user"
    "END" "END" "END"
  )
)

(define (general_general_properties)
  (vector
    "General"
    "General"
    "Layer" "dropdown" "user"
    "Color" "dropdown" "user"
    "Line Type" "dropdown" "user"
    "Line Weight" "dropdown" "user"
    "END" "END" "END"
  )
)

(define (misc_arc_properties)
  (vector
    "Misc"
    "Arc"
    "Clockwise" "int" "system"
    "END" "END" "END"
  )
)

(define (misc_image_properties)
  (vector
    "Misc"
    "Image"
    "Name" "string" "system"
    "Path" "string" "system"
    "END" "END" "END"
  )
)

(define (misc_path_properties)
  (vector
    "Misc"
    "Path"
    "Closed" "int" "user"
    "END" "END" "END"
  )
)

(define (misc_polyline_properties)
  (vector
    "Misc"
    "Polyline"
    "Closed" "int" "user"
    "END" "END" "END"
  )
)

(define (misc_text_single_properties)
  (vector
    "Misc"
    "Text Single"
    "Backward" "int" "user"
    "Upside down" "int" "user"
    "END" "END" "END"
  )
)

(define (geometry_circle_properties)
  (vector
    "Geometry"
    "Circle"
    "Center X" "double" "user"
    "Center Y" "double" "user"
    "Radius" "double" "user"
    "Diameter" "double" "user"
    "Area" "double" "user"
    "Circumference" "double" "user"
    "END" "END" "END"
  )
)

(define (geometry_image_properties)
  (vector
    "Geometry"
    "Image"
    "Position X" "double" "user"
    "Position Y" "double" "user"
    "Width" "double" "user"
    "Height" "double" "user"
    "END" "END" "END"
  )
)

(define (geometry_infinite_line_properties)
  (vector
    "Geometry"
    "Infinite Line"
    "Start X" "double" "user"
    "Start Y" "double" "user"
    "2nd X" "double" "user"
    "2nd Y" "double" "user"
    "Vector X" "double" "system"
    "Vector Y" "double" "system"
    "END" "END" "END"
  )
)

(define (GroupBox10)
  (vector
    "Geometry"
    "Line"
    "Start X" "double" "user"
    "Start Y" "double" "user"
    "End X" "double" "user"
    "End Y""double" "user"
    "Delta X" "double" "system"
    "Delta Y" "double" "system"
    "Angle X" "double" "system"
    "Length Y""double" "system"
    "END" "END" "END"
  )
)

(define (GroupBox9)
  (vector
    "Geometry"
    "Path"
    "Vertex #" "int" "user"
    "Vertex X" "double" "user"
    "Vertex Y" "double" "user"
    "Area" "double" "system"
    "Length" "double" "system"
    "END" "END" "END"
  )
)

(define (GroupBox8)
  (vector
    "Misc"
    "Path"
    "Closed" "int" "user"
    "END" "END" "END"
  )
)

(define (geometry-polygon-properties)
  (vector
    "Geometry"
    "Polygon"
    "Center X" "double" "user"
    "Center Y" "double" "user"
    "Vertex Radius" "double" "user"
    "Side Radius" "double" "user"
    "Vertex Diameter" "double" "user"
    "Side Diameter" "double" "user"
    "Interior Angle" "double" "system"
    "END" "END" "END"
  )
)

(define (geometry-polyline-properties)
  (vector
    "Geometry"
    "Polyline"
    "Vertex #" "int" "user"
    "Vertex X" "double" "user"
    "Vertex Y" "double" "user"
    "Area" "double" "system"
    "Length" "double" "system"
    "END" "END" "END"
  )
)

(define (geometry-ray-properties)
  (vector
    "Geometry"
    "Ray"
    "Start X" "double" "user"
    "Start Y" "double" "user"
    "2nd X" "double" "user"
    "2nd Y" "double" "user"
    "Vector X" "double" "system"
    "Vector Y" "double" "system"
    "END" "END" "END"
  )
)

(define (geometry-text-multi-properties)
  (vector
    "Geometry"
    "Text Multi"
    "Position X" "double" "user"
    "Position Y" "double" "user"
    "END" "END" "END"
  )
)

;(define GroupBox3[] =
;  (vector
;    "Text"
;    "Text Single"
;    "Contents" "string" "user"
;    "Font" "dropdown" "user"
;    "Justify" "dropdown" "user"
;    "Height" "double" "user"
;    "Rotation" "double" "user"
;    "END" "END" "END"
;  )
;)

;(define GroupBox2[] =
;  (vector
;    "Geometry"
;    "Text Single"
;    "Position X" "double" "user"
;    "Position Y" "double" "user"
;    "END" "END" "END"
;  )
;)

;(define GroupBox1[] =
;  (vector
;    "Misc"
;    "Text Single"
;    "Backward" "int" "user"
;    "Upside Down" "int" "user"
;    "END" "END" "END"
;  )
;)

;(define General1[] =
;  (vector
;    "Layer (Toolbutton" " combobox)"
;    "Color (toolbutton" " combobox)"
;    "LineType (toolbutton" " combobox)"
;    "LineWeight (toolbutton" " combobox)"
;    "END" "END" "END"
;  )
;)

;(define Path[] =
;  (vector
;    "VertexNum (toolbutton" " combobox)"
;    "VertexX (toolbutton" " lineedit)"
;    "VertexY (toolbutton" " lineedit)"
;    "Area (toolbutton" " lineedit)"
;    "Length (toolbutton" " lineedit)"
;    "Closed (toolbutton" " combobox)"
;    "END" "END" "END"
;  )
;)

;(define (Polyline)
;  (vector
;    "Polyline"
;    "VertexNum (toolbutton" " combobox)"
;    "VertexX (toolbutton" " lineedit)"
;    "VertexY (toolbutton" " lineedit)"
;    "Area (toolbutton" " lineedit)"
;    "Length (toolbutton" " lineedit)"
;    "Closed (toolbutton" " combobox)"
;    "END" "END" "END"
;  )
;)

;(define Ray)
;    "X1 (toolbutton" " lineedit)"
;    "Y1 (toolbutton" " lineedit)"
;    "X2 (toolbutton" " lineedit)"
;    "Y2 (toolbutton" " lineedit)"
;    "VectorX (toolbutton" " lineedit)"
;    "VectorY (toolbutton" " lineedit)"
;    "END" "END" "END"
;  )
;)

;(define TextMulti)
;    "X (toolbutton" " lineedit)"
;    "Y (toolbutton" " lineedit)"
;    "END" "END" "END"
;  )
;)

