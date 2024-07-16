"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

#importacion de las paginas
from .pages.home import home
from .pages.resume import resume
#from .pages.footer import footer
#from .components.navbar import navbar

#docs_url = "https://reflex.dev/docs/getting-started/introduction/"
#filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""



        #rx.theme_panel(),
    """rx.theme(appearance="dark", has_background=True, radius="large", accent_color="teal"),
        rx.vstack(
            rx.heading("Jorge Valdes Flores", size="9",  aling="rigth", color_scheme="indigo"),
            rx.heading("Data Engineer", size="9"),
            rx.heading("Sobre mi", size="9"),
            #rx.text("Ingeniero Industrial", "element.", as_="p",),
                rx.text(
                "This is a ",
                #rx.text.strong("label"),
                " element.",
                #as_="label",
            ),
            #rx.code(filename)),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="2",
                aling="left"
            ),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),color_scheme="tomato",
                size="2",
            ),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="2",
            ),
            rx.logo(),
            align="center",
            spacing="6",
            font_size="2em",
        ),
        spacing="3",
        height="100vh",
        aling="left" """
    #)


app = rx.App()
#app.add_page(index, route="/")
app.add_page(home, route="/")
app.add_page(resume, route="/resume")
