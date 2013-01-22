import sublime, sublime_plugin

class Selection(object):
    saved = []

    def CopyRegions(self, regions) :
        return [region for region in regions]

    def SaveRegions(self, regions) :
        self.saved = self.CopyRegions(regions)

    def GetRegions(self) :
        return self.saved

    def ClearRegions(self, regions) :
        self.saved = []


class ManageSelectCommand(sublime_plugin.TextCommand, Selection):
    def run(self, edit, action="save"):
        regions = self.view.sel()
        print "----- begin -----"
        for region in regions:
                print(region)
        print "----- begin -----"
        saved_regions = self.GetRegions()

        if action == "save" or action == "exchange":
            self.SaveRegions(regions)

        if action == "restore" or action == "exchange":
            if saved_regions :
                regions.clear()    

        if action == "restore"  or action == "exchange" or action == "add" :
            for region in saved_regions:
                regions.add(region)
        elif action == "subtract" :
            for region in saved_regions:
                regions.subtract(sublime.Region(region.a,region.b))

        if action == "inverse" :
            regions_temp = self.CopyRegions(regions)
            regions.clear()
            n = 0 # the number of new regions
            a = 0
            for region in regions_temp:
                print(region)
                if region.empty():
                    continue
                b = region.begin()
                if (a != b) :
                    regions.add(sublime.Region(a,b))
                    n += 1
                a = region.end()

            b = self.view.size()
            if (a != b or n == 0) :
                regions.add(sublime.Region(a,b))
                
        if action == "repeate" :            
            def repeate_done(str_num):
                try:
                    self.num = int(str_num)
                except exceptions.ValueError:
                    return    
                edit = self.view.begin_edit()
                # ---------------------------
                # repate for all regions
                # ---------------------------    
                for region in reversed(regions) :
                    text = self.view.substr(region)
                    self.view.replace(edit, region, text*self.num)
                # ---------------------------    
                self.view.end_edit(edit)
            try :   
                str_num = str(self.num)
            except :
                str_num = ''    
            self.view.window().show_input_panel("number to repeate", str_num, repeate_done, None, None)        
        
        regions = self.view.sel()
        print "----- end -----"
        for region in regions:
                print(region)
        print "----- end -----"
