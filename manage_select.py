import sublime, sublime_plugin


class Selection(object):
    saved = []  # contain all saved regions
    regions_copy = []  # copy of all regions

    def CopyRegions(self, regions):
        return [region for region in regions]

    def SaveRegions(self, regions):
        self.saved = self.CopyRegions(regions)

    def GetRegions(self):
        return self.saved

    def ClearRegions(self, regions):
        self.saved = []


class ManageSelectCommand(sublime_plugin.TextCommand, Selection):
    def run(self, edit, action="save"):
        regions = self.view.sel()
        saved_regions = self.GetRegions()

        if action == "save" or action == "exchange":
            self.SaveRegions(regions)

        if action == "restore" or action == "exchange":
            if saved_regions:
                regions.clear()

        if action == "restore" or action == "exchange" or action == "add":
            for region in saved_regions:
                regions.add(region)
        elif action == "subtract":
            for region in saved_regions:
                regions.subtract(sublime.Region(region.a, region.b))

        if action == "inverse":
            self.regions_copy = self.CopyRegions(regions)
            regions.clear()
            n = 0  # the number of new regions
            a = 0
            for region in self.regions_copy:
                if region.empty():
                    continue
                b = region.begin()
                if a != b:
                    regions.add(sublime.Region(a, b))
                    n += 1
                a = region.end()

            b = self.view.size()
            if a != b or n == 0:
                regions.add(sublime.Region(a, b))
            self.regions_copy = []  # free memory


class ExtendSelection(sublime_plugin.TextCommand, Selection):
    extendto_reg_key = "regions_with_input_text"

    # this command can have two actions: literal and regex
    def run(self, edit, action="literal"):
        self.regions_copy = self.CopyRegions(self.view.sel())
        self.regex = "regex" in action
        if self.regex:
            msg = "Regex"
        else:
            msg = "Literal"
        self.ignore_case = "sensitive" not in action
        if self.ignore_case:
            msg += " (ignore case)"
        msg += " extend to:"
        sublime.active_window().show_input_panel(
            msg, "", self.on_done, self.on_change, self.on_cancel
        )

    def on_done(self, user_input):
        self.regions_copy = []  # free memory
        self.view.erase_regions(self.extendto_reg_key)

    def on_change(self, user_input):
        regions = self.view.sel()
        regions.clear()
        if self.regex:
            flag = 0  # there is no flag for regex
        else:
            flag = sublime.LITERAL
        if self.ignore_case:
            flag |= sublime.IGNORECASE
        find_all = self.view.find_all(user_input, flag) if user_input else []
        find_all_len = len(find_all)
        j = 0
        for i, region in enumerate(self.regions_copy):
            new_region = sublime.Region(region.a, region.b)
            while j < find_all_len:
                if region.b < region.a:
                    if find_all[j].end() <= region.b:
                        if i == 0 or find_all[j].end() > self.regions_copy[i - 1].end():
                            new_region = sublime.Region(region.a, find_all[j].end())
                        j += 1
                    else:
                        break
                else:
                    if find_all[j].begin() < region.b:
                        j += 1
                    else:
                        if (
                            i + 1 >= len(self.regions_copy)
                            or find_all[j].begin() < self.regions_copy[i + 1].begin()
                        ):
                            new_region = sublime.Region(region.a, find_all[j].begin())
                        break
            regions.add(new_region)
        # Bug https://github.com/SublimeTextIssues/Core/issues/485
        self.view.add_regions(
            self.extendto_reg_key, find_all, "string", "", sublime.DRAW_OUTLINED
        )

    def on_cancel(self):
        regions = self.view.sel()
        regions.clear()
        for region in self.regions_copy:
            regions.add(sublime.Region(region.a, region.b))
        self.regions_copy = []  # free memory
        self.view.erase_regions(self.extendto_reg_key)
