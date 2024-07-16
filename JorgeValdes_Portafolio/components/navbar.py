import reflex as rx

def navbar():
    return rx.hstack(
        rx.hstack(
            rx.heading("Jorge Valdes Flores", font_size="min(5vw, 35px)"),
            marginRight="1em"
        ),
        rx.hstack(
            rx.link(
                "Inicio",
                href="/",
                color="black",
                marginRight="1em",
            ),
            rx.link(
                "Resumen",
                #href="https://www.google.com/search?q=google&rlz=1C1VDKB_esCL1084CL1084&oq=google&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhBFGDwyBggDEEUYQTIGCAQQRRg8MgYIBRBFGEEyBggGEEUYPDIGCAcQRRhB0gEHNjU3ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8",
                href="/resume",
                color="black",
                marginRight="1em",
            ),
            rx.link(
                "Proyectos",
                href="/projects",
                color="black",
                marginRight="1em",
            ),
            rx.menu.root(
                rx.menu.trigger(
                  
                ),
                rx.menu.content(
                    rx.menu.item(
                        rx.link(
                            "OrganizeAI",
                            href="/OrganizeAI",
                            color="black",
                            marginRight="1em",
                        ),
                    ),
                    rx.menu.item(
                        rx.link(
                            "QandA Market",
                            href="/QandAMarket",
                            color="black",
                            marginRight="1em",
                        ),
                    ),
                    rx.menu.item(
                        rx.link(
                            "ChatVac",
                            href="/ChatVac",
                            color="black",
                            marginRight="1em",
                        ),
                    ),
                    width="10rem",
                ),
            ), 
        ),
        position="fixed",
        top="0px",
        background_color="white",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
        align="center",
    )