import sublime, sublime_plugin

class MoveSelectCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=False):
        regions = self.view.sel()
        regions_copy = [region for region in regions]

        for region in regions_copy :
            if forward :
                if region.end() < self.view.size():
                    regions.subtract(region)
                    regions.add(sublime.Region(region.a+1, region.b+1))
            else :
                if region.begin() > 0:
                    regions.subtract(region)
                    regions.add(sublime.Region(region.a-1, region.b-1))


class MoveInSelectCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=False):
        regions = self.view.sel()
        regions_copy = [region for region in regions]
        
        changed = False
        for region in regions_copy :
            if forward :
                swap = region.a > region.b
            else :
                swap = region.a < region.b

            if swap :
                regions.add(sublime.Region(region.b, region.a))
                changed = True

        if not changed :
            self.view.run_command("move", {"by": "words", "forward": forward})
