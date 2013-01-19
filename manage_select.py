import sublime, sublime_plugin

class Selection(object):
    saved = []

    def SaveRegions(self,regions) :
        self.saved = [region for region in regions]


    def GetRegions(self) :
        print "Get :"
        print self.saved
        return self.saved

    def ClearRegions(self, regions) :
        self.saved = []


class ManageSelectCommand(sublime_plugin.TextCommand, Selection):
    def run(self, edit, action="save"):
        regions = self.view.sel()
        saved_regions = self.GetRegions()
        if action=="save" or action=="exchange":
            self.SaveRegions(regions)
        if not saved_regions :
            return
        if action=="restore" or action=="exchange":
            regions.clear()    
        if action=="restore"  or action=="exchange" or action=="add" :
            for region in saved_regions:
                regions.add(region)
        elif action=="subtract" :
            for region in saved_regions:
                regions.subtract(sublime.Region(region.a,region.b))     
        