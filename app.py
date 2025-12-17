import streamlit as st


def calculate_grade(percentage: float) -> str:
	"""Return a letter grade based on percentage."""
	if percentage >= 90:
		return "A+"
	if percentage >= 80:
		return "A"
	if percentage >= 70:
		return "B"
	if percentage >= 60:
		return "C"
	if percentage >= 50:
		return "D"
	return "F"


def main() -> None:
	st.set_page_config(page_title="Marks to Percentage & Grade", page_icon="🎓")
	st.title("Student Percentage & Grade Calculator 🎓")

	with st.sidebar:
		st.header("Options")
		student_name = st.text_input("Student name (optional)")
		num_subjects = st.number_input("Number of subjects", min_value=1, max_value=50, value=5, step=1)
		max_marks = st.number_input("Max marks per subject", min_value=1, value=100, step=1)

	st.write("---")

	st.markdown("### Enter marks for each subject")

	# Collect marks
	marks = []
	cols = st.columns(3)
	for i in range(int(num_subjects)):
		col = cols[i % 3]
		with col:
			mark = st.number_input(f"Subject {i+1}", min_value=0.0, max_value=float(max_marks), value=0.0, step=1.0, key=f"m{i}")
			marks.append(float(mark))

	if st.button("Calculate"):
		total_obtained = sum(marks)
		total_max = float(num_subjects) * float(max_marks)

		if any(m < 0 or m > max_marks for m in marks):
			st.error("Please ensure all marks are between 0 and the maximum marks per subject.")
			return

		percentage = (total_obtained / total_max) * 100 if total_max > 0 else 0.0
		grade = calculate_grade(percentage)

		st.success("Results")
		st.write(f"**Student:** {student_name or '—'}")
		st.write(f"**Total Obtained:** {total_obtained:.2f} / {total_max:.2f}")
		st.write(f"**Percentage:** {percentage:.2f}%")
		st.write(f"**Grade:** {grade}")

		st.progress(min(max(int(percentage), 0), 100))

		# Helpful tip
		st.info("Tip: Change the number of subjects or max marks in the sidebar and re-enter marks to recalculate.")


if __name__ == "__main__":
	main()

