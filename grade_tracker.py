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
        scores.append(scores)
        print(name + ' added!')
    name = input('enter student name (or done to stop): ')
print('data entry complete. ' + str(len(names)) + ' students entered.')
