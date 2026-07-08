"""
DomainHunter Pro X
Version : 0.1.0-alpha
Module  : Global Styles
"""

MAIN_STYLE = """
/* --------------------------------------------------
   GLOBAL
-------------------------------------------------- */

QMainWindow{
    background:#1e1f22;
}

QWidget{
    background:#1e1f22;
    color:#f5f5f5;
    font-family:Segoe UI;
    font-size:13px;
}

/* --------------------------------------------------
   HEADER
-------------------------------------------------- */

QFrame#Header{
    background:#313338;
    border:none;
}

QLabel#Title{
    font-size:24px;
    font-weight:bold;
    color:white;
    padding-left:10px;
}

/* --------------------------------------------------
   SIDEBAR
-------------------------------------------------- */

QFrame#Sidebar{
    background:#2b2d31;
    border-right:1px solid #3f4147;
}

QPushButton#SidebarButton{

    background:#3a3d41;

    border:none;

    border-radius:8px;

    padding:10px 14px;

    text-align:left;

    color:white;

    font-size:13px;
}

QPushButton#SidebarButton:hover{

    background:#4a4d52;
}

QPushButton#SidebarButton:pressed{

    background:#5a5d62;
}

QPushButton#SidebarButton:checked{

    background:#0b84ff;

    color:white;

    font-weight:bold;
}

/* --------------------------------------------------
   CONTENT
-------------------------------------------------- */

QFrame#Content{

    background:#1e1f22;
}

/* --------------------------------------------------
   STATUS BAR
-------------------------------------------------- */

QStatusBar{

    background:#2b2d31;

    color:white;

    border-top:1px solid #3f4147;
}
"""