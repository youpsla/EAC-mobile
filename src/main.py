import os
import sys
from importlib import reload
 

def get_application():
    if sys.platform == 'darwin':
        from enamlnative.ios.app import IPhoneApplication
        return IPhoneApplication
    else:
        from enamlnative.android.app import AndroidApplication
        return AndroidApplication


def main():
    Application = get_application()
    app = Application(
        debug=False,  # Uncomment to debug the bridge
        # dev='192.168.0.41',  # Set to 'server', 'remote', an IP address
        dev = 'server',
        load_view=load_view
    )
    app.start()


def load_view(app):
    # Create and show the enaml view
    import enaml
    with enaml.imports():
        import view
        if app.view:
            #: The view was already set so reload
            reload(view)
        app.view = view.ContentView()
    app.show_view()





if __name__ == '__main__':
    # This is used when remote debugging
    # Init remote nativehooks implementation
    from enamlnative.core import remotehooks
    remotehooks.init()
    main()
