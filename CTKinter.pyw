from logging import basicConfig as LogBasConf, error as LogErr, ERROR as LogERROR
from customtkinter import CTk, CTkTabview, set_appearance_mode, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkFont, CTkScrollableFrame, CTkComboBox, BooleanVar, CTkCheckBox, CTkToplevel, CTkSlider
#from time import sleep as time_sleep
from json import load as json_load, dump as json_dump
from pathlib import Path
from os import path as os_path, system as os_system, getpid as os_getpid
import sys
from webbrowser import open as web_open

current_directory = os_path.dirname(__file__)

LogBasConf(filename="app.log", level=LogERROR, format="\n\n\n%(asctime)s - %(name)s - %(message)s\n")

def get_config_path():
    if getattr(sys, 'frozen', False):
        base_path = os_path.dirname(sys.executable)
    else:
        base_path = os_path.dirname(__file__)
    return os_path.join(base_path, 'config','autoclicker.json')

try:
    with open(get_config_path(), 'r') as auto_spec:
        auto_specs = json_load(auto_spec)
except Exception as e:
    LogErr("You deleted 'Autoclicker.json'!\n%s", str(e), exc_info=True)
    os_system('taskkill /F /PID ' + str(os_getpid()))

try:
    try:
        base_path = sys._MEIPASS2
    except AttributeError:
        base_path = Path(__file__).parent
    icon_path = os_path.join(base_path, 'Autoclicker.ico')

except Exception as e:
    LogErr(f"Error with a file icon!")

def RESTART():
    app.destroy()
    App()

