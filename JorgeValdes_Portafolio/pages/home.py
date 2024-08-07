import reflex as rx
from ..template import template

@rx.page(route="/")
#template realiza el llamado a las paginas definidas de navbar y footer
@template
def home():
    return rx.box(
        rx.flex(
            rx.heading(
                "JORGE VALDES",
                font_size="min(9vw, 80px)",
                color="black",
                letterSpacing= "min(2.5vw, 40px)",
                fontWeight="500",
            ),
             rx.box(
                height="1em",
            ),
            rx.text(
                "Portafolio Personal",
                font_size="min(5.5vw, 40px)",
                color="black",
                letterSpacing= "min(2vw, 18px)",
                fontWeight="400",
            ),
            rx.box(
                height="1em"
            ),
            rx.chakra.image(
                src="/jorgevaldesbn.jpg",
                width="200px",
                height="200px",
                border_radius="full",
            ),
            direction="column",
            justify="center",
            align="center",
            width="100%",
            height="100%",
            paddingTop="50vh",
            #background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))",
            #background="black",
        ),
        background="center/cover url('/montain.jpg')",
        width="100%",
        height="100vh",
        #rx.logo()
    ),