#amazon scraper
import customtkinter as ctk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import csv

# Initialize customtkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ScraperApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Amazon Scraper")
        self.geometry("500x300")
        
        # URL Input
        self.url_label = ctk.CTkLabel(self, text="Enter Amazon Product URL:")
        self.url_label.pack(pady=10)
        
        self.url_entry = ctk.CTkEntry(self, width=400)
        self.url_entry.pack(pady=5)
        
        # Scrape Button
        self.scrape_button = ctk.CTkButton(self, text="Scrape Data", command=self.scrape_data)
        self.scrape_button.pack(pady=20)
        
        # Status Label
        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=10)

    def scrape_data(self):
        url = self.url_entry.get()
        
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for request errors
            soup = BeautifulSoup(response.text, 'html.parser')
            
            data = []
            
            name = soup.select_one('#productTitle').text.strip()
            price = soup.select_one('.a-price-whole').text.strip()
            rating = soup.select_one('.a-size-base').text.strip()
            
            data.append({
                'Name': name,
                'Price': price,
                'Rating': rating
            })         
            # Save data to CSV
            self.save_to_csv(data)
            self.status_label.configure(text="Scraping completed and data saved to products.csv")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scrape data: {e}")
            self.status_label.configure(text="")

    def save_to_csv(self, data):
        with open('data//products.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Rating'])
            writer.writeheader()
            writer.writerows(data)
        messagebox.showinfo("Success", "Data successfully saved to products.csv")

if __name__ == "__main__":
    app = ScraperApp()
    app.mainloop()
