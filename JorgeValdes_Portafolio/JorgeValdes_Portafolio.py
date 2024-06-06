"""Welcome to Reflex! This file outlines the steps to create a basic app."""

#from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
#filename = f"{config.app_name}/{config.app_name}.py"
youtube = "https://www.youtube.com/?tab=w1&gl=CL"


#class State(rx.State):
#    """The app state."""

class State(rx.State):
    count: int = 10

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

        
#codiogo de muestra template del proyecto
# def index() -> rx.Component:
#     return rx.center(
#         #rx.theme_panel(),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.heading("Como estan todos...", size="9"),
#             rx.heading("un gusto conocerlos", size="9"),
#             rx.heading("parce que ya no esta lento", size="9"),
#             #rx.text("Get started by editing ", rx.code(filename)),
#             rx.button(
#                 "Check out our docs!",
#                 on_click=lambda: rx.redirect(docs_url),
#                 size="4",
#             ),
#             rx.button(
#                 "siganme en youtube!",
#                 on_click=lambda: rx.redirect(youtube),
#                 size="4",
#             ),
#             rx.logo(),
#             align="center",
#             spacing="7",
#             font_size="2em",
#         ),
#         height="100vh",
#     )

def index():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="tomato",
            on_click=State.decrement,
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="teal",
            on_click=State.increment,
        ),
        spacing="9",
    )


app = rx.App()
app.add_page(index)
