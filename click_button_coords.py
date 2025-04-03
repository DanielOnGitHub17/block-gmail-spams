"""Script to loop all button clicks using coordinates with a GUI interface"""
import json
import os
import pyautogui
import tkinter as tk
from tkinter import ttk, messagebox
import threading


class GmailSpamBlocker:
    """Class to handle Gmail spam blocking using coordinates"""
    
    # Class variable to store coordinates
    _coords = None
    
    @staticmethod
    def _load_coordinates():
        """Load button coordinates from JSON file"""
        coords_file = os.path.join("assets", "coords.json")
        try:
            with open(coords_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Coordinates file not found: {coords_file}. "
                "Please run get_button_coords.py first to record button positions."
            )
    
    @staticmethod
    def click_next():
        """Function to click next button"""
        GmailSpamBlocker.click_button("next")
    
    @staticmethod
    def click_menu():
        """Function to click menu button"""
        GmailSpamBlocker.click_button("menu")
    
    @staticmethod
    def click_block():
        """Function to click block button"""
        GmailSpamBlocker.click_button("block")
    
    @staticmethod
    def click_block_confirm():
        """Function to click block confirm button"""
        GmailSpamBlocker.click_button("block_confirm")
    
    @staticmethod
    def click_button(button_name, duration=0.5):
        """Function to click a button using saved coordinates"""
        # Ensure coordinates are loaded
        if GmailSpamBlocker._coords is None:
            GmailSpamBlocker._coords = GmailSpamBlocker._load_coordinates()
            
        if button_name not in GmailSpamBlocker._coords:
            print(f"Error: Coordinates for {button_name} not found")
            return False
        
        try:
            x, y = GmailSpamBlocker._coords[button_name]
            pyautogui.moveTo(x, y, duration=duration)
            pyautogui.click(interval=0.1)
            return True
        except Exception as e:
            print(f"Error clicking {button_name}: {str(e)}")
            return False


class BlockGmailSpamsApp:
    """GUI Application for blocking Gmail spam using coordinates"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gmail Spam Blocker (Coordinates)")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
        # Initialize coordinates if not already loaded
        if GmailSpamBlocker._coords is None:
            try:
                GmailSpamBlocker._coords = GmailSpamBlocker._load_coordinates()
            except FileNotFoundError as e:
                messagebox.showerror("Error", str(e))
                self.root.after(100, self.root.destroy)
                return
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Instructions
        ttk.Label(
            main_frame, 
            text="Please open the spam gmails window/tab first",
            wraplength=350,
            font=("Arial", 10, "bold")
        ).pack(pady=(0, 15))
        
        # Input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Number of spam emails:").pack(side=tk.LEFT, padx=5)
        
        self.spam_count = tk.StringVar(value="10")
        ttk.Entry(input_frame, textvariable=self.spam_count, width=10).pack(side=tk.LEFT, padx=5)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=15)
        
        self.start_button = ttk.Button(button_frame, text="Start Blocking", command=self.start_process)
        self.start_button.pack(padx=5)
        
        # Progress frame
        progress_frame = ttk.Frame(main_frame)
        progress_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(progress_frame, text="Progress:").pack(anchor=tk.W)
        
        self.progress = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=350, mode="determinate")
        self.progress.pack(fill=tk.X, pady=5)
        
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(progress_frame, textvariable=self.status_var)
        self.status_label.pack(anchor=tk.W)
        
        # Is process running flag
        self.is_running = False

    def start_process(self):
        """Start the blocking process in a separate thread"""
        try:
            count = int(self.spam_count.get())
            if count <= 0:
                messagebox.showerror("Invalid Input", "Please enter a positive number")
                return
                
            if self.is_running:
                return
                
            self.is_running = True
            self.start_button.configure(state=tk.DISABLED)
            self.progress["maximum"] = count
            self.progress["value"] = 0
            self.status_var.set("Starting...")
            
            # Run in thread to keep GUI responsive
            threading.Thread(target=self.run_delete_spams, args=(count,), daemon=True).start()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    
    def run_delete_spams(self, count):
        """Run the delete_spams function with progress updates"""
        try:
            for i in range(count):
                if i:
                    self.status_var.set(f"Processing email {i+1}/{count} - clicking next")
                    GmailSpamBlocker.click_next()
                else:
                    self.status_var.set(f"Processing email {i+1}/{count}")
                
                self.status_var.set(f"Processing email {i+1}/{count} - clicking menu")
                GmailSpamBlocker.click_menu()
                
                self.status_var.set(f"Processing email {i+1}/{count} - clicking block")
                GmailSpamBlocker.click_block()
                
                self.status_var.set(f"Processing email {i+1}/{count} - confirming")
                GmailSpamBlocker.click_block_confirm()
                
                pyautogui.moveTo(10, 10, duration=0.5)
                
                # Update progress bar
                self.progress["value"] = i + 1
                self.root.update_idletasks()
            
            self.status_var.set("Completed!")
            messagebox.showinfo("Success", f"Successfully blocked {count} spam emails")
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.is_running = False
            self.start_button.configure(state=tk.NORMAL)


def main():
    """Initialize and run the GUI application"""
    root = tk.Tk()
    app = BlockGmailSpamsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
