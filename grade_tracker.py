import sys
# Read command-line argument if provided
if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    mode = 'all'

#collect student data
names = []
scores = []
print('=== Student Grade Tracker ===')
print (' Enter student names and scores. Type done when finished')
# while loop to keep collecting until user types done
name = input('Enter student name (or done to stop)')

while name != 'done':
    score = int(input('enter score for ' + name + ': '))
    if score < 0 or score > 100:
        print ('score must be between 0 and 100. try again. ')
    else:
        names.append(name)
        scores.append(score)
        print(name + ' added!')
    name = input('enter student name (or done to stop): ')
print('data entry complete. ' + str(len(names)) + ' students entered.')



total = 0
highest = scores[0]
lowest = scores[0]

# for loop with range() to walk through both lists by index
for i in range(len(names)):
    total = total + scores[i]
    if scores[i] > highest:
        highest = scores[i]
    if scores[i] < lowest:
        lowest = scores[i]
average = total / len(names)
# Around the Part 2 summary block:
if mode == 'all' or mode == 'summary':
    # ... your summary print statements here ...
    print('')
    print('=== Class Summary ===')
    print('Total students: ' + str(len(names)))
    print('Class average: ' + str(round(average, 1)))
    print('Highest score: ' + str(highest))
    print('Lowest score: ' + str(lowest))


# for loop directly over the names list
for i in range(len(names)):
    score = scores[i]
    print('')
    print('=== Full Grade Report ===')



# if/elif/else to assign letter grades
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

# Around the Part 3 report block:
if mode == 'all' or mode == 'report':
    # ... your report print statements here ...
    print(f"{names[i]:<20} {score:<8} {grade:<6}")