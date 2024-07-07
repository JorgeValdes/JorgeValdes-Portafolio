import reflex as rx


def footer():
    return rx.box(
        rx.heading("hola comoe stan"),
        background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))",
        width="100%",
        height="100vh",
        #rx.logo()
    ),