"""Script to loop all button clicks with a GUI interface"""
import pyautogui
import tkinter as tk
from tkinter import ttk, messagebox
import threading


class BlockGmailSpamsApp:
    """GUI Application for blocking Gmail spam"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Gmail Spam Blocker")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
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
                    self.click_next()
                else:
                    self.status_var.set(f"Processing email {i+1}/{count}")
                
                self.status_var.set(f"Processing email {i+1}/{count} - clicking menu")
                self.click_menu()
                
                self.status_var.set(f"Processing email {i+1}/{count} - clicking block")
                self.click_block()
                
                self.status_var.set(f"Processing email {i+1}/{count} - confirming")
                self.click_block_confirm()
                
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
    
    @staticmethod
    def click_next():
        """Function to click next button"""
        BlockGmailSpamsApp.click_button("next")

    @staticmethod
    def click_menu():
        """Function to click menu button"""
        BlockGmailSpamsApp.click_button("menu")

    @staticmethod
    def click_block():
        """Function to click block button"""
        BlockGmailSpamsApp.click_button("block")

    @staticmethod
    def click_block_confirm():
        """Function to click block confirm button"""
        BlockGmailSpamsApp.click_button("block_confirm")

    @staticmethod
    def click_button(button_name, ext="png", duration=0.5):
        """Function to click a button given image name"""
        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            try:
                pyautogui.moveTo(f"assets/{button_name}_button.{ext}", duration=duration)
                pyautogui.click(interval=0.1)
                return True
            except pyautogui.ImageNotFoundException:
                print(f"Attempt {attempts+1}: Could not find {button_name} button image")
                attempts += 1
        
        # If we get here, all attempts failed
        raise Exception(f"Could not find {button_name} button after {max_attempts} attempts")


def main():
    """Initialize and run the GUI application"""
    root = tk.Tk()
    app = BlockGmailSpamsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
