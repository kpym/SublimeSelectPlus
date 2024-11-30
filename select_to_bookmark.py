import sublime, sublime_plugin


class SelectToBookmarkCommand(sublime_plugin.TextCommand):
    extendto_reg_key = "regions_with_input_text"

    def run(self, edit, forward=True):
        if forward:
            bookmarks = [b for b in self.view.get_regions("bookmarks")]
        else:
            bookmarks = [b for b in reversed(self.view.get_regions("bookmarks"))]
        regions = self.view.sel()
        regions_copy = [region for region in regions]
        regions.clear()
        j = 0
        for i, cr in enumerate(regions_copy):
            new_region = cr
            if forward:
                for j, bm in enumerate(bookmarks):
                    if bm.end() <= cr.begin():
                        continue
                    if bm.begin() > cr.end():
                        new_region = sublime.Region(cr.begin(), bm.begin())
                    break
            else:
                for j, bm in enumerate(bookmarks):
                    if bm.begin() >= cr.end():
                        continue
                    if bm.end() < cr.begin():
                        new_region = sublime.Region(cr.end(), bm.end())
                        break
            # add the new region
            regions.add(new_region)
