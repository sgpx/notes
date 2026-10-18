import os, time
from datetime import datetime
import llm

# Define constants
BASE_SCORE = 10
DECAY = 0.9

# Recency factor based on days since last practice
def get_recency_factor(last_practice_days):
    if last_practice_days <= 1:
        return 1.2
    elif 2 <= last_practice_days <= 3:
        return 1.0
    else:
        return 0.5

# Consistency multiplier based on the number of practice days in a week
def get_consistency_multiplier(practice_days_per_week):
    if practice_days_per_week >= 7:
        return 1.5
    elif 4 <= practice_days_per_week <= 6:
        return 1.2
    else:
        return 0.8

# Calculate Total Practice Score (TPS)
def calculate_tps(program_dates):
    total_score = 0
    today = datetime.now()

    for program_date in program_dates:
        days_old = (today - program_date).days
        total_score += BASE_SCORE * (DECAY ** days_old)

    return total_score

# Main function to calculate Learning Progress Score (LPS)
def calculate_lps(program_dates, last_practice_date, practice_days_per_week):
    # Calculate Total Practice Score (TPS)
    tps = calculate_tps(program_dates)

    # Calculate Recency Factor (RF)
    last_practice_days = (datetime.now() - last_practice_date).days
    rf = get_recency_factor(last_practice_days)

    # Calculate Consistency Multiplier (CM)
    cm = get_consistency_multiplier(practice_days_per_week)

    # Calculate LPS
    lps = tps * rf * cm
    return lps

# Function to get all .cpp files in the current directory and the most recent practice date
def get_cpp_files_and_dates():
    cpp_files = []
    most_recent_time = None
    txt = ""

    for filename in os.listdir('.'):
        if filename.endswith('.cpp'):
            file_path = os.path.join('.', filename)
            file_stat = os.stat(file_path)
            file_date = datetime.fromtimestamp(file_stat.st_mtime)
            cpp_files.append(file_date)
            txt += f"// {file_path} created at :  {file_date}\n{open(filename,'r').read()}\n\n"

            # Track the most recent modification time (latest practice)
            if most_recent_time is None or file_date > most_recent_time:
                most_recent_time = file_date

    return cpp_files, most_recent_time, txt

# Function to get a list of repetitive programs to practice based on LLM analysis
def get_repetitive_programs(lps, cpp_files_dates, txt):
    # Prepare a list of program filenames and their modification dates
    program_list = ""
    for date in cpp_files_dates:
        program_list += f"Last modified on {date.strftime('%Y-%m-%d %H:%M:%S')}\n"
    
    # Generate the LLM prompt based on the learning progress score and the C++ program list
    formula = """
Look at this formula that gauges the learning progress of a kinetic learner practicing C++, we can consider a few key factors:

1. **Number of Programs Written**: More programs indicate more practice.
2. **Recency of Practice**: More recent practice is typically more beneficial than older practice.
3. **Consistency**: Regular practice is better than intermittent practice.
4. **Quality of Practice**: We may also want to account for the complexity or quality of the programs written (if such data is available).

### Proposed Formula:

Let's define a Learning Progress Score (LPS) using the following components:

1. **Total Practice Score (TPS)**: This will be a cumulative score based on the number of programs written and their age.

2. **Recency Factor (RF)**: To adjust the score based on when programs were written.

3. **Consistency Multiplier (CM)**: To encourage consistency in practice.

The formula can be constructed as follows:

[
LPS = TPS \\times RF \\times CM
]

### Components of the Formula

1. **Total Practice Score (TPS)**: Accumulate a score for each program written.
 - For each program written, assign a base score (e.g., `10 points`).
 - Apply a decay for older programs. For example, every day past the creation of the program, the score can decay based on a decay factor (e.g., `0.9`).

 \\[
 TPS = \\sum_{i=1}^{n} (Base\\_Score \\times Decay^{Days\\_Old(i)})
 \\]
 
 - Where \\(Days\\_Old(i)\\) is the number of days since the `i-th` program was created, and \\(Base\\_Score\\) is a constant score you assign.

2. **Recency Factor (RF)**: A multiplier based on the time since the last practice session, encouraging recent practice.
 - You could set a threshold, for example, if there's been no practice for more than a specific number of days.
 - Example:
 - If practiced in the last 1 day: `RF = 1.2`
 - If practiced in the last 2-3 days: `RF = 1.0`
 - If practiced more than 3 days ago: `RF = 0.5`

3. **Consistency Multiplier (CM)**: To emphasize regular, consistent practice over sporadic practice.
 - This can be calculated based on the number of practice sessions in a given time frame.
 - For example:
 - If practiced every day for a week: `CM = 1.5`
 - If practiced 4-6 times a week: `CM = 1.2`
 - If practiced less than 3 times a week: `CM = 0.8`

### Final Learning Progress Score Calculation

Putting it all together, the final formula would look like this:

\\[
LPS = \\left( \\sum_{i=1}^{n} (Base\\_Score \\times Decay^{Days\\_Old(i)}) \\right) \\times RF \\times CM
\\]


"""

    prompt = f"""
{formula}

    Based on the following information:
    - The learner's Learning Progress Score (LPS) is {lps:.2f}.
    - The learner has written the following C++ programs, listed by their last modification dates:
    {program_list}
    
    Suggest a list of relevant (ref. the current skill level or topic) but repetitive C++ practice problems to help improve the learner's skills. (at least 10)

These are the programs practiced by the student

{txt}
    """

    # Invoke the LLM with the prompt
    response = llm.invoke(prompt)

    # Print the LLM's suggestions
    ts = int(time.time())
    open(f"response-{ts}.txt","w").write(response)
    print(llm.invoke(f"structure all the programming tasks given (including optional programs) into 1 simple bullet point list. write the list and nothing else: \n\n{response}", model="gpt-4o-mini"))

# Main function to calculate the LPS from files in the current directory
def main():
    # Get all C++ program files in the current directory and the most recent practice date
    cpp_files_dates, last_practice_date, txt = get_cpp_files_and_dates()
    
    if not cpp_files_dates:
        print("No C++ files found in the current directory.")
        return

    # Calculate the practice days per week based on your own tracking or assumptions (for example purposes)
    practice_days_per_week = 5  # User practiced 5 days a week

    # If no files were found or no valid practice date exists, use the current date
    if not last_practice_date:
        last_practice_date = datetime.now()

    # Calculate the Learning Progress Score (LPS)
    lps = calculate_lps(cpp_files_dates, last_practice_date, practice_days_per_week)

    # Print the result
    print(f"Learning Progress Score (LPS): {lps:.2f}")

    # Get and print repetitive programs to practice based on LLM's analysis
    get_repetitive_programs(lps, cpp_files_dates, txt)

if __name__ == "__main__":
    main()
