import reflex as rx

def footer():
    return rx.flex(
        rx.hstack(
            rx.link(
                rx.avatar(src="/github.png", radius="full"),
                href="https://github.com/JorgeValdes",
                target="_blank",
            ),
            rx.link(
                rx.avatar(src="/linkedIn.png", radius="full"),
                href="https://www.linkedin.com/in/luccapsaila/",
                target="_blank",
            ),
            rx.link(
                rx.avatar(src="/gmail.png", radius="full"),
                href="mailto:lucca12vp@gmail.com",
                target="_blank",
            ),
            rx.link(
                rx.avatar(src="/instagram.png", radius="full"),
                href="https://www.instagram.com/jorge_ignacio_valdes/",
                target="_blank",
            ),
            
            rx.link(
                rx.avatar(src="/youtube.png", radius="full"),
                href="https://www.youtube.com/channel/UCW3OryKy9zF-9qylG6bo3Kw",
                target="_blank",
            ),
        ),
        bottom="0px",
        padding="1em",
        height="6em",
        width="100%",
        justify="center",
        align="center",
        #bg="orange",
    )