import sublime
import sublime_plugin
from os.path import expanduser
from subprocess import call


class TfsCheckoutCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            user_path = expanduser('~')
            return_code = call([user_path + "/Local/tfs/tf", "checkout", self.view.file_name()])
            sublime.status_message("TFS Checkout: " + str(return_code))

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0
