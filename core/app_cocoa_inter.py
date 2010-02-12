# -*- coding: utf-8 -*-
# Created By: Virgil Dupras
# Created On: 2010-02-02
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

# Common interface for all editions' dg_cocoa unit.

from hsutil.cocoa.inter import signature, PyOutline, PyGUIObject, PyRegistrable

from .gui.details_panel import DetailsPanel
from .gui.directory_tree import DirectoryTree
from .gui.result_tree import ResultTree
from .gui.stats_label import StatsLabel

# Fix py2app's problems on relative imports
from core import app, app_cocoa, data, directories, engine, export, ignore, results, fs, scanner
from hsutil import conflict

class PyDupeGuruBase(PyRegistrable):
    #---Directories
    def addDirectory_(self, directory):
        return self.py.add_directory(directory)
    
    def removeDirectory_(self, index):
        self.py.remove_directory(index)
    
    #---Results
    def clearIgnoreList(self):
        self.py.scanner.ignore_list.Clear()
    
    def doScan(self):
        return self.py.start_scanning()
    
    def exportToXHTMLwithColumns_(self, column_ids):
        return self.py.export_to_xhtml(column_ids)
    
    def loadIgnoreList(self):
        self.py.load_ignore_list()
    
    def loadResults(self):
        self.py.load()
    
    def markAll(self):
        self.py.mark_all()
    
    def markNone(self):
        self.py.mark_none()
    
    def markInvert(self):
        self.py.mark_invert()
    
    def purgeIgnoreList(self):
        self.py.PurgeIgnoreList()
    
    def toggleSelectedMark(self):
        self.py.toggle_selected_mark_state()
    
    def saveIgnoreList(self):
        self.py.save_ignore_list()
    
    def saveResults(self):
        self.py.save()
    
    #---Actions
    def addSelectedToIgnoreList(self):
        self.py.add_selected_to_ignore_list()
    
    def deleteMarked(self):
        self.py.delete_marked()
    
    def applyFilter_(self, filter):
        self.py.apply_filter(filter)
    
    def makeSelectedReference(self):
        self.py.make_selected_reference()
    
    def copyOrMove_markedTo_recreatePath_(self, copy, destination, recreate_path):
        self.py.copy_or_move_marked(copy, destination, recreate_path)
    
    def openSelected(self):
        self.py.open_selected()
    
    def removeMarked(self):
        self.py.results.perform_on_marked(lambda x:True, True)
    
    def removeSelected(self):
        self.py.remove_selected()
    
    def renameSelected_(self,newname):
        return self.py.rename_selected(newname)
    
    def revealSelected(self):
        self.py.reveal_selected()
    
    #---Information
    def getIgnoreListCount(self):
        return len(self.py.scanner.ignore_list)
    
    def getMarkCount(self):
        return self.py.results.mark_count
    
    def getOperationalErrorCount(self):
        return self.py.last_op_error_count
    
    #---Properties
    def setMixFileKind_(self, mix_file_kind):
        self.py.scanner.mix_file_kind = mix_file_kind
    
    def setEscapeFilterRegexp_(self, escape_filter_regexp):
        self.py.options['escape_filter_regexp'] = escape_filter_regexp
    
    def setRemoveEmptyFolders_(self, remove_empty_folders):
        self.py.options['clean_empty_dirs'] = remove_empty_folders
    
    #---Worker
    def getJobProgress(self):
        return self.py.progress.last_progress
    
    def getJobDesc(self):
        return self.py.progress.last_desc
    
    def cancelJob(self):
        self.py.progress.job_cancelled = True
    
    def jobCompleted_(self, jobid):
        self.py._job_completed(jobid)
    

class PyDetailsPanel(PyGUIObject):
    py_class = DetailsPanel
    @signature('i@:')
    def numberOfRows(self):
        return self.py.row_count()
    
    @signature('@@:@i')
    def valueForColumn_row_(self, column, row):
        return self.py.row(row)[int(column)]
    

class PyDirectoryOutline(PyOutline):
    py_class = DirectoryTree
    
    def addDirectory_(self, path):
        self.py.add_directory(path)
    

class PyResultOutline(PyOutline):
    py_class = ResultTree
    
    @signature('c@:')
    def powerMarkerMode(self):
        return self.py.power_marker
    
    @signature('v@:c')
    def setPowerMarkerMode_(self, value):
        self.py.power_marker = value
    
    @signature('c@:')
    def deltaValuesMode(self):
        return self.py.delta_values
    
    @signature('v@:c')
    def setDeltaValuesMode_(self, value):
        self.py.delta_values = value
    
    @signature('@@:@i')
    def valueForPath_column_(self, path, column):
        return self.py.get_node_value(path, column)
    
    @signature('c@:@')
    def renameSelected_(self, newname):
        return self.py.app.rename_selected(newname)
    
    @signature('v@:ic')
    def sortBy_ascending_(self, key, asc):
        self.py.sort(key, asc)
    
    def markSelected(self):
        self.py.app.toggle_selected_mark_state()
    
    def rootChildrenCounts(self):
        return self.py.root_children_counts()
    
    # python --> cocoa
    def invalidate_markings(self):
        self.cocoa.invalidateMarkings()
    

class PyStatsLabel(PyGUIObject):
    py_class = StatsLabel
    
    def display(self):
        return self.py.display
    