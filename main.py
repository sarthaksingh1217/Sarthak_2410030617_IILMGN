import customtkinter as ctk
from tkinter import messagebox
import requests
from datetime import date
import database 
from dotenv import load_dotenv
import os

# Set the modern UI Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
load_dotenv()
# Your OpenWeatherMap API Key
API_KEY=os.getenv("API_KEY")

class SmartTransitApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SmartTransit - Reservation System")
        self.geometry("500x600")
        self.current_user = None
        self.show_login_screen()

    def clear_screen(self):
        """Deletes old screens before showing new ones."""
        for widget in self.winfo_children():
            widget.destroy()

    # --- SCREEN 1 & 2: AUTHENTICATION ---
    def show_login_screen(self):
        self.clear_screen()
        self.geometry("500x600")
        
        frame = ctk.CTkFrame(self)
        frame.pack(pady=50, padx=50, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="SmartTransit Login", font=("Roboto", 24, "bold")).pack(pady=30)
        
        self.email_entry = ctk.CTkEntry(frame, placeholder_text="Email", width=250)
        self.email_entry.pack(pady=10)
        
        self.password_entry = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=250)
        self.password_entry.pack(pady=10)
        
        ctk.CTkButton(frame, text="Login", command=self.attempt_login).pack(pady=20)
        ctk.CTkButton(frame, text="Create New Account", fg_color="transparent", 
                      border_width=1, text_color="white", command=self.show_register_screen).pack(pady=10)

    def show_register_screen(self):
        self.clear_screen()
        
        frame = ctk.CTkFrame(self)
        frame.pack(pady=50, padx=50, fill="both", expand=True)
        
        ctk.CTkLabel(frame, text="Create Account", font=("Roboto", 24, "bold")).pack(pady=20)
        
        self.reg_name = ctk.CTkEntry(frame, placeholder_text="Full Name", width=250)
        self.reg_name.pack(pady=10)
        
        self.reg_email = ctk.CTkEntry(frame, placeholder_text="Email", width=250)
        self.reg_email.pack(pady=10)
        
        self.reg_password = ctk.CTkEntry(frame, placeholder_text="Password", show="*", width=250)
        self.reg_password.pack(pady=10)
        
        self.reg_phone = ctk.CTkEntry(frame, placeholder_text="Phone Number", width=250)
        self.reg_phone.pack(pady=10)
        
        ctk.CTkButton(frame, text="Sign Up", command=self.attempt_register).pack(pady=20)
        ctk.CTkButton(frame, text="Back to Login", fg_color="transparent", 
                      border_width=1, text_color="white", command=self.show_login_screen).pack(pady=10)

    # --- SCREEN 3: THE MAIN DASHBOARD ---
    def show_dashboard(self):
        self.clear_screen()
        self.geometry("700x650") # Make the window wider for the dashboard
        
        ctk.CTkLabel(self, text=f"Welcome, {self.current_user['full_name']}!", font=("Roboto", 24, "bold")).pack(pady=20)

        # 1. Fetch cities from the database to populate dropdowns
        self.city_data = database.get_all_cities()
        self.city_names = [city['city_name'] for city in self.city_data]

        if not self.city_names:
            ctk.CTkLabel(self, text="Database empty! Please run the SQL inserts.").pack()
            return

        # 2. Build the Search Bar
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(search_frame, text="Leaving From:").grid(row=0, column=0, padx=10, pady=15)
        self.from_var = ctk.StringVar(value=self.city_names[0])
        ctk.CTkOptionMenu(search_frame, variable=self.from_var, values=self.city_names).grid(row=0, column=1, padx=10, pady=15)

        ctk.CTkLabel(search_frame, text="Going To:").grid(row=0, column=2, padx=10, pady=15)
        self.to_var = ctk.StringVar(value=self.city_names[1] if len(self.city_names) > 1 else self.city_names[0])
        ctk.CTkOptionMenu(search_frame, variable=self.to_var, values=self.city_names).grid(row=0, column=3, padx=10, pady=15)

        ctk.CTkButton(self, text="Search Available Routes", command=self.display_routes).pack(pady=15)

        # 3. Build the Results Area (Scrollable)
        self.results_frame = ctk.CTkScrollableFrame(self, width=600, height=300)
        self.results_frame.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkButton(self, text="Logout", fg_color="#C62828", hover_color="#b71c1c", command=self.show_login_screen).pack(pady=15)

    # --- CORE LOGIC FUNCTIONS ---
    def attempt_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        user = database.login_user(email, password)
        if user:
            self.current_user = user
            self.show_dashboard() # Move directly to dashboard on success!
        else:
            messagebox.showerror("Error", "Invalid Email or Password")

    def attempt_register(self):
        success = database.register_user(self.reg_name.get(), self.reg_email.get(), self.reg_password.get(), self.reg_phone.get())
        if success:
            messagebox.showinfo("Success", "Account created! You can now log in.")
            self.show_login_screen()
        else:
            messagebox.showerror("Error", "Registration failed.")

    def get_city_id_by_name(self, name):
        """Helper to translate the string 'Mumbai' into its database ID."""
        for city in self.city_data:
            if city['city_name'] == name:
                return city['city_id']
        return None

    def display_routes(self):
        # Clear old search results
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        from_city = self.from_var.get()
        to_city = self.to_var.get()

        if from_city == to_city:
            messagebox.showwarning("Invalid Selection", "Please select two different cities.")
            return

        from_id = self.get_city_id_by_name(from_city)
        to_id = self.get_city_id_by_name(to_city)

        # Query the database
        routes = database.search_routes(from_id, to_id)

        if not routes:
            ctk.CTkLabel(self.results_frame, text="No direct routes found for this selection.", text_color="gray").pack(pady=30)
            return

        # Display the found routes
        for r in routes:
            row_frame = ctk.CTkFrame(self.results_frame, fg_color="#2b2b2b")
            row_frame.pack(fill="x", pady=5, padx=5)

            route_info = f"🚆 {r['transport_type']}   |   Fare: ₹{r['price']}"
            ctk.CTkLabel(row_frame, text=route_info, font=("Roboto", 14)).pack(side="left", padx=15, pady=15)
            
            # The Book button passes the specific route details to the confirmation function
            ctk.CTkButton(row_frame, text="Book Ticket", width=120, fg_color="#2E7D32", hover_color="#1B5E20",
                          command=lambda route_id=r['route_id'], dest=to_city: self.confirm_booking(route_id, dest)).pack(side="right", padx=15, pady=15)

    def confirm_booking(self, route_id, destination_city):
        """Fetches live weather and asks the user for final confirmation."""
        weather_text = "Fetching live weather..."
        
        # 1. API Call to OpenWeatherMap
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={destination_city}&appid={API_KEY}&units=metric"
            response = requests.get(url).json()
            
            if response.get("cod") == 200:
                temp = response['main']['temp']
                desc = response['weather'][0]['description']
                weather_text = f"{temp}°C, {desc.capitalize()}"
            else:
                weather_text = "Weather data unavailable right now."
        except:
            weather_text = "Connection error while fetching weather."

        # 2. Show the Smart Pop-up
        confirmation_message = (
            f"You are about to book a ticket to {destination_city}.\n\n"
            f"🌤️ Live Destination Weather:\n{weather_text}\n\n"
            f"Do you want to confirm this booking?"
        )
        
        confirm = messagebox.askyesno("Confirm Your Journey", confirmation_message)

        # 3. Write to Database
        if confirm:
            today_date = date.today().strftime("%Y-%m-%d")
            success = database.create_booking(self.current_user['user_id'], route_id, today_date)
            
            if success:
                messagebox.showinfo("Ticket Confirmed", "Your booking has been saved to the database successfully!")
            else:
                messagebox.showerror("Database Error", "Failed to secure the booking.")

# Run the app
if __name__ == "__main__":
    app = SmartTransitApp()
    app.mainloop()