 
# import streamlit as st
# from models.user import User
# from models.note import Note
# from utils.auth import login
# from utils.payment import simulate_payment
# from utils.database import notes_db

# # ✅ Yeh pehli Streamlit command honi chahiye
# st.set_page_config(page_title="EduTrack - Student Performance Tracker", layout="centered")

# # 🔐 Simulate login
# current_user = login()

# st.title("📊 EduTrack - Student Performance Tracker")

# # -------------------------------
# # 👤 Sidebar - User Info
# # -------------------------------
# st.sidebar.title("👤 User Info")
# st.sidebar.write(f"Logged in as: {current_user.username} ({current_user.role})")
# st.sidebar.write(f"Status: {'Premium ✅' if current_user.is_premium else 'Free ❌'}")

# if not current_user.is_premium and st.sidebar.button("Upgrade to Premium (Rs. 500)"):
#     simulate_payment(current_user)
#     st.sidebar.success("You are now a Premium user! Refresh to see benefits.")

# # -------------------------------
# # 👩‍🏫 Teacher View
# # -------------------------------
# if current_user.role == "teacher":
#     st.subheader("✏️ Add Student Performance Note")
#     student_name = st.text_input("Student Name")
#     subject = st.selectbox("Subject", [
#         "Math", "English", "Science", "Urdu", "Social Studies",
#         "Biology", "Chemistry", "Physics", "Islamiat", "Other"
#     ])
#     note_text = st.text_area("Note")

#     if st.button("Save Note"):
#         # ✅ Note object properly created
#         note = Note(current_user.username, student_name, subject, note_text)
#         notes_db.append(note)
#         st.success("✅ Performance note added successfully!")

# # -------------------------------
# # 👨‍👩‍👧 Parent View
# # -------------------------------
# elif current_user.role == "parent":
#     st.subheader("📖 View Your Child's Performance Notes")
#     student_name = st.text_input("Enter Your Child's Name")

#     if student_name:
#         student_notes = [n for n in notes_db if n.student.lower() == student_name.lower()]

#         if student_notes:
#             for note in student_notes:
#                 st.markdown(f"**Subject:** {note.subject}")
#                 st.markdown(f"**Note by {note.teacher}:** {note.text}")
#                 st.markdown("---")

#             if current_user.is_premium:
#                 if st.button("Download Report (PDF)"):
#                     st.success("📄 PDF download feature coming soon!")
#         else:
#             st.warning("⚠️ No notes found for this student.")

# # -------------------------------
# # ❌ Unknown Role
# # -------------------------------
# else:
#     st.error("Unknown role. Please contact admin.")
import streamlit as st
from models.user import User
from models.note import Note
from utils.auth import login
from utils.payment import simulate_payment
from utils.database import notes_db, save_notes

st.set_page_config(page_title="EduTrack - Student Progress Tracker", layout="centered")

# Simulate login
current_user = login()

st.title("📊 EduTrack - Student Performance Tracker")

# Sidebar
st.sidebar.title("👤 User Info")
st.sidebar.write(f"Logged in as: {current_user.username} ({current_user.role})")
st.sidebar.write(f"Status: {'Premium ✅' if current_user.is_premium else 'Free ❌'}")

if not current_user.is_premium and st.sidebar.button("Upgrade to Premium (Rs. 500)"):
    simulate_payment(current_user)
    st.sidebar.success("You are now a Premium user!")

# Teacher View
if current_user.role == "teacher":
    st.subheader("✏️ Add Student Performance Note")
    student_name = st.text_input("Student Name")
    subject = st.selectbox("Subject", [
        "Math", "English", "Science", "Urdu", "Social Studies",
        "Biology", "Chemistry", "Physics", "Islamiat", "Other"
    ])
    note_text = st.text_area("Note")
    
    if st.button("Save Note"):
        note = Note(teacher=current_user.username, student=student_name, subject=subject, text=note_text)
        notes_db.append(note)
        save_notes(notes_db)
        st.success("✅ Performance note added successfully!")

# Parent View
elif current_user.role == "parent":
    st.subheader("📖 View Your Child's Performance Notes")
    student_name = st.text_input("Enter Your Child's Name")
    
    if student_name:
        student_notes = [n for n in notes_db if n.student.lower() == student_name.lower()]
        if student_notes:
            for note in student_notes:
                st.markdown(f"**Subject:** {note.subject}")
                st.markdown(f"**Note by {note.teacher}:** {note.text}")
                st.markdown("---")
            
            if current_user.is_premium:
                if st.button("Download Report (PDF)"):
                    st.success("📄 PDF download feature coming soon!")
        else:
            st.warning("No notes found for this student.")

else:
    st.error("Unknown role. Please contact admin.")