#App
def App():

    try:
        Language = auto_specs["Language"]
        Auto_Start = auto_specs["Auto_Start"]
        Auto_Disable = auto_specs["Auto_Disable"]
        Auto_Exit = auto_specs["Auto_Exit"]
        Function_Name = auto_specs["Function_Name"]
        topmost = auto_specs["topmost"]
        theme = auto_specs["theme"]
        standart_geometry = auto_specs["standart_geometry"]
        allow_updates = auto_specs["allow_updates"]
        toolwindow = auto_specs["toolwindow"]
        alpha = auto_specs["alpha"]
        Version = auto_specs["Version"]

        Simple_interval = auto_specs["Simple_Function"]["interval"]
        Simple_clicks = auto_specs["Simple_Function"]["clicks"]
        Simple_button = auto_specs["Simple_Function"]["button"]
        Simple_duration = auto_specs["Simple_Function"]["duration"]
        Simple_repeat = auto_specs["Simple_Function"]["repeat"]
    except Exception as e:
        LogErr(f"Something went wrong with '{os_path.abspath('autoclicker.json')}'!\n", str(e), exc_info=True)
        os_system('taskkill /F /PID ' + str(os_getpid()))

    if Language==1:
        Autoclicker = f"Autoclicker by @arturwol {Version}"
        Settings = "Settings"
        ChangeLogs = "ChangeLogs"
        Credits = "Credits"
        Other = "Other"
        Click_interval = "Click interval"
        Clicks_per_interval = "Clicks per interval"
        Duration = "Duration"
        Click_button = "Click button"
        Clicks_repeat = "Clicks repeat"
        times = "times"
        Confirm_all = "Confirm all settings!"
        Start = "Start"
        Stop = "Stop"
        Exit = "Exit"
        Simple_Functions = "Simple Functions"
        Hard_Functions = "Hard Functions"
        Future_Update = "Future Update"
        Next_Update = "Next Update"
        Current_Update = "Current Update"
        Past_Update = "Past Update"
        Old_Update = "Old Update"
        themes = ["System","Dark","Light"]
        Top_most = "On top of other applications"
        geometry = "Standart screen resolution:"
        Succesfully_changed_to = "Succesfully changed to:"
        Confirm = "Confirm!"
        ToolWindow = "Tool Window"
        AlphaDescription = f"Opacity selection from 0 to 1 ({round(alpha,3)})"
        update = f"Autoclicker UPDATE {Version}"
        confirm_to_update = f"Autoclicker has received an update {Version}!\n\nIf you want to update it, click “Redeem” and you will be taken to: https://github.com/arturwo1/Autoclicker.\n\nIf you don't want to get cool new features and bug fixes in your autoclicker, click “Cancel”."
        Redeem = "Redeem"
        Cancel = "Cancel"
        See_Updates = "Did you want to see Updates notification?"
    elif Language==2:
        Autoclicker = f"Автокликер от @arturwol {Version}"
        Settings = "Настройки"
        ChangeLogs = "Список изменений"
        Credits = "Авторы"
        Other = "Другое"
        Click_interval = "Интервал кликов"
        Clicks_per_interval = "Кликов за интервал"
        Duration = "Длительность"
        Click_button = "Кнопка"
        Clicks_repeat = "Повторение кликов"
        times = "раз"
        Confirm_all = "Подтвердить все настройки!"
        Start = "Старт"
        Stop = "Стоп"
        Exit = "Выход"
        Simple_Functions = "Простые Функции"
        Hard_Functions = "Сложные Функции"
        Future_Update = "Будущее Обновление"
        Next_Update = "Следующее Обновление"
        Current_Update = "Текущее Обновление"
        Past_Update = "Прошлое Обновление"
        Old_Update = "Дайвнейшее обновление"
        themes = ["Системная","Тёмная","Светлая"]
        Top_most = "Поверх других приложений"
        geometry = "Стандартное разрешение экрана:"
        Succesfully_changed_to = "Изменено на:"
        Confirm = "Подтвердить!"
        update = f"Обновление Автокликера {Version}"
        ToolWindow = "Окно Инструментов"
        AlphaDescription = f"Выбор непрозрачности от 0 до 1 ({round(alpha,3)})"
        update = f"Обновление Автокликера {Version}"
        confirm_to_update = f"Автокликер получил обновление {Version}!\n\nЕсли вы хотите обновить его, нажмите «Перейти» и вы перейдете на сайт: https://github.com/arturwo1/Autoclicker.\n\nЕсли вы не хотите получить новые возможности и исправления ошибок в вашем Автокликере, нажмите «Отмена»."
        Redeem = "Перейти"
        Cancel = "Отмена"
        See_Updates = "Хотите ли вы видеть уведомления о обновлениях?"
    elif Language==3:
        Autoclicker = f"Autoclicker pagal @arturwol {Version}"
        Settings = "Parametrai"
        ChangeLogs = "Pakeitimų žurnalai"
        Credits = "Autoriai"
        Other = "Kita"
        Click_interval = "Spustelėkite intervalą"
        Clicks_per_interval = "Paspaudimai per intervalą"
        Duration = "Trukmė"
        Click_button = "Spustelėkite mygtuką"
        Clicks_repeat = "Paspaudimai kartojasi"
        times = "kartus"
        Confirm_all = "Patvirtinti visi parametrai!"
        Start = "Startas"
        Stop = "Sustabdyti"
        Exit = "Išeiti"
        Simple_Functions = "Paprastos funkcijos"
        Hard_Functions = "Sunkiosios funkcijos"
        Future_Update = "Būsimas Atnaujinimas"
        Next_Update = "Kitas Atnaujinimas"
        Current_Update = "Dabartinis Atnaujinimas"
        Past_Update = "Praeities Naujienos"
        Old_Update = "Praeities Atnaujinimas"
        themes = ["Sisteminis","Tamsioji","Šviesos"]
        Top_most = "Ant kitų programų"
        geometry = "Standartinis ekrano skiriamoji geba:"
        Succesfully_changed_to = "Pakeista į:"
        Confirm = "Patvirtinti!"
        update = f"Autoclicker Atnaujinimas {Version}"
        ToolWindow = "Įrankių Langas"
        AlphaDescription = f"Neskaidrumo pasirinkimas nuo 0 iki 1 ({round(alpha,3)})"
        confirm_to_update = f"„Autoclicker“ gavo atnaujinimą {Version}\n\n!Jei norite jį atnaujinti, spustelėkite “Eiti į“ ir jis nukels jus į svetainę: https://github.com/arturwo1/Autoclicker.\n\nJei nenorite gauti naujų funkcijų ir ištaisytų klaidų savo Autoclicker, spustelėkite “Atšaukimas“."
        Redeem = "Eiti į"
        Cancel = "Atšaukimas"
        See_Updates = "Ar norėtumėte gauti pranešimus apie atnaujinimus?"
    else:
        Autoclicker = " "
        Settings = " "
        ChangeLogs = "  "
        Credits = "   "
        Other = "    "
        Click_interval = " "
        Clicks_per_interval = " "
        Duration = " "
        Click_button = " "
        Clicks_repeat = " "
        times = " "
        Confirm_all = " "
        Start = " "
        Stop = " "
        Exit = " "
        Simple_Functions = " "
        Hard_Functions = " "
        Future_Update = " "
        Next_Update = " "
        Current_Update = " "
        Past_Update = " "
        Old_Update = " "
        themes = [" "," "," "]
        Top_most = " "
        geometry = " "
        Succesfully_changed_to = " "
        Confirm = " "
        update = " "
        ToolWindow = " "
        AlphaDescription = " "
        confirm_to_update = " "
        Redeem = " "
        Cancel = " "
        See_Updates = " "

    global app

    def CONFIRM():
        try:
            fcsientry = float(csientry.get())
            auto_specs["Simple_Function"]["interval"] = fcsientry
            csientry.delete(0,"end")
            csientry.insert(0,f"{Succesfully_changed_to} {fcsientry}")
            app.after(2500, lambda: csientry.delete(0,"end"))
        except Exception:
            if csientry.get()!="":
                csientry.delete(0,"end")
                csientry.insert(0,"FAIL")
                app.after(2500, lambda: csientry.delete(0,"end"))
        try:
            fcspientry = int(cspientry.get())
            auto_specs["Simple_Function"]["clicks"] = fcspientry
            cspientry.delete(0,"end")
            cspientry.insert(0,f"{Succesfully_changed_to} {fcspientry}")
            app.after(2500, lambda: cspientry.delete(0,"end"))
        except Exception:
            if cspientry.get()!="":
                cspientry.delete(0,"end")
                cspientry.insert(0,"FAIL")
                app.after(2500, lambda: cspientry.delete(0,"end"))
        try:
            fcsdentry = float(csdentry.get())
            auto_specs["Simple_Function"]["duration"] = fcsdentry
            csdentry.delete(0,"end")
            csdentry.insert(0,f"{Succesfully_changed_to} {fcsdentry}")
            app.after(2500, lambda: csdentry.delete(0,"end"))
        except Exception:
            if csdentry.get()!="":
                csdentry.delete(0,"end")
                csdentry.insert(0,"FAIL")
                app.after(2500, lambda: csdentry.delete(0,"end"))
        try:
            fcsrentry = int(csrentry.get())
            auto_specs["Simple_Function"]["repeat"] = fcsrentry
            csrentry.delete(0,"end")
            csrentry.insert(0,f"{Succesfully_changed_to} {fcsrentry}")
            app.after(2500, lambda: csrentry.delete(0,"end"))
        except Exception:
            if csrentry.get()!="":
                csrentry.delete(0,"end")
                csrentry.insert(0,"FAIL")
                app.after(2500, lambda: csrentry.delete(0,"end"))
        
        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)

    def GEOMETRY():
        try:
            app.geometry(othergeometryEntry.get())
            ooo = othergeometryEntry.get()
            auto_specs["standart_geometry"] = ooo
            othergeometryEntry.delete(0,"end")
            othergeometryEntry.insert(0,f"{Succesfully_changed_to} {ooo}")
            app.after(2500, lambda: othergeometryEntry.delete(0,"end"))
        except Exception:
            othergeometryEntry.delete(0,"end")
            othergeometryEntry.insert(0,"FAIL")
            app.after(2500, lambda: othergeometryEntry.delete(0,"end"))
        
        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)

    def TOPMOST():
        app.attributes('-topmost', othertopmost_check_var.get())
        auto_specs["topmost"] = othertopmost_check_var.get()

        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)

    def THEME(choice):
        if Language==1:
            if choice=="Dark":
                auto_specs["theme"] = "dark"
                set_appearance_mode(theme)
            elif choice=="Light":
                auto_specs["theme"] = "light"
                set_appearance_mode(theme)
            else:
                auto_specs["theme"] = "system"
                set_appearance_mode(theme)
        elif Language==2:
            if choice=="Тёмная":
                auto_specs["theme"] = "dark"
                set_appearance_mode(theme)
            elif choice=="Светлая":
                auto_specs["theme"] = "light"
                set_appearance_mode(theme)
            else:
                auto_specs["theme"] = "system"
                set_appearance_mode(theme)
        elif Language==3:
            if choice=="Tamsioji":
                auto_specs["theme"] = "dark"
                set_appearance_mode(theme)
            elif choice=="Šviesos":
                auto_specs["theme"] = "light"
                set_appearance_mode(theme)
            else:
                auto_specs["theme"] = "system"
                set_appearance_mode(theme)

        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)
        RESTART()

    def LANGUAGE(choice):
        if choice=="English":
            auto_specs["Language"] = 1
        elif choice=="Русский":
            auto_specs["Language"] = 2
        elif choice=="Lietuvių":
            auto_specs["Language"] = 3

        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)
        RESTART()

    def ALLOW_UPDATES():
        auto_specs["allow_updates"] = UDCheckB_check_var.get()

        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)

    def TOOLWINDOW():
        auto_specs["toolwindow"] = toolwindowCheckBox_check_var.get()
        app.attributes('-toolwindow',toolwindowCheckBox_check_var.get())

        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)

    def ALPHA(value):
        app.attributes('-alpha',value)
        auto_specs["alpha"] = value
        alphaLabel.configure(text=f"Opacity selection from 0 to 1 ({round(alpha,3)})")

        with open(get_config_path(),'w') as f:
            json_dump(auto_specs, f, indent=4)

    app = CTk()
    try:
        app.geometry(standart_geometry)
        app.title(Autoclicker)
        app.attributes('-toolwindow',toolwindow)
        app.attributes('-alpha',alpha)
        app.attributes('-topmost', topmost)
        app.iconbitmap(icon_path)
    except Exception as e:
        LogErr("!!!ERROR!!!\n", str(e), exc_info=True)

    set_appearance_mode(theme)

    UDCheckB_check_var = BooleanVar()

    if Version!=Version and allow_updates==True:

        def REDEEM():
            UpdateTopl.destroy()
            web_open("https://github.com/arturwo1/Autoclicker")

        def CANCEL():
            UpdateTopl.destroy()

        UpdateTopl = CTkToplevel(app)
        UpdateTopl.geometry("365x225")
        UpdateTopl.title(update)
        UpdateTopl.attributes('-topmost', True)
        UpdateTopl.iconbitmap(icon_path)
        UpdateTopl.protocol("WM_DELETE_WINDOW", True)
        UpdateTopl.grab_set()
        UpdateTopl.transient(app)
        UpdateTopl.resizable(False,False)
        UpdateTopl.attributes('-alpha',alpha)
        UpdateTopl.attributes('-toolwindow',True)

        ULabel = CTkLabel(master=UpdateTopl, text=confirm_to_update, wraplength=350)
        ULabel.place(x=0,y=0,relheight=0.6,relwidth=1)

        URButton = CTkButton(master=UpdateTopl, text=Redeem,fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),command=REDEEM)
        URButton.place(x=0,y=0,relheight=0.2,relwidth=0.45, relx=0.025,rely=0.6)

        UCButton = CTkButton(master=UpdateTopl, text=Cancel,fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),command=CANCEL)
        UCButton.place(x=0,y=0,relheight=0.2,relwidth=0.45, relx=0.52,rely=0.6)

        UDCheckB = CTkCheckBox(master=UpdateTopl,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),text=See_Updates,variable=UDCheckB_check_var,command=ALLOW_UPDATES)
        UDCheckB.place(x=0,y=0,relheight=0.2,relwidth=0.95, relx=0.025,rely=0.8)
        UDCheckB_check_var.set(allow_updates)

    #Tab
    tabview = CTkTabview(master=app,height=470,width=350)
    tabview.place(x=0,y=0,relheight=0.9,relwidth=0.9,relx=0.05,rely=0.05)

    #Other tabs creation
    tabs = {Settings:1, ChangeLogs:2, Credits:3, Other:4}
    for tab in tabs:
        tabview.add(tab)

    #Settings
    settingsframe = CTkFrame(master=tabview.tab(Settings),border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None))
    settingsframe.place(x=0,y=0,relheight=0.9,relwidth=0.9,relx=0.05,rely=0.05)

    #Frames
    cliksframe = CTkFrame(master=settingsframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    cliksframe.place(x=0,y=0,relheight=0.35,relwidth=0.9,relx=0.05,rely=0.05)

    keybindsframe = CTkFrame(master=settingsframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    keybindsframe.place(x=0,y=0,relheight=0.35,relwidth=0.9,relx=0.05,rely=0.59)

    #ClicksFrame
    csframe = CTkFrame(master=cliksframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    csframe.place(x=0,y=0,relheight=0.35,relwidth=0.9,relx=0.05,rely=0.15)

    csilabel = CTkLabel(master=settingsframe,fg_color="transparent",text=Click_interval,text_color="gray")
    csilabel.place(x=0,y=0,relheight=0.1,relwidth=0.2,relx=0.11,rely=0.0425)

    csientry = CTkEntry(master=csframe,fg_color="transparent",placeholder_text=f"{Click_interval} ({Simple_interval})",placeholder_text_color="darkgray",text_color=("white" if theme=="dark" else "black" if theme=="light" else None))
    csientry.place(x=0,y=0,relheight=0.5,relwidth=0.265,relx=0.01,rely=0.3)

    csilabel_s = CTkLabel(master=csframe,fg_color="transparent",text="s")
    csilabel_s.place(x=0,y=0,relheight=0.5,relwidth=0.02,relx=0.275,rely=0.3)

    cspilabel = CTkLabel(master=settingsframe,fg_color="transparent",text=Clicks_per_interval,text_color="gray")
    cspilabel.place(x=0,y=0,relheight=0.1,relwidth=0.3,relx=0.36,rely=0.0425)

    cspientry = CTkEntry(master=csframe,fg_color="transparent",placeholder_text=f"{Clicks_per_interval} ({Simple_clicks})",placeholder_text_color="darkgray",text_color=("white" if theme=="dark" else "black" if theme=="light" else None))
    cspientry.place(x=0,y=0,relheight=0.5,relwidth=0.355,relx=0.3325,rely=0.3)

    csdlabel = CTkLabel(master=settingsframe,fg_color="transparent",text=Duration,text_color="gray")
    csdlabel.place(x=0,y=0,relheight=0.1,relwidth=0.2,relx=0.69,rely=0.0425)

    csdentry = CTkEntry(master=csframe,fg_color="transparent",placeholder_text=f"{Duration} ({Simple_duration})",placeholder_text_color="darkgray",text_color=("white" if theme=="dark" else "black" if theme=="light" else None))
    csdentry.place(x=0,y=0,relheight=0.5,relwidth=0.265,relx=0.7,rely=0.3)

    csdlabel_s = CTkLabel(master=csframe,fg_color="transparent",text="s")
    csdlabel_s.place(x=0,y=0,relheight=0.5,relwidth=0.02,relx=0.97,rely=0.3)

    #ClickOptionButton
    csobutton = CTkButton(master=cliksframe,text=f"{Click_button} ({Simple_button})",fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),text_color=(None if theme=="dark" else "black" if theme=="light" else None))
    csobutton.place(x=0,y=0,relheight=0.35,relwidth=0.44,relx=0.051,rely=0.59)

    #ClicksRepeatFrame
    csrframe = CTkFrame(master=cliksframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    csrframe.place(x=0,y=0,relheight=0.35,relwidth=0.44,relx=0.51,rely=0.59)

    csrlabel = CTkLabel(master=settingsframe,fg_color="transparent",text=Clicks_repeat,text_color="gray")
    csrlabel.place(x=0,y=0,relheight=0.06,relwidth=0.2,relx=0.6,rely=0.22)

    csrentry = CTkEntry(master=csrframe,fg_color="transparent",placeholder_text=f"{Clicks_repeat} ({Simple_repeat}) {times}",placeholder_text_color="darkgray",text_color=("white" if theme=="dark" else "black" if theme=="light" else None))
    csrentry.place(x=0,y=0,relheight=0.6,relwidth=0.96,relx=0.02175,rely=0.2)

    #StartKeybindButton
    startkbutton = CTkButton(master=keybindsframe,text=f"{Start} ({Auto_Start})",fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),text_color=(None if theme=="dark" else "black" if theme=="light" else None))
    startkbutton.place(x=0,y=0,relheight=0.35,relwidth=0.45,relx=0.03,rely=0.1)

    #StopKeybindButton
    stopkbutton = CTkButton(master=keybindsframe,text=f"{Stop} ({Auto_Disable})",fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),text_color=(None if theme=="dark" else "black" if theme=="light" else None))
    stopkbutton.place(x=0,y=0,relheight=0.35,relwidth=0.45,relx=0.52,rely=0.1)

    #ExitKeybindButton
    startkbutton = CTkButton(master=keybindsframe,text=f"{Exit} ({Auto_Exit})",fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),text_color=(None if theme=="dark" else "black" if theme=="light" else None))
    startkbutton.place(x=0,y=0,relheight=0.35,relwidth=0.45,relx=0.03,rely=0.55)

    #FunctionsButton
    stopkbutton = CTkButton(master=keybindsframe,text=Simple_Functions if Function_Name=="Simple_Function" else Hard_Functions,fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),text_color=(None if theme=="dark" else "black" if theme=="light" else None))
    stopkbutton.place(x=0,y=0,relheight=0.35,relwidth=0.45,relx=0.52,rely=0.55)

    #ConfirmALL
    csobutton = CTkButton(master=settingsframe,text=Confirm_all,fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),font=CTkFont(family="Helvetica",size=14,weight="bold"),text_color=(None if theme=="dark" else "black" if theme=="light" else None),command=CONFIRM)
    csobutton.place(x=0,y=0,relheight=0.1,relwidth=0.9,relx=0.05,rely=0.45)


    #ChangeLogs
    clscrollframe = CTkScrollableFrame(master=tabview.tab(ChangeLogs),border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),orientation="vertical",scrollbar_button_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None))
    clscrollframe.place(x=0,y=0,relheight=0.9,relwidth=0.9,relx=0.05,rely=0.05)

    clframe = CTkFrame(master=clscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    clframe.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    cllabel = CTkLabel(master=clframe,fg_color="transparent",text=Future_Update,text_color="#4545b5", font=CTkFont(family="Helvetica",size=20,weight="bold"))
    cllabel.place(x=0,y=0,relheight=0.1,relwidth=0.6,relx=0.2,rely=0)

    cllabelversion = CTkLabel(master=clframe,fg_color="transparent",text="p-A 0.0.1",text_color="darkgray", font=CTkFont(family="Helvetica",size=10,weight="bold"))
    cllabelversion.place(x=0,y=0,relx=0.05,rely=0.1,relheight=0.06,relwidth=0.9)

    cllabel11 = CTkLabel(master=clframe,fg_color="transparent",text="- App added to GitHub.",text_color="gray",height=0,width=0)
    cllabel11.place(x=1,y=40)

    clframe2 = CTkFrame(master=clscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    clframe2.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    cllabelversion2 = CTkLabel(master=clframe2,fg_color="transparent",text="p-A 0.0.0",text_color="darkgray", font=CTkFont(family="Helvetica",size=10,weight="bold"))
    cllabelversion2.place(x=0,y=0,relx=0.05,rely=0.1,relheight=0.06,relwidth=0.9)

    cllabel2 = CTkLabel(master=clframe2,fg_color="transparent",text=Next_Update,text_color="#0ffbff", font=CTkFont(family="Helvetica",size=20,weight="bold"))
    cllabel2.place(x=0,y=0,relheight=0.1,relwidth=0.6,relx=0.2,rely=0)

    clframe3 = CTkFrame(master=clscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    clframe3.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    cllabel3 = CTkLabel(master=clframe3,fg_color="transparent",text=Current_Update,text_color="#00ff00", font=CTkFont(family="Helvetica",size=20,weight="bold"))
    cllabel3.place(x=0,y=0,relheight=0.1,relwidth=0.65,relx=0.17,rely=0)

    cllabelversion3 = CTkLabel(master=clframe3,fg_color="transparent",text=Version,text_color="darkgray", font=CTkFont(family="Helvetica",size=10,weight="bold"))
    cllabelversion3.place(x=0,y=0,relx=0.05,rely=0.1,relheight=0.06,relwidth=0.9)

    cllabel33 = CTkLabel(master=clframe3,fg_color="transparent",text="- App created.",text_color="gray",height=0,width=0)
    cllabel33.place(x=1,y=50)

    clframe4 = CTkFrame(master=clscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    clframe4.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    cllabel4 = CTkLabel(master=clframe4,fg_color="transparent",text=Past_Update,text_color="#ff0000", font=CTkFont(family="Helvetica",size=20,weight="bold"))
    cllabel4.place(x=0,y=0,relheight=0.1,relwidth=0.6,relx=0.2,rely=0)

    cllabelversion4 = CTkLabel(master=clframe4,fg_color="transparent",text="p-A 0.0.0",text_color="darkgray", font=CTkFont(family="Helvetica",size=10,weight="bold"))
    cllabelversion4.place(x=0,y=0,relx=0.05,rely=0.1,relheight=0.06,relwidth=0.9)

    clframe5 = CTkFrame(master=clscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    clframe5.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    cllabel5 = CTkLabel(master=clframe5,fg_color="transparent",text=Old_Update,text_color="#000000", font=CTkFont(family="Helvetica",size=20,weight="bold"))
    cllabel5.place(x=0,y=0,relheight=0.1,relwidth=0.6,relx=0.2,rely=0)

    cllabelversion5 = CTkLabel(master=clframe5,fg_color="transparent",text="p-A -0.0.0",text_color="darkgray", font=CTkFont(family="Helvetica",size=10,weight="bold"))
    cllabelversion5.place(x=0,y=0,relx=0.05,rely=0.1,relheight=0.06,relwidth=0.9)


    #Credits
    creditsscrollframe = CTkScrollableFrame(master=tabview.tab(Credits),border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),orientation="vertical",scrollbar_button_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None))
    creditsscrollframe.place(x=0,y=0,relheight=0.9,relwidth=0.9,relx=0.05,rely=0.05)

    cframediscord = CTkFrame(master=creditsscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    cframediscord.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    clabeldiscord = CTkLabel(master=cframediscord,fg_color="transparent",text="Discord",text_color="#5562f6", font=CTkFont(family="Helvetica",size=25,weight="bold"))
    clabeldiscord.place(x=0,y=0,relheight=0.1,relwidth=0.26,relx=0.36,rely=0)

    clabeldiscord1 = CTkLabel(master=cframediscord,fg_color="transparent",text="Made everything in app - arturwol - https://discord.gg/MXupeAApza",text_color="gray",font=CTkFont(size=14))
    clabeldiscord1.place(x=10,y=20)

    cframegithub = CTkFrame(master=creditsscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    cframegithub.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    clabelgithub = CTkLabel(master=cframegithub,fg_color="transparent",text="GitHub",text_color="#1c2128", font=CTkFont(family="Helvetica",size=25,weight="bold"))
    clabelgithub.place(x=0,y=0,relheight=0.1,relwidth=0.245,relx=0.37,rely=0)

    clabelgithub1 = CTkLabel(master=cframegithub,fg_color="transparent",text="Made everything in app - arturwo1 - https://github.com/arturwo1/Autoclicker",text_color="gray",font=CTkFont(size=14))
    clabelgithub1.place(x=10,y=20)

    cframeyoutube = CTkFrame(master=creditsscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    cframeyoutube.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    clabelyoutube = CTkLabel(master=cframeyoutube,fg_color="transparent",text="Youtube",text_color="#ff0000", font=CTkFont(family="Helvetica",size=25,weight="bold"))
    clabelyoutube.place(x=0,y=0,relheight=0.1,relwidth=0.285,relx=0.37,rely=0)

    clabelyoutube1 = CTkLabel(master=cframeyoutube,fg_color="transparent",text="Made everything in app - @arturwol - https://www.youtube.com/@arturwol",text_color="gray",font=CTkFont(size=14))
    clabelyoutube1.place(x=10,y=20)

    cframesteam = CTkFrame(master=creditsscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None))
    cframesteam.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)

    clabelsteam = CTkLabel(master=cframesteam,fg_color="transparent",text="Steam",text_color="#171d25", font=CTkFont(family="Helvetica",size=25,weight="bold"))
    clabelsteam.place(x=0,y=0,relheight=0.1,relwidth=0.23,relx=0.38,rely=0)

    clabelsteam1 = CTkLabel(master=cframesteam,fg_color="transparent",text="Made everything in app - arturwol - https://steamcommunity.com/id/arturwol",text_color="gray",font=CTkFont(size=14))
    clabelsteam1.place(x=10,y=20)


    #Other
    otherscrollframe = CTkScrollableFrame(master=tabview.tab(Other),border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),orientation="vertical",scrollbar_button_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None))
    otherscrollframe.place(x=0,y=0,relheight=0.9,relwidth=0.9,relx=0.05,rely=0.05)

    otherlanguageComboBox = CTkComboBox(master=otherscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),values=["English","Русский","Lietuvių"],command=LANGUAGE)
    otherlanguageComboBox.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)
    otherlanguageComboBox.set("English" if Language==1 else "Русский" if Language==2 else "Lietuvių")

    otherthemeComboBox = CTkComboBox(master=otherscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),fg_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),values=themes,command=THEME)
    otherthemeComboBox.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)
    otherthemeComboBox.set("Dark" if theme=="dark" and Language==1 else "Light" if theme=="light" and Language==1 else "System" if theme=="system" and Language==1 else "Тёмная" if theme=="dark" and Language==2 else "Светлая" if theme=="light" and Language==2 else "Системная" if theme=="system" and Language==2 else "Tamsioji" if theme=="dark" and Language==3 else "Šviesos" if theme=="light" and Language==3 else "Sisteminis")

    othertopmost_check_var = BooleanVar()
    othertopmostCheckBox = CTkCheckBox(master=otherscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),text=Top_most, font=CTkFont(size=16),variable=othertopmost_check_var,command=TOPMOST)
    othertopmostCheckBox.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)
    othertopmost_check_var.set(topmost)

    allow_updatesCheckBox = CTkCheckBox(master=otherscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),text=See_Updates, font=CTkFont(size=16),variable=UDCheckB_check_var,command=ALLOW_UPDATES)
    allow_updatesCheckBox.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)
    UDCheckB_check_var.set(allow_updates)

    toolwindowCheckBox_check_var = BooleanVar()
    toolwindowCheckBox = CTkCheckBox(master=otherscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else None),text=ToolWindow, font=CTkFont(size=16),variable=toolwindowCheckBox_check_var,command=TOOLWINDOW)
    toolwindowCheckBox.pack(fill="x",anchor="w",expand=True,padx=10,pady=10)
    toolwindowCheckBox_check_var.set(toolwindow)

    alphaLabel = CTkLabel(master=otherscrollframe,text=AlphaDescription)
    alphaLabel.pack(fill="x",anchor="w",expand=True,padx=10,pady=(10,0))

    alphaSlider = CTkSlider(master=otherscrollframe,border_width=1,border_color=("#282424" if theme=="dark" else "#ebebeb" if theme=="light" else 'transparent'),button_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),button_hover_color=("white" if theme=="dark" else "black" if theme=="light" else "red"),progress_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),from_=0,to=1,number_of_steps=1e100,command=ALPHA)
    alphaSlider.pack(fill="x",anchor="w",expand=True,padx=10,pady=(0,10))
    alphaSlider.set(alpha)

    othergeometryEntry = CTkEntry(master=otherscrollframe,fg_color="transparent",placeholder_text=f"{geometry} {standart_geometry}",placeholder_text_color="darkgray",text_color=("white" if theme=="dark" else "black" if theme=="light" else None))
    othergeometryEntry.pack(fill="x",anchor="w",expand=True,padx=10,pady=(10,0))

    othergeometrybutton = CTkButton(master=otherscrollframe,text=Confirm,fg_color=("#333333" if theme=="dark" else "#979da2" if theme=="light" else None),hover_color=("#2b2b2b" if theme=="dark" else "#dbdbdb" if theme=="light" else None),font=CTkFont(family="Helvetica",size=14,weight="bold"),text_color=(None if theme=="dark" else "black" if theme=="light" else None),command=GEOMETRY)
    othergeometrybutton.pack(fill="x",anchor="w",expand=True,padx=10,pady=(0,10))

    app.mainloop()
    
if __name__ == '__main__':
    App()