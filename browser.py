from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**Kwargs):
        super(MainWindow,self).__init__(*args , **Kwargs)
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.urlbar = QLineEdit()
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.status=QStatusBar()
        self.setCentralWidget(self.browser)

        self.setStatusBar(self.status)

        #for navigation-------
        navtb=QToolBar("Navigation")
        self.addToolBar(navtb)
        back_btn=QAction("Back",self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        forward_btn=QAction("forward",self)
        forward_btn.triggered.connect(self.browser.forward)
        navtb.addAction(forward_btn)

        reload_btn=QAction("reload",self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn=QAction("Home",self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)


        self.show()

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme()=="":
            q.setScheme("http")
        
        self.browser.setUrl(q)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com"))

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
    
    def update_title(self):
        title=self.browser.page().title()
        self.setWindowTitle(f"")

app=QApplication(sys.argv)
app.setApplicationName("My Browser")
window=MainWindow()
app.exec_()