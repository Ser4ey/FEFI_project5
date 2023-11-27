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
                        border: none;
                        background: rgba(114, 124, 176, 0.5);
                        color: #C4CDFF;
                        text-align: center;
                        font-family: Comfortaa;
                        font-size: 20px;
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
                            color: rgba(196, 205, 255, 0.46);
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
    card_button_green_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 1px solid #4CAF50;
                            background: #2E7D32;
                            color: #C4CDFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                        }
                        
                        QPushButton:hover {
                            background: #43A047;
                            color: #C4CDFF;
                        }
                    """
    card_button_red_style = """
                        QPushButton {
                            border-radius: 10px;
                            border: 1px solid #E53935;
                            background: #D32F2F;
                            color: #C4CDFF;
                            text-align: center;
                            font-family: Comfortaa;
                            font-size: 16px;
                            font-style: normal;
                            font-weight: 500;
                            line-height: 24px;
                        }
                        
                        QPushButton:hover {
                            background: #FF5252;
                            color: #C4CDFF;
                        }
                    """
