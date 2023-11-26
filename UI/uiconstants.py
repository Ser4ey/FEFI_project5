class UIConst:
    new_user_page = 0
    auth_page = 1
    set_pass_page = 2
    change_pass_page = 3
    desks_page = 4
    card_page = 5

    icons_path = "data/ui/icons"
    fonts_path = "data/ui/fonts"
    styles_path = "data/ui/styles"

    column_scroll_area_style = """
            QScrollArea {
            border-radius: 10px;
            background-color: #363847;
        }
        
        QScrollBar:vertical {
            background: transparent;
            width: 15px;
            margin: 15px 3px 15px 3px;
            border: 1px transparent #2A2929;
            border-radius: 4px;
        }
        
        QScrollBar::handle:vertical {
            background-color: rgba(196, 205, 255, 0.555);
            min-height: 5px;
            border-radius: 4px;
        }
        
        QScrollBar::sub-line:vertical {
            margin: 3px 0px 3px 0px;
            border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
            height: 10px;
            width: 10px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        
        QScrollBar::add-line:vertical {
            margin: 3px 0px 3px 0px;
            border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
            height: 10px;
            width: 10px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        
        QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {
            border-image: url(:/qss_icons/rc/up_arrow.png);
            height: 10px;
            width: 10px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        
        QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {
            border-image: url(:/qss_icons/rc/down_arrow.png);
            height: 10px;
            width: 10px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
            background: none;
        }
        
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        
        QScrollArea QWidget {
            background-color: transparent;
        }

        """
    desk_button_style = """
            QPushButton {
                border-radius: 10px;
                border: 1px solid #727CB0;
                background: #363847;
                color: #C4CDFF;
                text-align: center;
                font-family: Comfortaa;
                font-size: 24px;
                font-style: normal;
                font-weight: 500;
                line-height: 24px;
            }

            QPushButton:hover {
                background: #3d436e;
                color: #C4CDFF;
            }
        """