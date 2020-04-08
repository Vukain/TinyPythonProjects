import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTabBar, QFrame,
                             QStackedLayout, QShortcut, QSplitter)
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()


class Application(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyBrowser")
        self.setMinimumSize(1024, 768)
        self.create_app()
        self.setWindowIcon(QIcon("resources/logo.png"))
        self.show()

    def create_app(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout = QHBoxLayout()

        # Create tabs
        tab_bar = QTabBar(movable=True, tabsClosable=True)
        tab_bar.tabCloseRequested.connect(self.close_tab)
        tab_bar.tabBarClicked.connect(self.switch_tab)
        tab_bar.setCurrentIndex(0)
        tab_bar.setDrawBase(False)
        self.tab_count = 0
        self.tabs = []

        # Shortcuts
        QShortcut(QKeySequence.AddTab, self).activated.connect(self.add_tab)
        QShortcut(QKeySequence.Refresh, self).activated.connect(self.reload_tab)
        QShortcut(QKeySequence("Ctrl+R"), self).activated.connect(self.reload_tab)

        # Create Tool bar
        toolbar = QWidget()
        toolbar.setObjectName("Toolbar")
        toolbar.setLayout(toolbar_layout)

        # Navigation buttons
        back_button = QPushButton("«")
        back_button.clicked.connect(self.go_back)
        toolbar_layout.addWidget(back_button)

        forward_button = QPushButton("»")
        forward_button.clicked.connect(self.go_forward)
        toolbar_layout.addWidget(forward_button)

        reload_button = QPushButton("¤")
        reload_button.clicked.connect(self.reload_tab)
        toolbar_layout.addWidget(reload_button)

        # Address bar
        address_bar = AddressBar()
        address_bar.returnPressed.connect(self.browse_to)
        toolbar_layout.addWidget(address_bar)

        # New tab button
        add_tab_button = QPushButton("+")
        add_tab_button.clicked.connect(self.add_tab)
        toolbar_layout.addWidget(add_tab_button)

        # set main view
        container = QWidget()
        container.layout = QStackedLayout()
        container.setLayout(container.layout)

        layout.addWidget(tab_bar)
        layout.addWidget(toolbar)
        layout.addWidget(container)
        self.setLayout(layout)

        # save objects in class
        self.tab_bar = tab_bar
        self.container = container
        self.address_bar = address_bar

        # get one tab
        self.add_tab()

    def close_tab(self, index):
        self.tab_bar.removeTab(index)
        self.tab_count -= 1
        self.tabs.pop(index)
        if self.tab_count > index:
            self.switch_tab(index)
        elif self.tab_count > 0:
            self.switch_tab(index - 1)

    def switch_tab(self, index):
        tab_name = self.tab_bar.tabData(index)["object"]
        tab_content = self.findChild(QWidget, tab_name)
        self.address_bar.setText(tab_content.content.url().toString())
        self.container.layout.setCurrentWidget(tab_content)

    def add_tab(self):
        index = self.tab_count
        self.tabs.append(QWidget())
        self.tabs[index].layout = QVBoxLayout()
        self.tabs[index].layout.setContentsMargins(0, 0, 0, 0)
        self.tabs[index].setObjectName("tab" + str(index))
        self.tabs[index].content = QWebEngineView()
        # Create default URL
        url = QUrl()
        url = url.fromUserInput("https://www.google.de")
        self.tabs[index].content.load(url)
        # register events
        self.tabs[index].content.titleChanged.connect(lambda: self.update_tab(index, "title"))
        self.tabs[index].content.iconChanged.connect(lambda: self.update_tab(index, "icon"))
        self.tabs[index].content.urlChanged.connect(lambda: self.update_tab(index, "url"))
        # create split view
        self.tabs[index].splitview = QSplitter()
        self.tabs[index].splitview.setOrientation(Qt.Vertical)
        self.tabs[index].layout.addWidget(self.tabs[index].splitview)
        self.tabs[index].splitview.addWidget(self.tabs[index].content)

        self.tabs[index].setLayout(self.tabs[index].layout)
        self.container.layout.addWidget(self.tabs[index])
        self.container.layout.setCurrentWidget(self.tabs[index])

        self.tab_bar.addTab("New tab")
        self.tab_bar.setTabData(index, {"object": "tab" + str(index), "initial": index})
        self.tab_bar.setCurrentIndex(index)
        self.tab_count += 1

    def browse_to(self):
        text = self.address_bar.text()
        index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(index)["object"]
        tab_content = self.findChild(QWidget, tab_name)

        if "http" not in text:
            if "." not in text:
                url = "https://www.google.com/search?q=" + text
            else:
                url = "http://" + text
        else:
            url = text

        tab_content.content.load(QUrl().fromUserInput(url))

    def reload_tab(self):
        index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(index)["object"]
        tab_content = self.findChild(QWidget, tab_name)
        tab_content.content.reload()

    def go_back(self):
        index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(index)["object"]
        tab_content = self.findChild(QWidget, tab_name)
        tab_content.content.back()

    def go_forward(self):
        index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(index)["object"]
        tab_content = self.findChild(QWidget, tab_name)
        tab_content.content.forward()

    def update_tab(self, index, type):
        tab_name = self.tabs[index].objectName()
        tab_content = self.findChild(QWidget, tab_name)
        current_tab = self.tab_bar.tabData(self.tab_bar.currentIndex())["object"]

        if tab_name == current_tab and type == "url":
            self.address_bar.setText(tab_content.content.url().toString())
        else:
            count = 0
            while True:
                if count >= self.tab_count:
                    break;
                tab_data_name = self.tab_bar.tabData(count)["object"]

                if tab_data_name == tab_name:
                    if type == "title":
                        title = tab_content.content.title()
                        self.tab_bar.setTabText(count, title)
                    elif type == "icon":
                        icon = tab_content.content.icon()
                        self.tab_bar.setTabIcon(count, icon)
                    break
                count += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = "667"

    window = Application()

    with open("resources/browser.css", "r") as style:
        app.setStyleSheet(style.read())

    sys.exit(app.exec_())