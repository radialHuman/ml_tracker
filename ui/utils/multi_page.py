'''
DOCUMENTATION
=============

Copied from 

# https://www.youtube.com/watch?v=nSw96qUbK9o&list=WL&index=4
# https://github.com/dataprofessor/multi-page-app/blob/main/multiapp.py

Not sure how it works, but facilitates multi pgae and drop down to navigate

'''


"""Frameworks for running multiple Streamlit applications as a single app.
"""

# https://www.youtube.com/watch?v=nSw96qUbK9o&list=WL&index=4
# https://github.com/dataprofessor/multi-page-app/blob/main/multiapp.py




import streamlit as st
class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.button("")
        app = st.selectbox(
            '',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
