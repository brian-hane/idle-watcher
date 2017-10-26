import sublime
import sublime_plugin


class IdleWatcher(sublimeplugin.Plugin):
    pending = 0
    
    def handleTimeout(self, view):
        self.pending = self.pending - 1
        if self.pending == 0:
            # There are no more queued up calls to handleTimeout, so it must have
            # been 1000ms since the last modification
            self.onIdle(view)

    def onModified(self, view):
        self.pending = self.pending + 1
        # Ask for handleTimeout to be called in 1000ms
        sublime.setTimeout(functools.partial(self.handleTimeout, view), 1000)

    def onIdle(self, view):
        print "No activity in the past 1000ms"