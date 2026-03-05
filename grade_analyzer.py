#Name: BALAJI R
#Roll Number: 2602014 
#Assignment: Python: Functions & Modularity

# Mini Student Grade Analyzer

def process_scores(students):
    """Task 1: Calculate averages rounded to 2 decimal places."""
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages


def classify_grades(averages):
    """Task 2: Assign letter grades based on thresholds."""
    
    # Grade thresholds defined inside the function
    A_LIMIT = 90
    B_LIMIT = 75
    C_LIMIT = 60

    classified = {}
    
    for name, avg in averages.items():
        if avg >= A_LIMIT:
            grade = "A"
        elif avg >= B_LIMIT:
            grade = "B"
        elif avg >= C_LIMIT:
            grade = "C"
        else:
            grade = "F"
        
        classified[name] = (avg, grade)
    
    return classified


def generate_report(classified, passing_avg=60):
    """Task 3: Print formatted report and return number of students who passed."""
    
    print("===== Student Grade Report =====")
    
    passed_count = 0
    
    for name, (avg, grade) in sorted(classified.items()):
        status = "PASS" if avg >= passing_avg else "FAIL"
        
        if status == "PASS":
            passed_count += 1
        
        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")
    
    total_students = len(classified)
    
    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total_students - passed_count}")
    
    return passed_count


# ===== Main Program =====
if __name__ == "__main__":
    
    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 97, 97]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)