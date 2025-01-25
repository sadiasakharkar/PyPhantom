from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10
        self.build_ui()

    def build_ui(self):
        # Add gradient background
        with self.canvas.before:
            Color(0.0, 0.0, 0.2, 1)  # Start color
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Title
        self.add_widget(Label(
            text="✨ Evento Login ✨",
            font_size=28,
            color=(1, 1, 1, 1),  # White text
            bold=True,
            halign="center"
        ))

        # Email/Username Input
        self.add_widget(Label(text="📧 Enter Email/Username", color=(1, 1, 1, 1)))
        self.email_input = TextInput(hint_text="Enter your email", multiline=False, background_color=(0.1, 0.1, 0.4, 1))
        self.add_widget(self.email_input)

        # Password Input
        self.add_widget(Label(text="🔑 Enter Password", color=(1, 1, 1, 1)))
        self.password_input = TextInput(hint_text="Enter your password", multiline=False, password=True, background_color=(0.1, 0.1, 0.4, 1))
        self.add_widget(self.password_input)

        # Role Selection Dropdown
        self.add_widget(Label(text="🛠 Select Role", color=(1, 1, 1, 1)))
        self.role_spinner = Spinner(
            text="Student",
            values=("University Admin", "Faculty", "Event Manager", "Coordinator", "Student"),
            background_color=(0.1, 0.1, 0.4, 1),
            color=(1, 1, 1, 1),
        )
        self.add_widget(self.role_spinner)

        # Login Button
        self.login_button = Button(
            text="Login 🚀",
            size_hint=(1, 0.5),
            background_color=(0.2, 0.5, 0.8, 1),
            bold=True,
        )
        self.login_button.bind(on_press=self.handle_login)
        self.add_widget(self.login_button)

        # Forgot Password Link
        self.forgot_password_button = Button(
            text="Forgot Password? 🔒",
            size_hint=(1, 0.3),
            background_color=(0, 0, 0, 0),
            color=(0.2, 0.6, 1, 1)
        )
        self.forgot_password_button.bind(on_press=self.handle_forgot_password)
        self.add_widget(self.forgot_password_button)

        # Create Account Link
        self.create_account_button = Button(
            text="Create Account 📝",
            size_hint=(1, 0.3),
            background_color=(0, 0, 0, 0),
            color=(0.2, 0.6, 1, 1)
        )
        self.create_account_button.bind(on_press=self.handle_create_account)
        self.add_widget(self.create_account_button)

    def handle_login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        role = self.role_spinner.text

        # Validate input
        if not email or not password:
            self.show_popup("Error", "Please fill in all fields!")
        elif "@" not in email:
            self.show_popup("Error", "Invalid email format!")
        else:
            self.show_popup("Login Successful", f"Welcome, {role}!")
            Clock.schedule_once(lambda dt: self.clear_inputs(), 2)

    def handle_forgot_password(self, instance):
        self.show_popup("Forgot Password", "Please contact support for password recovery.")

    def handle_create_account(self, instance):
        self.show_popup("Create Account", "Redirecting to account creation...")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message, halign="center"))
        popup_close = Button(text="Close", size_hint=(1, 0.3))
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.5))
        popup_close.bind(on_press=popup.dismiss)
        popup_layout.add_widget(popup_close)
        popup.open()

    def clear_inputs(self):
        self.email_input.text = ""
        self.password_input.text = ""

    def update_bg(self, instance, value):
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos


class InteractiveLoginApp(App):
    def build(self):
        self.title = "Interactive Login App"
        return LoginPage()


if __name__ == "__main__":
    InteractiveLoginApp().run()
