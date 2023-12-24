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

    dark_column_scroll_area_style = """
            QScrollArea {
            border-radius: 10px;
            background-color: #FFFFFF;
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
    light_column_scroll_area_style = """
            QScrollArea {
            border-radius: 10px;
            background-color: #FFFFFF;
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
    desk_not_active_style = """
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
    desk_active_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 1px solid #727CB0;
                            background: #727CB0;
                            color: #C4CDFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 24px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                    }
                    """
    column_scroll_area_style = """
                        QScrollArea {
                            background-color: #1f2338;
                            border: 1px solid rgba(114, 124, 176, 0.5);
                        }
                    """
    column_name_button_style = """
                        border-radius: 10px;
                        border: 1px solid #727CB0;
                        background: #727CB0;
                        color: #C4CDFF;
                        text-align: center;
                        font-family: Comfortaa;
                        font-size: 20px;
                        font-style: normal;
                        font-weight: 400;
                        line-height: 24px; /* 120% */
                    """
    column_delete_button_style = """
                        background: transparent;
                        color: #9A5757;
                        text-align: center;
                        font-family: Comfortaa;
                        font-size: 15px;
                        font-style: normal;
                        font-weight: 400;
                        """
    column_add_card_button_style = """
                        QPushButton {
                            color: rgba(83, 91, 131, 0.46);
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 400;
                            border: 0px solid #727CB0;
                        }
                        
                        QPushButton:hover {
                            color: rgb(160, 171, 231);
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
    card_button_none_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 1px solid #727CB0;
                            background: #363847;
                            color: #C4CDFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                        }
            
                        QPushButton:hover {
                            background: #3d436e;
                            color: #C4CDFF;
                        }
                    """
    card_button_none_active_style = """
                       QPushButton {
                            border-radius: 10px;
                            border: 2px solid #c4cdff;
                            background: #7a85bf;
                            color: #FFFFFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                       }
                    """
    card_button_green_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 1px solid #4CAF50;
                            background: #1e5821;
                            color: #C4CDFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                        }
                        
                        QPushButton:hover {
                            background: #2d7530;
                            color: #C4CDFF;
                        }
                    """
    card_button_green_active_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 2px solid #87ff8d;
                            background: #56c75c;
                            color: #FFFFFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                        }
                    """
    card_button_red_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 1px solid #af4c4c;
                            background: #581e1e;
                            color: #C4CDFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                        }
                        
                        QPushButton:hover {
                            background: #752d2d;
                            color: #C4CDFF;
                        }
                    """
    card_button_red_active_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 2px solid #ff8787;
                            background: #c75656;
                            color: #FFFFFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                        }
                    """
