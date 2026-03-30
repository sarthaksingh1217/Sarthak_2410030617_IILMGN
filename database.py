import mysql.connector
from mysql.connector import Error

def create_connection():
    """Creates and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="1234", # ⚠️ PUT YOUR PASSWORD HERE AGAIN
            database="SmartTransit"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def get_all_cities():
    """Fetches all cities for the UI dropdowns."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor(dictionary=True) # Returns data as a dictionary
        cursor.execute("SELECT city_id, city_name FROM Cities;")
        cities = cursor.fetchall()
        cursor.close()
        conn.close()
        return cities
    return []

def register_user(full_name, email, password, phone):
    """Inserts a new user into the database."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO Users (full_name, email, password_hash, phone) VALUES (%s, %s, %s, %s)"
            val = (full_name, email, password, phone) # In a real app, hash the password first!
            cursor.execute(sql, val)
            conn.commit()
            return True
        except Error as e:
            print(f"Registration Failed: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
    return False

def login_user(email, password):
    """Checks if email and password match."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM Users WHERE email = %s AND password_hash = %s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user # Returns user info if successful, None if failed
    return None

def search_routes(source_id, dest_id):
    """Finds available transit routes between two cities."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        # Using JOINs to get the actual city names alongside the route data
        sql = """
            SELECT r.route_id, s.city_name as source, d.city_name as dest, r.transport_type, r.price 
            FROM Routes r
            JOIN Cities s ON r.source_city_id = s.city_id
            JOIN Cities d ON r.dest_city_id = d.city_id
            WHERE r.source_city_id = %s AND r.dest_city_id = %s;
        """
        cursor.execute(sql, (source_id, dest_id))
        routes = cursor.fetchall()
        cursor.close()
        conn.close()
        return routes
    return []

def create_booking(user_id, route_id, travel_date):
    """Records a new ticket booking."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO Bookings (user_id, route_id, travel_date) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user_id, route_id, travel_date))
            conn.commit()
            return True
        except Error as e:
            print(f"Booking Failed: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
    return False