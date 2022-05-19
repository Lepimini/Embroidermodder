#!/usr/bin/env python3

r"""
    Embroidermodder 2.

    -----

    Copyright 2013-2022 The Embroidermodder Team
    Embroidermodder 2 is Open Source Software.
    See LICENSE for licensing terms.

    -----

"""

import tkinter as tk


class LayerManager():
    r" . "
    def __init__(self, tab, mw, parent):
        r"."
        layer_model = QStandardItemModel(0, 8, this)

        layer_model_sorted = new QSortFilterProxyModel
        layer_model_sorted.setDynamicSortFilter(1)
        layer_model_sorted.setSourceModel(layer_model)

        treeView = new QTreeView
        treeView.setRootIsDecorated(0)
        treeView.setAlternatingRowColors(1)
        treeView.setModel(layer_model_sorted)
        treeView.setSortingEnabled(1)
        treeView.sortByColumn(0, Qt_AscendingOrder)

        mainLayout = tk.VBoxLayout()
        mainLayout.addWidget(treeView)
        setLayout(mainLayout)

        setWindowTitle(translate("Layer Manager"))
        setMinimumSize(750, 550)

        layer_model.setHeaderData(0, Qt_Horizontal, translate("Name"))
        layer_model.setHeaderData(1, Qt_Horizontal, translate("Visible"))
        layer_model.setHeaderData(2, Qt_Horizontal, translate("Frozen"))
        layer_model.setHeaderData(3, Qt_Horizontal, translate("Z Value"))
        layer_model.setHeaderData(4, Qt_Horizontal, translate("Color"))
        layer_model.setHeaderData(5, Qt_Horizontal, translate("Linetype"))
        layer_model.setHeaderData(6, Qt_Horizontal, translate("Lineweight"))
        layer_model.setHeaderData(7, Qt_Horizontal, translate("Print"))

        addLayer("0", 1, 0, 0.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("1", 1, 0, 1.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("2", 1, 0, 2.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("3", 1, 0, 3.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("4", 1, 0, 4.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("5", 1, 0, 5.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("6", 1, 0, 6.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("7", 1, 0, 7.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("8", 1, 0, 8.0, qRgb(0,0,0), "Continuous", "Default", 1)
        addLayer("9", 1, 0, 9.0, qRgb(0,0,0), "Continuous", "Default", 1)

        for(i = 0; i < layer_model.columnCount(); ++i)
            treeView.resizeColumnToContents(i)

        QApplication_setOverrideCursor(Qt_ArrowCursor)

        return self

    def add(self, name, visible=True, frozen=False, zValue=0, color="black",
            lineType="solid", line_weight=0.35):
        r"."
        # const print):
        layer_model.insertRow(0)
        layer_model.setData(layer_model.index(0, 0), name)
        layer_model.setData(layer_model.index(0, 1), visible)
        layer_model.setData(layer_model.index(0, 2), frozen)
        layer_model.setData(layer_model.index(0, 3), zValue)

        colorPix = QPixmap(16, 16)
        colorPix.fill(Color(color))
        layer_model.itemFromIndex(layer_model.index(0, 4)).setIcon(QIcon(colorPix))
        layer_model.setData(layer_model.index(0, 4), Color(color))

        layer_model.setData(layer_model.index(0, 5), lineType)
        layer_model.setData(layer_model.index(0, 6), lineWeight)
        #layer_model.setData(layer_model.index(0, 7), print)

    def layer_model(self):
        r"."
        return

    def layer_model_sorted(self):
        r"."
        return

    def tree_view(self):
        r"."
        return

    def __del__(self):
        r"."
        self.mw.restore_override_cursor()
