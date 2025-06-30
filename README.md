# 🎯 Job Application Tracker
A sleek Flask web app to organize, monitor, and take control of your job search. Powered by an Excel backend, it’s lightweight and user-friendly.

---

## 🚀 Features
- 📊 Dashboard: See your application journey—Applied, Interviewing, Offer—at a glance.
- ➕ Add Applications: Log new opportunities with just ID, company, title, and status.
- ✏️ Edit Applications: Easily update details on the fly.
- 🗑️ Delete Applications: Clean up outdated entries with a click.
- 📋 List View: View all applications in a neat, sortable table.
- 🔍 Track by ID: Instantly fetch any entry using its Application ID.
- 👑 Admin Panel: Secure access to sensitive actions (default: admin / password).

---
## ⭐ Usage Flow
- Home (Dashboard) – Your project control center with instant status counts.
- Add – Submit new applications swiftly.
- List – Bulk view, edit entries, or purge unwanted ones.
- Track – Lookup specific applications by ID in one click.
- Admin Panel – Log in using admin / password to protect your data.

---

## 🔧 Dependencies
- Flask – Web framework
- pandas – Efficient data handling
- openpyxl – Excel read/write support  

---

## 🖼️ Screenshot

### Home Page
![Screenshot 2025-06-30 135922](https://github.com/user-attachments/assets/413c2f04-2047-45d2-9f77-973c2195e0d5)
 

### Admin Login

![Screenshot 2025-06-30 135953](https://github.com/user-attachments/assets/ba787899-ca68-4943-b0b7-564691908acc)


### Admin Logout

![Screenshot 2025-06-30 140210](https://github.com/user-attachments/assets/85b70a21-6f09-425a-8406-abbc1d4a9cd8)

### Track Application

![Screenshot 2025-06-30 140010](https://github.com/user-attachments/assets/5c216f9b-1dfa-4c0a-9623-8c01de3bf40a)


### Add New Application

![Screenshot 2025-06-30 140054](https://github.com/user-attachments/assets/73bfe27d-7ea7-488c-b1fc-fdbf56dd6a41)



### Application List

![Screenshot 2025-06-30 140136](https://github.com/user-attachments/assets/4e5160a5-2e8f-45b8-b858-bee53671df8c)



## 📁 File Structure
```
├── app.py                 # Main application
├── applications.xlsx      # Excel database
├── requirements.txt       # Required Python libraries
├── README.md              # Project documentation
├── templates/             # HTML view templates
│   ├── home.html
│   ├── add.html
│   ├── edit.html
│   ├── list.html
│   ├── track.html
    └── admin.html
```

---

## 📜 License
This project is MIT licensed—see the LICENSE file for details.
