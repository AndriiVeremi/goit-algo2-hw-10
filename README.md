# University Schedule Planner

A program to create a university class schedule using a greedy algorithm for the set cover problem.

## Task Description

The goal is to assign teachers to subjects, minimizing the number of teachers involved while ensuring all required subjects are covered.

The teacher selection algorithm at each step is as follows:
1.  Preference is given to the teacher who can cover the largest number of yet uncovered subjects.
2.  If there are multiple such candidates, the youngest one is chosen.

## Project Structure

-   `main.py`: The main file to run the program. It contains the data for subjects and teachers, calls the schedule creation function, and prints the result.
-   `models.py`: Defines the `Teacher` class to represent teacher data.
-   `scheduler.py`: Contains the `create_schedule` function, which implements the core logic of the greedy algorithm.

## How to Run

To run the program, execute the following command in your terminal:

```bash
python3 main.py
```

## Expected Output

The program will output the optimal schedule, indicating which teacher is assigned to which subjects. Please note that the program's console output will remain in Ukrainian.

```
Розклад занять:
Наталія Шевченко, 29 років, email: n.shevchenko@example.com
   Викладає предмети: Біологія, Хімія

Дмитро Бондаренко, 35 років, email: d.bondarenko@example.com
   Викладає предмети: Інформатика, Фізика

Олександр Іваненко, 45 років, email: o.ivanenko@example.com
   Викладає предмети: Математика
```