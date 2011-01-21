# Created By: Virgil Dupras
# Created On: 2009-05-23
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMessageBox, QAction

from hscommon.trans import tr, trmsg
from ..base.result_window import ResultWindow as ResultWindowBase

class ResultWindow(ResultWindowBase):
    def _setupUi(self):
        ResultWindowBase._setupUi(self)
        self.actionClearPictureCache = QAction(tr("Clear Picture Cache"), self)
        self.menuFile.insertAction(self.actionClearIgnoreList, self.actionClearPictureCache)
        self.connect(self.actionClearPictureCache, SIGNAL("triggered()"), self.clearPictureCacheTriggered)
    
    def clearPictureCacheTriggered(self):
        title = tr("Clear Picture Cache")
        msg = trmsg("ClearPictureCacheConfirmMsg")
        if self.app.confirm(title, msg, QMessageBox.No):
            self.app.scanner.clear_picture_cache()
            QMessageBox.information(self, title, trmsg("PictureCacheClearedMsg"))
    