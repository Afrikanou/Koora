from flet import *

def main(page:Page):
    page.title = "My Torch"
    page.scroll = "auto"
    page.window.top = 1
    page.window.left = 850
    page.window.width = 390
    page.window.height = 640
    page.bgcolor = "#CD9DFF"
    page.theme_mode = ThemeMode.LIGHT


    page.add(

        AppBar(
            title=Text('My Torch By Flet',size=14),
            bgcolor='#800080',
            color='white',
            actions=[
                IconButton(icons.SETTINGS,on_click=...)
            ]
        ),

        Row([
            Text('\nFlash Light App\n',size=31,color='black')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Image(src="torch.png",width=280)

        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text(' \n')
        ],alignment=MainAxisAlignment.CENTER),

        Row([

            ElevatedButton(
                "ON",
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor='#800080',
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),on_click=...
                
            )
            ,

            ElevatedButton(
                "OFF",
                width=100,
                icon=icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor='#800080',
                    color='white',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),on_click=...
                
            )

        ],alignment=MainAxisAlignment.CENTER),
    )

    page.update()
app(main)